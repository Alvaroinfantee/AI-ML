from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')

url = "https://edition.cnn.com/2022/04/26/economy/inflation-recession-economy-deutsche-bank/index.html"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
#print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
#print(sentiment)

if sentiment>0:
    print("Sentiment is negative")
elif sentiment>-.01 and sentiment<0.01:
    print("Sentiment is neutral")
else :
    print("Sentiment is positive")

#make it with deeper analysis