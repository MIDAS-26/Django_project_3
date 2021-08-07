from django import forms
from forms_app.models import User

class new_user_form(forms.ModelForm):
	class Meta():
		model = User
		fields = "__all__"

