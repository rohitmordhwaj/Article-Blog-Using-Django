from django.http import HttpResponse
from django.shortcuts import render 
from newsapi import NewsApiClient 

  
# Create your views here.  
def index(request): 
      
    newsapi = NewsApiClient(api_key ='41ff5161b7c24c03838c374031964793') 
    top = newsapi.get_top_headlines(sources ='techcrunch,bbc-news,the-verge') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
  
    return render(request, 'newsapp/index.html', context ={"mylist":mylist}) 

