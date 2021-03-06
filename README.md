<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <h1>FE-595 Midterm NLP API</h1>
    <h3>Developed by Tom Cifelli, Zenya Koprowski, Katie Prazdnik, and Vasu Srevatsan</h3>
</head>
<body>
<p>Our API has eight functions, described below:</p>
<ul>
    <li>sentiment: sentiment score from -1 to 1</li>
    <li>commonWords: up to the five most common words in the query</li>
    <li>posCount: counts words in the query by part-of-speech</li>
    <li>wordCount: total number of words in the query</li>
    <li>language: the language of the query</li>
    <li>longestAndShortestWords: the longest and shortest words in the query</li>
    <li>uniqueWordCount: the number of unique words in the query</li>
    <li>mostCommonWordsByPOS: the most common identified noun, verb, and adjective in the query</li>
</ul>

<p>To use our API:</p>
<ol>
    <li>make a GET or POST request to: 3.133.151.249:8000/query</li>
    <li>append the text you want to analyze in the form '?text=YourDesiredText'</li>
    <li>
        append any of the above arguments in the form '&functionName=True'
        <ul>
            <li>if no function arguments are specified, or if all function arguments are anything other than 'True',
                all eight functions will be run</li>
        </ul>
    </li>
    <li>request results are returned as a JSON dictionary alongside the version of the input text
         passed to the functions
        <ul>
            <li>to help prevent errors input text is stripped of all non-alphanumeric characters</li>
        </ul>
    </li>
</ol>

<p>You must specify the text argument in the GET/POST request,
    and it must contain at least one alphanumeric character.</p>

<p>Example Query: 3.133.151.249:8000/query?text=Example Text&sentiment=True&wordCount=True</p>
</body>
</html>
