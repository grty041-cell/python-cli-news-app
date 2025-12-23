import argparse
import requests as req
x=argparse.ArgumentParser(description="a news app")
x.add_argument("choices",type=int,choices=[1,2,3,4,5],help="1:newsof Apple\n 2:news of Tesla \n 3:news about USA headlines \n 4:News about tech \n 5:News about wall street ")
y=x.parse_args()
if y.choices==1:
    url="https://newsapi.org/v2/everything?q=apple&from=2025-12-22&to=2025-12-22&sortBy=popularity&apiKey=a741bf73467b4e3090924b4597c624ed"
    a=req.get(url)
    data=a.json()
    articles=data["articles"]
    print("NEWS ABOUT APPLE")
    for i in range(len(articles)):
        print(f"{i+1}",articles[i]["title"])

if y.choices==2:
    url="https://newsapi.org/v2/everything?q=tesla&from=2025-11-23&sortBy=publishedAt&apiKey=a741bf73467b4e3090924b4597c624ed"
    a=req.get(url)
    data=a.json()
    articles=data["articles"]
    print("NEWS ABOUT TESLA")
    for i in range(len(articles)):
        print(f"{i+1}",articles[i]["title"])

if y.choices==3:
    url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=a741bf73467b4e3090924b4597c624ed"
    a=req.get(url)
    data=a.json()
    articles=data["articles"]
    print("NEWS ABOUT USA HEADLINES")
    for i in range(len(articles)):
        print(f"{i+1}",articles[i]["title"])

if y.choices==4:
    url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a741bf73467b4e3090924b4597c624ed" 
    a=req.get(url)
    data=a.json()
    articles=data["articles"]
    print("NEWS ABOUT LATEST TECH")
    for i in range(len(articles)):
        print(f"{i+1}",articles[i]["title"])


if y.choices==5:
    url="https://newsapi.org/v2/everything?domains=wsj.com&apiKey=a741bf73467b4e3090924b4597c624ed"
    a=req.get(url)
    data=a.json()
    articles=data["articles"]
    print("NEWS ABOUT LATEST TRENDS IN WALL STREET")
    for i in range(len(articles)):
        print(f"{i+1}",articles[i]["title"])

           




              

