from django.urls import include, path
from django.views.generic import TemplateView

app_name = 'pc'
urlpatterns = [
    path("", TemplateView.as_view(template_name="people_counter/home.html"), name="home"),
]
