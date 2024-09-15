from django.contrib import admin
from django.urls import path
from swastik import views

urlpatterns = [
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path("product",views.product,name='product'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("getintouch",views.getintouch,name='getintouch'),
    path('brassinsertproducts',views.brassinsertproducts,name='brassinsertproducts'),
    path('hextnutsbolts',views.hextnutsbolts,name='hextnutsbolts'),
    path('brasssensitrololivalveproducts',views.brasssensitrololivalveproducts,name='brasssensitrololivalveproducts'),
    path('bicyclepumpparts',views.bicyclepumpparts,name='bicyclepumpparts'),
    path('brasswingnutproducts',views.brasswingnutproducts,name='brasswingnutproducts'),
    path('electricpartproducts',views.electricpartproducts,name='electricpartproducts'),
    path('santrairyitems',views.santrairyitems,name='santrairyitems'),
    path('surgicalpartproducts',views.surgicalpartproducts,name='surgicalpartproducts'),
    path('brassterminals',views.brassterminals,name='brassterminals'),
    path('thankyou',views.thankyou,name='thankyou'),
    
]