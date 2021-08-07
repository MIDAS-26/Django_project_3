from django.conf.urls import url
from forms_app import views

urlpatterns = [
	url(r"^$", views.user, name="users"),
]