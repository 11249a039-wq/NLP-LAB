from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
ps = PorterStemmer()
new_text = "ls is very important to be pythonly while you are pythoning with python. All pythoners have poorly pythoned atleast once"
words = word_tokenize(new_text)
for W in words:
    print(ps.stem(W))
