from urllib.request import Request, urlopen
import json
import random

#Online stuff
link = 'https://type.fit/api/quotes'
contents = urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'})).read()

#Formatting the recived information and getting one random quote
quotes = json.loads(contents)
randomQuote= random.choice(quotes)

#Printing result
print("%s\n-%s"%(randomQuote.get("text"), randomQuote.get("author")))