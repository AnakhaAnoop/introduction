from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('buyers',views.buyers,name='buyers'),
    path('buyer_details',views.buyer_details,name='buyer_details'),
    path('prod_details',views.prod_details,name='prod_details'),
    path('all',views.all,name='all'),
]