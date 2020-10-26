from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
# def indexView(request):
# 	return render(request,'baseblog.html')

class IndexView(ListView):
	model = Post
	template_name = 'indexblog.html'

class PostDetailView(DetailView):
	model=Post
	template_name= 'postdetail.html'
class CreatePostView(CreateView):
	model=Post
	template_name= 'addpost.html'
	fields='__all__'
class PostEditView(UpdateView):
	model=Post
	template_name='editpost.html'	
	fields=['title','body']		
class PostDeleteView(DeleteView):
	model=Post
	template_name='deletepost.html'	
	success_url = reverse_lazy('home')