from django.shortcuts import render

# Create your views here.
def myhome(request):
	import requests
	import json

	news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6bc38b54a1044628a1a43816eb865235")
	api = json.loads(news_api_request.content)
	return render(request,'myhome.html',{'api':api})
