from django.shortcuts import render, get_object_or_404
from .models import bloginfo

def allblog(request):
    blogdata = bloginfo.objects.order_by('-date')
    return render(request, 'blog/allblog.html',{'data': blogdata})
def detail(request, blog_id):
    blog = get_object_or_404(bloginfo, pk=blog_id)
    return render (request,'blog/detail.html',{'id':blog})
def allblogi(request):
    blogdata = bloginfo.objects.order_by('-date')[:5]
    return render(request, 'blog/allblog.html',{'data': blogdata})
