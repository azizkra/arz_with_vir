from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    context={}
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form']=form
    
    else:
        form = UserRegistrationForm()
        context['register_form']=form
    return render(request, 'users/register.html', context)


def login_views(request):
    context={}
    if request.POST:
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, ('You Were Logged In!'))
                return redirect('rdp')
            else:
                messages.warning(request, ('Ther Was An Error Logging In, Try Again...'))
                return redirect('login')
        else:
            context['login_form']=form
            
    else:
        form=UserLoginForm()
        context['login_form']=form
               
    return render(request, 'users/login.html', context)




def logout_view(request):
    logout(request)
    messages.success(request, ('You Were Logged Out!'))
    return redirect('login')



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)  
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context ={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html', context)




