import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from textblob import TextBlob #use to determine the language of the string

def initNLTK():
    #below needs these commands to get stopwords gutenberg library and punctuation to remove punctuation before
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('gutenberg')
    nltk.download('averaged_perceptron_tagger')

def getSentiment(text):
    return TextBlob(text).sentiment.polarity

def getMostCommonWords(text):
    allWords = nltk.tokenize.word_tokenize(text.lower())
    stopWords = nltk.corpus.stopwords.words('english')
    allWordDist = nltk.FreqDist(word.lower() for word in allWords if word not in stopWords)
    n = 5 if len(allWordDist) >= 5 else len(allWordDist)
    mostCommonWords = allWordDist.most_common(n)

    #print(mostCommonWords)

    return {word[0]: word[1] for word in mostCommonWords}

def NumofPOS(self):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(self)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    tagged = pos_tag(filtered_sentence)
    counts = Counter(tag for word, tag in tagged)
    #print(counts)

    return counts

def MostCommonPOS(self):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(self)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    tagged = pos_tag(filtered_sentence)
    nouns = ([word for (word, pos) in tagged if pos[0] == 'N'])
    adjectives = ([word for (word, pos) in tagged if pos[0] == 'J'])
    verbs = ([word for (word, pos) in tagged if pos[0] == 'V'])
    print("Most common noun:", Counter(nouns).most_common(1))
    print("Most common adjective:", Counter(adjectives).most_common(1))
    print("Most common verb:", Counter(verbs).most_common(1))

    return {'mostCommonNoun': Counter(nouns).most_common(1)[0][0] if Counter(nouns).most_common(1)[0][0] is not [] else None,
            'mostCommonAdjective': Counter(adjectives).most_common(1)[0][0] if Counter(nouns).most_common(1)[0][0] is not [] else None,
            'mostCommonVerb': Counter(verbs).most_common(1)[0][0] if Counter(nouns).most_common(1)[0][0] is not [] else None}

def countwords(inputs):
    # Counts the number of words and characters in the string
    # https://www.codevscolor.com/python-count-words-characters-string
    char_count = 0
    split_string = inputs.split()
    word_count = len(split_string)
    for word in split_string:
        if not word.isalpha() | word.isdigit():
            char_count += 1
    #print("Total Words : {}".format(word_count))
    #print("Total Special Characters : {}".format(char_count))

    return {'wordCount': word_count, 'specialCharacters': char_count}

def findlanguage(inputs):
    # Uses Textblob to find the language of the inputted text
    words = TextBlob(inputs)
    #print("Detected Language : ", words.detect_language())

    return words.detect_language()

def longshort(text):
    text1 = nltk.tokenize.word_tokenize(text)
    # below makes all the words in text lowercase and takes out any punctuation
    text2 = [word.lower() for word in text1 if word.isalnum()]
    longest = ''
    for word in text2:
        if len(word) > len(longest):
            longest = word

    stopwords = nltk.corpus.stopwords.words('english')
    str1 = " "
    shortest = (str1.join(text2[0:1]))
    for word in text2:
        if word not in stopwords and len(word) < len(shortest):
            shortest = word
    #print(shortest)
    #print(longest)

    return {'longestWord': longest, 'shortestWord': shortest}

def findnumofunique(text):
    text1 = nltk.tokenize.word_tokenize(text)
    text2 = [word.lower() for word in text1 if word.isalnum()]
    unique = set()
    result = []
    for word in text2:
        if word not in unique:
            unique.add(word)
            result = result + [word]

    return len(result)
