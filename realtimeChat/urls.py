from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chatapp.views import index
from chatapp import views as core_views

urlpatterns = [
    path('', index),
    path('login/', login, {'template_name': 'login.html'},name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),
    path('admin/', admin.site.urls),

    path('account_activation_sent/', core_views.account_activation_sent, name='account_activation_sent'),
    path('signup/', core_views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', core_views.activate,
            name='activate'),
]

