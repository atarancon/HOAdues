from django.urls import path, re_path
from . import views

app_name = 'hoadues'

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('member_page', views.member_page, name='member_page'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('check_out', views.check_out, name='check_out'),
    path('postcheck_out', views.postcheck_out, name='postcheck_out'),
    
    path('', views.index, name='index'),
]
