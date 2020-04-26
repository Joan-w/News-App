from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

# Init
@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='3bf0db982cf4456b88151b7d2546f619')
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    pubAt = []
    author = []
    news = []
    desc = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        pubAt.append(myarticles['publishedAt'])
        author.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    mylist = zip(pubAt, author, news, name, desc, url)
    

    return render_template('index.html', context = mylist)

@app.route('/al-jazeera')
def al-jazeera():
    newsapi = NewsApiClient(api_key='3bf0db982cf4456b88151b7d2546f619')
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-news")

    articles = topheadlines['articles']

    pubAt = []
    author = []
    news = []
    desc = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        pubAt.append(myarticles['publishedAt'])
        author.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    mylist = zip(pubAt, author, news, name, desc, url)
    

    return render_template('index.html', context = mylist)


if __name__ == '__main__':
    app.run(debug=True)
