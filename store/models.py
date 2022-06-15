from django.db import models
from django.urls import reverse
from django.core import validators
from users.models import NewUser
# Create your models here.


class Server_Os(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class SSL(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
# --- shell ---
class Product_Shell(models.Model):
    RUSSIA = 'RUS'
    USA = 'USA'
    GERMANY = 'GER'
  
    COUNTRY = (
        (RUSSIA, "Russia"),
        (USA, "USA"),
        (GERMANY, "Germany"),
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=3, choices=COUNTRY, default=RUSSIA)
    ssl = models.ForeignKey(SSL, on_delete=models.CASCADE)
    tld = models.CharField(max_length=20, help_text="Add Your Domain")
    server_information = models.TextField(max_length=500)
    server_os =   models.ForeignKey(Server_Os, on_delete=models.CASCADE)
    detected_hosting = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    stripe_product_id = models.CharField(max_length=100)

class PriceShell(models.Model):
    product = models.ForeignKey(Product_Shell, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def get_display_price(self):
        return self.price


class OrderDetailShell(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    customer_email = models.EmailField(verbose_name='Customer Email', max_length=255)
    product = models.ForeignKey(to=Product_Shell, verbose_name="Product Shell", on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(verbose_name='Payment Status', default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)

# --- Rdp ---
class Product_Rdp(models.Model):
 
    STATUS=(
        ('POSTED','POSTED'),
        ('HANGING','HANGING'),
    )
    RUSSIA = 'RUS'
    USA = 'USA'
    GERMANY = 'GER'
  
    COUNTRY = (
        (RUSSIA, "Russia"),
        (USA, "USA"),
        (GERMANY, "Germany"),
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    country = models.CharField(max_length=3, choices=COUNTRY, default=RUSSIA)
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, help_text="Add Your state")
    windows = models.IntegerField()
    ram = models.CharField(max_length=50)
    Access = models.CharField(max_length=100, default=1)
    detected_hosting = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    stripe_product_id = models.CharField(max_length=100)
    status_field = models.CharField(max_length=10, choices=STATUS, default='HANGING', blank=True, null=True)

class PriceRdp(models.Model):
    product = models.ForeignKey(Product_Rdp, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def get_display_price(self):
        return self.price

class OrderDetailRdp(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    customer_email = models.EmailField(verbose_name='Customer Email', max_length=255)
    product = models.ForeignKey(to=Product_Rdp, verbose_name="Product Rdp", on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(verbose_name='Payment Status', default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)



# --- cPanel ---
class Product_cPanel(models.Model):
    RUSSIA = 'RUS'
    USA = 'USA'
    GERMANY = 'GER'
  
    COUNTRY = (
        (RUSSIA, "Russia"),
        (USA, "USA"),
        (GERMANY, "Germany"),
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=3, choices=COUNTRY, default=RUSSIA)
    ssl = models.ForeignKey(SSL, on_delete=models.CASCADE)
    tld = models.CharField(max_length=20, help_text="Add Your Domain")
    detected_hosting = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    stripe_product_id = models.CharField(max_length=100)

class PriceCpanel(models.Model):
    product = models.ForeignKey(Product_cPanel, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def get_display_price(self):
        return self.price



class OrderDetailCpanel(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    customer_email = models.EmailField(verbose_name='Customer Email', max_length=255)
    product = models.ForeignKey(to=Product_cPanel, verbose_name="Product Cpanel", on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(verbose_name='Payment Status', default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)



# --- SSH ---
class Product_ssh(models.Model):
    RUSSIA = 'RUS'
    USA = 'USA'
    GERMANY = 'GER'
  
    COUNTRY = (
        (RUSSIA, "Russia"),
        (USA, "USA"),
        (GERMANY, "Germany"), 
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    country = models.CharField(max_length=3, choices=COUNTRY, default=RUSSIA)
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    ssl = models.ForeignKey(SSL, on_delete=models.CASCADE)
    tld = models.CharField(max_length=20, help_text="Add Your Domain")
    detected_hosting = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    stripe_product_id = models.CharField(max_length=100)

class PriceSsh(models.Model):
    product = models.ForeignKey(Product_ssh, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def get_display_price(self):
        return self.price

class OrderDetailSsh(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    customer_email = models.EmailField(verbose_name='Customer Email', max_length=255)
    product = models.ForeignKey(to=Product_ssh, verbose_name="Product Ssh", on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(verbose_name='Payment Status', default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)


# --- mailer ---
class Product_Mailer(models.Model):
    RUSSIA = 'RUS'
    USA = 'USA'
    GERMANY = 'GER'
  
    COUNTRY = (
        (RUSSIA, "Russia"),
        (USA, "USA"),
        (GERMANY, "Germany"),
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    country = models.CharField(max_length=3, choices=COUNTRY, default=RUSSIA)
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    detected_hosting = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    stripe_product_id = models.CharField(max_length=100)

class PriceMailer(models.Model):
    product = models.ForeignKey(Product_Mailer, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def get_display_price(self):
        return self.price
    
class OrderDetailMailer(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    customer_email = models.EmailField(verbose_name='Customer Email', max_length=255)
    product = models.ForeignKey(to=Product_Mailer, verbose_name="Product Mailer", on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(verbose_name='Payment Status', default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)



# --- SMTP ---
class Product_Smtp(models.Model):
    RUSSIA = 'RUS'
    USA = 'USA'
    GERMANY = 'GER'
  
    COUNTRY = (
        (RUSSIA, "Russia"),
        (USA, "USA"),
        (GERMANY, "Germany"),
    )
    
    YES = 'YES'
    NO = 'NO'
    
    CHOSE = (
        (YES, 'YES'),
        (NO, 'NO')
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    country = models.CharField(max_length=3, choices=COUNTRY, default=RUSSIA)
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    webmail = models.CharField(max_length=3, choices=CHOSE, default=YES)
    detected_hosting = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    stripe_product_id = models.CharField(max_length=100)

class PriceSmtp(models.Model):
    product = models.ForeignKey(Product_Smtp, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
class OrderDetailSmtp(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    customer_email = models.EmailField(verbose_name='Customer Email', max_length=255)
    product = models.ForeignKey(to=Product_Smtp, verbose_name="Product Smtp", on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(verbose_name='Payment Status', default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)



# --- lEADS ---
class Product_Leads(models.Model):
    RUSSIA = 'RUS'
    USA = 'USA'
    GERMANY = 'GER'
  
    COUNTRY = (
        (RUSSIA, "Russia"),
        (USA, "USA"),
        (GERMANY, "Germany"),
    )
    
    YES = 'YSE'
    NO = 'NO'
    
    CHOSE = (
        (YES, 'YES'),
        (NO, 'NO')
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    country = models.CharField(max_length=3, choices=COUNTRY, default=RUSSIA)
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    source = models.TextField(max_length=1000)
    Email_Domains = models.CharField(max_length=30, help_text="Add Your Domain Email")
    email_num = models.CharField(max_length=5, help_text="Add Number of Your Emails")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    stripe_product_id = models.CharField(max_length=100)

class Priceleads(models.Model):
    product = models.ForeignKey(Product_Leads, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    

class OrderDetailLeads(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    customer_email = models.EmailField(verbose_name='Customer Email', max_length=255)
    product = models.ForeignKey(to=Product_Leads, verbose_name="Product Leads", on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(verbose_name='Payment Status', default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)


class Ticket(models.Model):
    STATUS = (
        ('Unacceptable','Unacceptable'),
        ('Acceptable','Acceptable'),
        ('Pending','Pending'),
    )
    
    TITLE = (
        ('1',''),
        ('Deposit Issue(Add Balance Issue)', 'Deposit Issue(Add Balance Issue)'),
        ('Bad Item/Order','Bad Item/Order'),
        ('Report Issue','Report Issue'),
        ('ArzijShop Account Issue','ArzijShop Account Issue'),
        ('Apply for a Seller','Apply for a Seller'),
        ('Other','Other')
    )
    id = models.BigAutoField(primary_key=True, unique=True)
    title = models.CharField(verbose_name="What can help you with?", max_length=50, choices=TITLE, default='1')
    description = models.TextField(verbose_name="Description")
    added_by_seller = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    
    
    
    
    