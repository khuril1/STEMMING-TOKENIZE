from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

words = ["Saya", "bangga", "jadi", "warga", "nahdlatul", "ulama"]

for w in words:
    print(w, ":", ps.stem(w))
