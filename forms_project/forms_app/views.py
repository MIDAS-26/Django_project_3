from django.shortcuts import render
from . import forms
# from forms_app.models import User
from forms_app.signup_form import new_user_form
# Create your views here.

def index(request):
	return render(request, "forms_app/index.html")

def form_name_view(request):
	form = forms.FormName()
	if request.method == "POST":
		form = forms.FormName(request.POST)

		if form.is_valid():
			print("Validated successfully!")
			print("NAME: " + form.cleaned_data["name"])
			print("EMAIL: " + form.cleaned_data["email"])
			print("TEXT: " + form.cleaned_data["text"])

	return render(request, "forms_app/form_page.html", {"form": form})


def user(request):
	form = new_user_form()

	if request.method == "POST":
		form = new_user_form(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR FORM INVALID")

	return render(request, "forms_app/users.html", {"form": form})
