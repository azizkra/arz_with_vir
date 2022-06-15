from django.contrib import admin

from .models import (
        PriceMailer,
        PriceSmtp,
        Priceleads,
        Product_Rdp,
        Product_ssh,
        Product_cPanel,
        Product_Leads,
        Product_Smtp,
        Product_Shell,
        Product_Mailer,
        Server_Os,
        SSL,
        Ticket,
        #--------------
        PriceRdp,
        PriceShell,
        PriceCpanel,
        PriceSsh,
        
        
    )
# Register your models here.
# --- RDP --- 
class PricesRdpInlineAdmin(admin.TabularInline):
    model = PriceRdp
    extra = 0
    
class Product_Rdp_Admin(admin.ModelAdmin):
    inlines = [PricesRdpInlineAdmin]

# --- SHELL --- 
class PricesShellInlineAdmin(admin.TabularInline):
    model = PriceShell
    extra = 0
    
class Product_Shell_Admin(admin.ModelAdmin):
    inlines = [PricesShellInlineAdmin]

# --- Cpanel ---
class ProductCpanelInlineAdmin(admin.TabularInline):
    model = PriceCpanel
    extra = 0

class Product_Cpanel_Admin(admin.ModelAdmin):
    inlines = [ProductCpanelInlineAdmin]
    
# --- SSH ---
class ProductSshInlineAdmin(admin.TabularInline):
    model = PriceSsh
    extra = 0

class Product_Ssh_Admin(admin.ModelAdmin):
    inlines = [ProductSshInlineAdmin]
    

# --- Leads ---
class ProductLeadsInlineAdmin(admin.TabularInline):
    model = Priceleads
    extra = 0

class Product_Leads_Admin(admin.ModelAdmin):
    inlines = [ProductLeadsInlineAdmin] 
    
# --- Mailer ---
class ProductMailerInlineAdmin(admin.TabularInline):
    model = PriceMailer
    extra = 0

class Product_Mailer_Admin(admin.ModelAdmin):
    inlines = [ProductMailerInlineAdmin] 

# --- SSH ---
class ProductSmtpInlineAdmin(admin.TabularInline):
    model = PriceSmtp
    extra = 0

class Product_Smtp_Admin(admin.ModelAdmin):
    inlines = [ProductSmtpInlineAdmin] 


    
admin.site.register(Product_Rdp, Product_Rdp_Admin)
admin.site.register(Product_Shell, Product_Shell_Admin)
admin.site.register(Product_ssh, Product_Ssh_Admin)
admin.site.register(Product_cPanel, Product_Cpanel_Admin)
admin.site.register(Product_Leads, Product_Leads_Admin)
admin.site.register(Product_Smtp, Product_Smtp_Admin)
admin.site.register(Product_Mailer, Product_Mailer_Admin)
admin.site.register(Server_Os)
admin.site.register(SSL)
admin.site.register(Ticket)