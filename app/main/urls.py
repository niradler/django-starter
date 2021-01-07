from django.conf.urls import url, include
from main.views import dashboard, register, main, profile

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^profile/", profile, name="profile"),
    url("", main, name="main"),
]
