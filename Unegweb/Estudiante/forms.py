from django import forms

class MiFormulario(forms.Form):
	nombre=forms.CharField(max_length=20)
	edad = forms.IntegerField()
