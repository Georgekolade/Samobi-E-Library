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
	return render(request, 'index.html')

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
			print(message)

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
	
	category = request.GET.get('category')

	if category:
		url = f'https://newsapi.org/v2/top-headlines?country=ng&category={category}&apiKey=bb67a387c8334df08527a8990f83713d'
		response = requests.get(url)
		data = response.json()
		articles = data['articles']
	else:
		url = f'https://newsapi.org/v2/top-headlines?country=ng&apiKey=bb67a387c8334df08527a8990f83713d'
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