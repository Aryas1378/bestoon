from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    path('submite/expense/', views.submit_expense, name='submit_expense'),
    path('submite/income/', views.submit_income, name='submit_income'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout')
]
