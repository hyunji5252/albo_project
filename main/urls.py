from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='main_index'),
    path('signup', views.signup, name='main_signup'),
    path('signup/join', views.join, name= 'main_join'),
    path('signin', views.signin, name='main_signin'),
    path('signin/login', views.login, name='main_login'),
    path('logout', views.logout, name = 'main_logout'),
    path('upload', views.upload, name = 'main_upload'),
    path('upload/posting', views.posting, name='main_posting'),
    path('upload/posting/<int:pk>/', views.new_post, name='new_post'),
    path('upload/posting/<int:pk>/upload/', views.remove_post, name= 'remove_post'),
    path('upload/posting/<int:pk>/edit/', views.boardEdit, name= 'boardEdit'),
    path('create_comment/<int:items_id>', views.create_comment, name='create_comment'),
    path('create_reply/<int:items_id>', views.create_reply, name='create_reply'),
    path('trade', views.trade, name='trade'),
    path('upload/predict_price', views.predict_price, name='predict_price'),
    

] 

