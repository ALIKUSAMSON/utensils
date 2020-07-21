
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cart/',views.cart,name='cart'),
    path('checkout/', views.checkout,name='checkout'),
    path('store/',views.store,name='store'),
    path('contact/',views.contact,name='contact'),
    path('courses/',views.courses,name='courses'),
    path('pricing/',views.pricing,name='pricing'),
    path('trainers/',views.trainers,name='trainers'),
    path('events/',views.events,name='events'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order')
]
