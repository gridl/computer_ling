from nltk.stem import PorterStemmer
from nltk import tokenize
from nltk.corpus import stopwords
tokens = tokenize.word_tokenize(open("text.txt").read())
stopWords = stopwords.words('english')
currnum = len(tokens)
i = 0
while i < len(tokens):
    if tokens[i] in stopWords:
        del tokens[i]
    else:
        i += 1
print(currnum, len(tokens))
stemmer = PorterStemmer()
percentage = (1 - len(tokens) / currnum) * 100
f = open("result.txt", "wt")
f.write("Stop words count: " + str(percentage) + " %\n")
for t in tokens:
    f.write(t + " : " + stemmer.stem(t) + "\n")
f.close()
