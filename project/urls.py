from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from store.views import (
    # --- session ---
    CreateChechoutSessionView,
    CreateCheckoutSessionView_Shell,
    CreateCheckoutSessionView_Cpanel,
    CreateChechoutSessionView_Ssh,
    CreateCheckoutSessionView_Leads,
    CreateCheckoutSessionView_Smtp,
    CreateCheckoutSessionView_Mailer,
    # --- TEMPLATES ---
    SuccessView,
    CancelView,
)
from users.views import register, login_views, logout_view, profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    
    # --- Payment ---
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateChechoutSessionView.as_view(), name='create-checkout-session'),
    path('create-checkout-session-shell/<pk>/', CreateCheckoutSessionView_Shell.as_view(), name='create-checkout-session-shell'),
    path('create-checkout-session-cpanel/<pk>/', CreateCheckoutSessionView_Cpanel.as_view(), name='create-checkout-session-cpanel'),
    path('create-checkout-session-ssh/<pk>/', CreateChechoutSessionView_Ssh.as_view(), name='create-checkout-session-ssh'),
    path('create-checkout-session-leads/<pk>/', CreateCheckoutSessionView_Leads.as_view(), name='create-checkout-session-leads'),
    path('create-checkout-session-smtp/<pk>/', CreateCheckoutSessionView_Smtp.as_view(), name='create-checkout-session-smtp'),
    path('create-checkout-session-mailer/<pk>/', CreateCheckoutSessionView_Mailer.as_view(), name='create-checkout-session-mailer'),
    

    
    
    # --- Auth ---
    path('register/', register, name='register'),
    path('login/', login_views, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    
    
    
    # Password reset links
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
    name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
    name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
    name='password_reset_complete'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
