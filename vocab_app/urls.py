from django.urls import path
from django.contrib.auth import views as auth_views

from vocab_app.forms import CustomAuthenticationForm, CustomPasswordChangeForm
from . import views

app_name = 'vocab_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('word/<int:pk>/', views.word_detail, name='word_detail'),
    path('practice/', views.practice, name='practice'),
    path('mark-learned/<int:word_id>/', views.mark_learned, name='mark_learned'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='vocab_app/login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='vocab_app/password_change.html', form_class=CustomPasswordChangeForm, success_url='/password-change/done/'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='vocab_app/password_change_done.html'), name='password_change_done'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
