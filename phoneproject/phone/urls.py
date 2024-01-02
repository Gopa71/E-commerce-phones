from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.allProCat,name='allProCat'),
    path('<slug:c_slug>',views.allProCat,name='products_by_category'),
    path('details/<int:id>',views.details,name='details')
]