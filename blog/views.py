from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy 
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import redirect

# class BlogListView(ListView):
#     model = Post
#     template_name = 'home.html'

def BlogListView(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')  
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewPost(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')