from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core import mail
from django.http import HttpResponse
from django.contrib import messages
from .form import MessageForms, UploadForms
from .models import Upload
from bs4 import BeautifulSoup
from django.template import loader
import requests

# Create your views here.
def index(request):
	url = "https://www.legit.ng/latest/"
	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')
	lists = soup.find_all('article', class_='c-article-card-no-border')

	template = loader.get_template('index.html')
	context = {"data":[], "article" : []}

	for i in lists:
		title = i.find('a', class_='c-article-card-no-border__headline').attrs['href']
		headlines = i.find('span', class_='c-article-card-no-border__headline-hover-inner').text
		time = i.find('time', class_='c-article-info__time--clock').text
		image = i.find('img', class_='lazyload thumbnail-picture__img').attrs['src']

		context["data"].append(dict({"title" : title, "headlines" : headlines, "time" : time, "image" : image}))

	article = soup.find_all('article', class_="c-article-card")

	for j in article:
		title = j.find('a', class_='c-article-card__headline').attrs['href']
		headline = j.find('span', class_='c-article-card__headline-hover-inner').text
		time = j.find('time', class_='c-article-info__time--clock').text

		context["article"].append(dict({"title" : title, "headline" : headline, "time" : time}))

	return HttpResponse(template.render(context, request))

def contact(request):
	if request.method == "POST":
		form = MessageForms(request.POST or None)
		if form.is_valid():
			form.save()
			subject = 'Samobi E-library Remarks'
			body = {
			'Name': form.cleaned_data['name'], 
			'E-mail': form.cleaned_data['email'], 
			'Subject': form.cleaned_data['subject'], 
			'Message': form.cleaned_data['message']
			}
			message = "\n".join(f'{k}: {v}' for k,v in body.items())

			try:
				send_mail(subject, message, 'koladegeorge5@gmail.com', ['koladegeorge5@gmail.com', 'obigbesanayodeji@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/contact")
	form = MessageForms()
	return render(request, 'contact.html', {"form" : form})

def news(request):
	url = 'https://newsapi.org/v2/top-headlines?country=ng&apiKey=bb67a387c8334df08527a8990f83713d'
	response = requests.get(url)
	data = response.json()

	articles = data['articles']

	context = {
		'articles' : articles
	}
	return render(request, 'news.html', context)

def download(request):
	fetch_data = Upload.objects.all()
	return render(request, 'download.html', {"fetch_data" : fetch_data})

def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		books = Upload.objects.filter(name__contains = searched)
	return render(request, 'search.html', {'searched' : searched, 'books' : books})

def upload(request):
	if request.method == 'POST':
		form = UploadForms(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = UploadForms()
	return render(request, 'upload.html', {"form" : form})