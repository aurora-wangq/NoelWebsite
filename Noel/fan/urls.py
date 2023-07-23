from django.urls import path
from . import views
app_name = 'fan'   # 定义一个命名空间，用来区分不同应用之间的链接地址
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/',views.register_view, name='register'),
    path('edit/',views.editarticle_view, name='edit'),
    path('post/<int:post_id>',views.post_detail_view, name='post_detail'),
    path('post/<int:post_id>/like', views.post_like, name="post_like"),
    path('mypage/',views.user_page_view,name='user_page'),
    path('logout/',views.logout_view,name='logout'),
    path('edit_profile/',views.edit_profile_view,name='editp'),
    path('user/<int:user_id>', views.others_page_view, name='others_page'),
]