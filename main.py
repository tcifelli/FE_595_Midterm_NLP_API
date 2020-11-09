from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
import NLPMethods

app = Flask(__name__)

NLPMethods.initNLTK()

funcDict = {
    'sentiment': NLPMethods.getSentiment,
    'commonWords': NLPMethods.getMostCommonWords,
    'posCount': NLPMethods.NumofPOS,
    'wordCount': NLPMethods.countwords,
    'language': NLPMethods.findlanguage,
    'longestAndShortestWords': NLPMethods.longshort,
    'uniqueWordCount': NLPMethods.findnumofunique,
    'mostCommonWordsByPOS': NLPMethods.MostCommonPOS
}

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/query', methods=['GET', 'POST'])
def query():
    rawText = request.args.get('text')

    if rawText is None:
        raise BadRequest("No text supplied for analysis. Please specify the 'text' argument in your api call using query?text=YourText")

    #ensure text contains only alphanumeric characters or spaces
    #modified from: https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
    text = ''.join(e for e in rawText if e.isalnum() or e == ' ')

    args = {
        'sentiment': request.args.get('sentiment'),
        'commonWords': request.args.get('commonWords'),
        'posCount': request.args.get('posCount'),
        'wordCount': request.args.get('wordCount'),
        'language': request.args.get('language'),
        'longestAndShortestWords': request.args.get('longestAndShortestWords'),
        'uniqueWordCount': request.args.get('uniqueWordCount'),
        'mostCommonWordsByPOS': request.args.get('mostCommonWordsByPOS')
    }

    cleanedArgs = [arg if arg is not None else False for arg in args.values()]
    boolArgs = [arg if isinstance(arg, bool) else str(arg).lower() == "true" for arg in cleanedArgs]
    boolArgs = boolArgs if sum(boolArgs) > 0 else [True] * len(boolArgs) #run all funcs if none specified

    results = {'inputText': text}
    for funcName, func, runFunc in zip(funcDict.keys(), funcDict.values(), boolArgs):
        if runFunc:
            results[funcName] = func(text)

    #return f"{text}"
    return results

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
