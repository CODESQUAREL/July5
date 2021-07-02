from django.urls import path

from accountapp.views import CODE_SQUARE

app_name = "accountapp"


urlpatterns = [
    path('CODE_SQUARE/', CODE_SQUARE, name='CODE_SQUARE')
]