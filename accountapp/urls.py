from django.urls import path

from accountapp.views import code_square, AccountCreateView

app_name = "accountapp"


urlpatterns = [
    path('CODE_SQUARE/', code_square, name='CODE_SQUARE'),

    path('create/', AccountCreateView.as_view(), name = 'create')
]