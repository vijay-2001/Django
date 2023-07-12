from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .import forms
# Create your views here.

def hello(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'hello.html',{"articles":articles})

def article_detail(request,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'article_detail.html',{'article':article})

@login_required(login_url='/account/login')
@csrf_exempt
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('main:list')
    else:
        form = forms.CreateArticle()
    return render(request,'article_create.html',{'form':form})
