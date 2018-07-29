from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from blog_posts.models import blog_posts
from . import forms
# Create your views here.
def index(request):
    return render(request,'blog_posts/index.html')


def form_name_view(request):
    form=forms.FormName()

    if request.method == 'POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("Hey this is successfully validation")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
    return render(request,'blog_posts/form_page.html',{'form':form})



class PostsForm(ModelForm):
    class Meta:
        model = blog_posts
        fields = ['id', 'title', 'author']
def post_list(request, template_name='blog_posts/post_list.html'):
    posts = blog_posts.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)
def post_create(request, template_name='blog_posts/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})
def post_update(request, pk, template_name='blog_posts/post_form.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})
def post_delete(request, pk, template_name='blog_posts/post_delete.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'object': post})