from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    return render(request,'Home/index.html',{'blogs':blogs})

@login_required
def create_Blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request,'Home/create.html',{'form':form})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'Home/blog_detail.html', {'blog': blog})

@login_required
def update_blog(request,pk):
    if request.user == get_object_or_404(Blog,pk=pk).author: 
        # or you can Do this if request.user == Blog.objects.get(pk=pk).author:
        blog=get_object_or_404(Blog,pk=pk)
        form=BlogForm(instance=blog)
   
        if request.method == 'POST':
            form=BlogForm(request.POST,request.FILES,instance=blog)
            if form.is_valid():
                form.save()
                return redirect('blog_detail',pk=blog.pk)
            else:
                print(form.errors)
            
        context={'form':form}
    
        return render(request,'Home/create.html',context)
    else :
        return HttpResponse("<h1> You are not allowed to edit this blog </h1>",status=403)
    
@login_required
def delete_blog(request,pk):
    if request.user == Blog.objects.get(pk=pk).author:
        blog=Blog.objects.get(pk=pk)
        blog.delete()
        return redirect('home')
    else :
        return HttpResponse("<h1> You are not allowed to delete this blog </h1>",status=403)
@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'Home/blog_detail.html', {'blog': blog})
