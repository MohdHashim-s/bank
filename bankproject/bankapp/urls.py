from . import views
from django.urls import path,include


from django.conf.urls.static import static
app_name='bank'
urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout,name='logout'),


]