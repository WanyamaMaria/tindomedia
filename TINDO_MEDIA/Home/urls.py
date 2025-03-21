from django.contrib import admin
from django.urls import path,include


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('Home/', include('Home.urls'))
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/', views.contact, name='contact'),
]
