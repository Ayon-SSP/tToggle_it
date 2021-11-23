"""
step1:
    I have used win32com module for voice speak.
    which converts text to speak
    url = [https://youtu.be/5Sf_Eaqri08]
step2:
    learn json and request module
    json:- JavaScript Object Notation is a format for structuring data.
    It is mainly used for storing and transferring data between the browser and the server. 
    Python too supports JSON with a built-in package called json.
    [https://youtu.be/9U4dHBOzmaE]
stem3:
    start working
"""
# learned from harry

def speat(str):
    # Speak function
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.speak(str)
import requests
import json
if __name__ == '__main__':
    speat("news for today...")
    print("1)Apple\n2)Tesla\n3)Business")
    news_number = int(input())
    if 1==news_number:
        url_apple = "https://newsapi.org/v2/everything?q=apple&from=2021-11-22&to=2021-11-22&sortBy=popularity&apiKey=7ef9d4c56dd34894a9576f97a9b62c2d"
        url_select = url_apple
    elif news_number==2:
        url_tesla = "https://newsapi.org/v2/everything?q=tesla&from=2021-10-23&sortBy=publishedAt&apiKey=7ef9d4c56dd34894a9576f97a9b62c2d"
        url_select = url_tesla
    elif news_number==3:
        url_business = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7ef9d4c56dd34894a9576f97a9b62c2d"
        url_select = url_business

    news = requests.get(url_select).text
    # print(news)
    news_dict =json.loads(news)
    arts = news_dict['articles']
    print("///////////////////////////////////////////////////////////")
    for article,i in zip(arts,range(1,10)):
        print(article['author'])
        print(f"{i})",end=" ")
        print(article['title'])
        # print(article['title'])
        speat(article['title'])
        print("for more click on the link",end=" :-")
        print(article['url'])
        print("-*-*-*-*-*-*-*--*-*-*-*-*-*-*--*-*-*-*-*-*-*--*-*-*-*-*-*-*")
        speat("next")
    speat("Thanks for lesoning...")
