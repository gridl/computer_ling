
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt') #Опционально

text = '''
«Пуськи бятые» — цикл «лингвистических сказок» Людмилы Петрушевской, написанных в разные годы её творчества. Первая из них, с таким же названием, была написана в 1984 году и впервые опубликована тогда же в «Литературной газете».
'''
tokens = word_tokenize(text)

from nltk.stem import PorterStemmer

stemsPorter = []
porter = PorterStemmer()
for w in tokens:
    a = w
    w = porter.stem(w)
    if w != "":
        stemsPorter.append(w)

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

text = '«Пуськи бятые» — цикл «лингвистических сказок» Людмилы Петрушевской, написанных в разные годы её творчества. Первая из них, с таким же названием, была написана в 1984 году и впервые опубликована тогда же в «Литературной газете».'
tokens = word_tokenize(text)
stems = []
stemmer = SnowballStemmer("russian")
for token in tokens:
	token = stemmer.stem(token)
	if token != "":
		stems.append(token)

from nltk.corpus import stopwords

nltk.download('stopwords')
text = ''' Ходят по земле с инструментами, маленькими метелочками и кисточками люди и отыскивают места обитания удивительных животных динозавров, живших миллионы лет назад. Никто никогда их не видел, но в горных породах сохранились их кости. Ученые-палеонтологи раскапывают, промывают и восстанавливают скелет, а потом воссоздают внешний вид динозавра. Это долгая и скрупулезная работа, ведь за миллионы лет кости стали хрупкими. '''

download_stopwords = stopwords.words('russian')
stop_text = []
tokens = word_tokenize(text)
for i in tokens:
	if i not in download_stopwords:
		stop_text.append(i)

for word in download_stopwords:
	i = 0
	while i < len(tokens):
		if tokens[i] == word:
			del tokens[i]
		else:
			i += 1
print("Origin")
print(text)
print("Worked out")
print(" ".join(tokens))
