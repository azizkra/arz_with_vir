from coinbase_commerce.client import Client
from project import settings
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.views import View
import stripe



from .models import (
        Product_Rdp,
        Product_ssh,
        Product_cPanel,
        Product_Leads,
        Product_Smtp,
        Product_Shell,
        Product_Mailer,
        #--------------
        OrderDetailRdp,
        #-------------
        Ticket,
        #------ Prices -------
        PriceRdp,
        PriceShell,
        PriceCpanel,
        PriceSsh,
        PriceSmtp,
        PriceMailer,
        Priceleads,
        
)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# Create your views here.


stripe.api_key = settings.STRIPE_PUBLIC_KEY

# --- RDP_Session ---
class CreateChechoutSessionView(View):
    def post(self, request, *args, **kwargs):
        pricerdp = PriceRdp.objects.get(id=self.kwargs['pk'])
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'alipay', 'us_bank_account'],
            line_items=[
                {
                    'price': pricerdp.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)

# --- CPANEL_Session ---
class CreateCheckoutSessionView_Cpanel(View):
    def post(self, request, *args, **kwargs):
        price_cpanel = PriceCpanel.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'alipay', 'us_bank_account'],
            line_items=[
                {
                    'price': price_cpanel.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)

# --- SSH_Session ---
class CreateChechoutSessionView_Ssh(View):
    def post(self, request, *args, **kwargs):
        pricessh = PriceSsh.objects.get(id=self.kwargs['pk'])
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'alipay', 'us_bank_account'],
            line_items=[
                {
                    'price': pricessh.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)

# --- SHELL_Session ---
class CreateCheckoutSessionView_Shell(View):
    def post(self, request, *args, **kwargs):
        price_shell = PriceShell.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'alipay', 'us_bank_account'],
            line_items=[
                {
                    'price': price_shell.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


# --- leads_Session ---
class CreateCheckoutSessionView_Leads(View):
    def post(self, request, *args, **kwargs):
        price_leads = Priceleads.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'alipay', 'us_bank_account'],
            line_items=[
                {
                    'price': price_leads.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


# --- SMTP_Session ---
class CreateCheckoutSessionView_Smtp(View):
    def post(self, request, *args, **kwargs):
        price_smtp = PriceSmtp.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'alipay', 'us_bank_account'],
            line_items=[
                {
                    'price': price_smtp.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)

# --- MAILER_Session ---
class CreateCheckoutSessionView_Mailer(View):
    def post(self, request, *args, **kwargs):
        price_Mailer = PriceMailer.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'alipay', 'us_bank_account'],
            line_items=[
                {
                    'price': price_Mailer.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)



class SuccessView(TemplateView):
    template_name = "store/success.html"

class CancelView(TemplateView):
    template_name = "store/cancel.html"

# --- Ticket ---
class Ticket_List(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'ticket_list'
    template_name = 'store/ticket.html'
    ordering =['-created_on']
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        ticket = self.get_object()
        if self.request.user == ticket.added_by_seller:
            return True
        return False
    
    
class Ticket_Create(LoginRequiredMixin, CreateView):
    model = Ticket
    fields=['title', 'description',]
    success_url = reverse_lazy('ticket')
    
    def form_valid(self, form):  #to valid user 
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)

# ---RDP----
class Rdp_List(LoginRequiredMixin, ListView):
    model = Product_Rdp
    queryset = Product_Rdp.objects.filter(status_field='POSTED')
    context_object_name = 'rdp_list'
    template_name ='store/rdp.html'
    ordering =['-added_on']
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        rdp = self.get_object()
        if self.request.user == rdp.added_by_seller:
            return True
        return False

class Rdp_Create(LoginRequiredMixin, CreateView):
    model = Product_Rdp
    fields=['country','state','windows','ram','Access','detected_hosting','price']
    success_url = reverse_lazy('rdp') #URL of the the page that the user should be redirected to, after saving the form

    def form_valid(self, form):  #to valid user 
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)
    
class Rdp_Detail(DetailView):
    model = Product_Rdp
    template_name = 'store/rdp_detail.html'
    pk_url_kwarg='id'
    
class ProductRdpLanding(TemplateView):
    template_name = 'store/landing_rdp.html'
    
    def get_context_data(self, **kwargs):
        
        product = Product_Rdp.objects.get(id=self.kwargs["id"])
        prices = PriceRdp.objects.filter(product=product)
        context = super(ProductRdpLanding, self).get_context_data(**kwargs)
        context.update({
            "product":product,
            "prices":prices
        })
        return context


# --- SSH ----
class Shh_List(LoginRequiredMixin, ListView):
    model = Product_ssh
    context_object_name = 'shh_list'
    template_name ='store/ssh.html'
    ordering =['-added_on']
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        shh = self.get_object()
        if self.request.user == shh.added_by_seller:
            return True
        return False

class Shh_Create(LoginRequiredMixin, CreateView):
    model = Product_ssh
    fields=['country','ssl','tld','detected_hosting','price']
    success_url = reverse_lazy('ssh')
    
    def form_valid(self, form):  #to valid user 
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)
    
class Shh_Detail(DetailView):
    model = Product_ssh
    template_name = 'store/ssh_detail.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(Shh_Detail, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY

class ProductLandingPageView_Ssh(TemplateView):
    template_name = "store/landing_ssh.html"

    def get_context_data(self, **kwargs):
        product = Product_ssh.objects.get(id=self.kwargs["id"])
        prices = PriceSsh.objects.filter(product=product)
        context = super(ProductLandingPageView_Ssh,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context 



# ---CPANEL----    
class Cpanel_List(LoginRequiredMixin, ListView):
    model = Product_cPanel
    context_object_name = 'cpanel_list'
    template_name ='store/cpanel.html'
    ordering =['-added_on']
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        cpanel = self.get_object()
        if self.request.user == cpanel.added_by_seller:
            return True
        return False

class Cpanel_Create(LoginRequiredMixin, CreateView):
    model = Product_cPanel
    fields=['country','ssl', 'tld', 'detected_hosting', 'price']
    success_url = reverse_lazy('cpanel')
    
    def form_valid(self, form):  #to valid user 
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)

class Cpanel_Detail(DetailView):
    model = Product_cPanel
    template_name = 'store/cpanle_detail.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(Cpanel_Detail, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        

class ProductLandingPageView_Cpanel(TemplateView):
    template_name = "store/landing_cpanel.html"

    def get_context_data(self, **kwargs):
        product = Product_cPanel.objects.get(id=self.kwargs["id"])
        prices = PriceCpanel.objects.filter(product=product)
        context = super(ProductLandingPageView_Cpanel,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context       

# ---Shell---- 
class Shell_List(LoginRequiredMixin, ListView):
    model = Product_Shell
    context_object_name = 'shell_list'
    template_name ='store/shells.html'
    ordering =['-added_on']
    
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        shell = self.get_object()
        if self.request.user == shell.added_by_seller:
            return True
        return False

class Shell_Create(LoginRequiredMixin, CreateView):
    model = Product_Shell
    fields=['country','ssl','tld','server_information','server_os','detected_hosting','price']
    success_url = reverse_lazy('shell')
    
    def form_valid(self, form):  #to valid user 
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)
    
class Shell_Detail(DetailView):
    model = Product_Shell
    template_name = 'store/shell_detail.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(Shell_Detail, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY

class ProductShellLanding(TemplateView):
    template_name = "store/landing_shell.html"

    def get_context_data(self, **kwargs):
        product = Product_Shell.objects.get(id=self.kwargs["id"])
        prices = PriceShell.objects.filter(product=product)
        context = super(ProductShellLanding,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context     

# ---Mailer----            
class Mailer_List(LoginRequiredMixin, ListView):
    model = Product_Mailer
    context_object_name = 'mailer_list'
    template_name ='store/mailer.html'
    ordering =['-added_on']
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        mailer = self.get_object()
        if self.request.user == mailer.added_by_seller:
            return True
        return False

class Mailer_Create(LoginRequiredMixin, CreateView):
    model = Product_Mailer
    fields=['country','detected_hosting','price']
    success_url = reverse_lazy('mailer')
    
    def form_valid(self, form):  #to valid user
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)

class Mailer_Detail(DetailView):
    model = Product_Mailer
    template_name = 'store/mailer_detail.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(Mailer_Detail, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
    
class ProductLandingPageView_Mailer(TemplateView):
    template_name = 'store/landing_mailer.html'
    
    def get_context_data(self, **kwargs):
        product = Product_Mailer.objects.get(id=self.kwargs["id"])
        prices = PriceMailer.objects.filter(product=product) 
        context = super(ProductLandingPageView_Mailer, self).get_context_data(**kwargs)
        context.update({
            "product":product,
            "prices":prices
        })
        return context



# ---Smtp----            
class Smtp_List(LoginRequiredMixin, ListView):
    model = Product_Smtp
    context_object_name = 'smtp_list'
    template_name ='store/smtp.html'
    ordering =['-added_on']
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        smtp = self.get_object()
        if self.request.user == smtp.added_by_seller:
            return True
        return False

class Smtp_Create(LoginRequiredMixin, CreateView):
    model = Product_Smtp
    fields=['country','webmail','detected_hosting','price']
    success_url = reverse_lazy('smtp')
    
    def form_valid(self, form):  #to valid user 
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)
    
    

class Smtp_Detail(DetailView):
    model = Product_Smtp   
    template_name = 'store/smtp_detail.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(Smtp_Detail, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY

class ProductLandingPageView_Smtp(TemplateView):
    template_name = 'store/landing_smtp.html'
    
    def get_context_data(self, **kwargs):
        product = Product_Smtp.objects.get(id=self.kwargs["id"])
        prices = PriceSmtp.objects.filter(product=product) 
        context = super(ProductLandingPageView_Smtp, self).get_context_data(**kwargs)
        context.update({
            "product":product,
            "prices":prices
        })
        return context     

# ---Leads----                
class Leads_List(LoginRequiredMixin, ListView):
    model = Product_Leads
    context_object_name = 'leads_list'
    template_name ='store/leads.html'
    ordering =['-added_on']
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        Leads = self.get_object()
        if self.request.user == Leads.added_by_seller:
            return True
        return False

class Leads_Create(LoginRequiredMixin, CreateView):
    model = Product_Leads
    fields=['country', 'source', 'Email_Domains', 'email_num', 'price']
    success_url = reverse_lazy('leads')
    
    def form_valid(self, form):  #to valid user
        form.instance.added_by_seller = self.request.user
        return super().form_valid(form)
    

    

class Leads_Detail(DetailView):
    model = Product_Leads
    template_name = 'store/leads_detail.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(Leads_Detail, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
    

class ProductLandingPageView_Leads(TemplateView):
    template_name = 'store/landing_Leads.html'
    
    def get_context_data(self, **kwargs):
        product = Product_Leads.objects.get(id=self.kwargs["id"])
        prices = Priceleads.objects.filter(product=product) 
        context = super(ProductLandingPageView_Leads, self).get_context_data(**kwargs)
        context.update({
            "product":product,
            "prices":prices
        })
        return context



# --- coin base --- 
# def home(request):
#     s = [
#         # '7ad17d2b-a36c-4992-9d2a-4cf69f2f1c96',
#         # '8f5a1c1b-e74d-4b40-b09e-637d9fd2a842',
#         # 'b00c08db-3f2b-450a-8f5c-7cdce31da58c',
#         '88a18a00-1311-4efa-9f9d-be72efbc4b7a',
#     ]
    
#     client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
#     checkout = []
#     i = 0
#     for x in s:
#         obj = {
#             'data': client.checkout.retrieve(s[i]),
#             'link': f'https://commerce.coinbase.com/checkout/{s[i]}'
            
#         }
#         print(obj)
#         checkout.append(obj)
#         i +=1
 
#     return render(request, 'store/home.html', {
#         'checkout': checkout,
#     })