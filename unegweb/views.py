from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	boldmessage="Crunchy, creamy, cookie, candy, cupcake!"
	diccionario = {  
		'boldmessage': boldmessage,
	}
	return render(request,"index.html",diccionario)

"""
#Con este estoy trabajando#
"""

def about(request):
	context={}
	return render (request,"about.html",{})

"""########################"""

def another(request):
	diccionario = {

	}
	return render(request,"another.html",diccionario)
def mobile(request):
	context={}
	return render(request,"mobile.html",context)
