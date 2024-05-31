from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('product/',views.product),
    path('event/',views.event),
    path('signout/',views.signout),
    path('myprofile/',views.myprofile),
    path('mycart/',views.mycart),
    path('cartitems/',views.cartitems),
    path('order/',views.morder),
    path('indexcart/',views.indexcart),
    path('mprofile/',views.mprofile),
    path('orderslist/',views.orderslist)
]