from django.urls import path
from .views import (
    #home,
    Rdp_List,
    Shh_List,
    Cpanel_List,
    Shell_List,
    Mailer_List,
    Smtp_List,
    Leads_List,
    Ticket_List,
    # --- detail ---
    Rdp_Detail,
    Shh_Detail,
    Cpanel_Detail,
    Shell_Detail,
    Mailer_Detail,
    Smtp_Detail,
    Leads_Detail,
    # --- create ---
    Rdp_Create,
    Shh_Create,
    Cpanel_Create,
    Shell_Create,
    Mailer_Create,
    Smtp_Create,
    Leads_Create,
    Ticket_Create,
    # --- for payment ---
    ProductRdpLanding,
    ProductShellLanding,
    ProductLandingPageView_Cpanel,
    ProductLandingPageView_Ssh,
    ProductLandingPageView_Leads,
    ProductLandingPageView_Smtp,
    ProductLandingPageView_Mailer,
    
)
    
urlpatterns = [
    
    # ---COINBASE---
    #path('', home, name='home'),
    
    
    # ---RDP----
    path('rdp/', Rdp_List.as_view(), name='rdp'),
    path('rdp/new/', Rdp_Create.as_view(), name='rdp-create'),
    path('rdp/<id>/', Rdp_Detail.as_view(), name='rdp-detail'),
    
    # ---SSH----
    path('ssh/', Shh_List.as_view(), name='ssh'),
    path('ssh/new/', Shh_Create.as_view(), name='ssh-create'),
    path('ssh/<id>/', Shh_Detail.as_view(), name='ssh-detail'),
    
    # ---CPANEL----  
    path('cPanel/', Cpanel_List.as_view(), name='cpanel'),
    path('cPanel/new/', Cpanel_Create.as_view(), name='cpanel-create'),
    path('cPanel/<id>/', Cpanel_Detail.as_view(), name='cpanel-detail'),
    
    # ---Shell----
    path('shell/', Shell_List.as_view(), name='shell'),
    path('shell/new/', Shell_Create.as_view(), name='shell-create'),
    path('shell/<id>/', Shell_Detail.as_view(), name='shell-detail'),

    # ---Mailer----     
    path('mailer/', Mailer_List.as_view(), name='mailer'),
    path('mailer/new/', Mailer_Create.as_view(), name='mailer-create'),
    path('mailer/<id>/', Mailer_Detail.as_view(), name='mailer-detail'),

    # ---Smtp----
    path('smtp/', Smtp_List.as_view(), name='smtp'),
    path('smtp/new/', Smtp_Create.as_view(), name='smtp-create'),
    path('smtp/<id>/', Smtp_Detail.as_view(), name='smtp-detail'),
    
    # ---Leads---- 
    path('leads/', Leads_List.as_view(), name='leads'),
    path('leads/new/', Leads_Create.as_view(), name='leads-create'),
    path('leads/<id>/', Leads_Detail.as_view(), name='leads-detail'),
    
    # --- Ticket ---
    path('ticket/', Ticket_List.as_view(), name='ticket'),
    path('ticket/new/', Ticket_Create.as_view(), name='ticket-create'),

    # --- landing PAge ---
    path('rdp_landing/<id>/', ProductRdpLanding.as_view(), name='landing-rdp'), 
    path('shell_landing/<id>/', ProductShellLanding.as_view(), name='landing-shell'),    
    path('cpanel_landing/<id>/', ProductLandingPageView_Cpanel.as_view(), name='landing-cpanel'),
    path('ssh_landing/<id>/', ProductLandingPageView_Ssh.as_view(), name='landing-ssh'),    
    path('leads_landing/<id>/', ProductLandingPageView_Leads.as_view(), name='landing-leads'),    
    path('smtp_landing/<id>/', ProductLandingPageView_Smtp.as_view(), name='landing-smtp'),    
    path('mailer_landing/<id>/', ProductLandingPageView_Mailer.as_view(), name='landing-mailer'),    
        
        
    #--- Payment ----
    #path('success/', views.PaymentSuccessView.as_view(), name='success'),
    #path('failed/', views.PaymentFailedView.as_view(), name='failed'),
    #path('history/', views.OrderHistoryListView.as_view(), name='history'),

    #path('api/checkout-session/<id>/', views.create_checkout_session, name='api_checkout_session'),
]
