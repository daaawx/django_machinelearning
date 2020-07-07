from django.urls import include, path
from django.views.generic import TemplateView

app_name = 'os'
urlpatterns = [
    path("", TemplateView.as_view(template_name="object_searcher/home.html"), name="home"),
]
