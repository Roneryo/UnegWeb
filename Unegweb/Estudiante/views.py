from django.shortcuts import render

from .forms import MiFormulario
# Create your views here.

def Registro(request):
	form=MiFormulario()
	context={
		"form":form
	}
	return render(request,"registro.html",context)
