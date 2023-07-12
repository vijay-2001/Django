from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('main:list')
    else:    
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

@csrf_exempt
def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('main:list')
            
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("main:list")