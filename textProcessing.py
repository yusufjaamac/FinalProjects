import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
#nltk.download('punkt')

def textConvert():
    print("--------------------------------------------------------------------------------")

    text = "https://www.geeksforgeeks.org/"
    text_tokens = word_tokenize(text)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

    print(tokens_without_sw)

