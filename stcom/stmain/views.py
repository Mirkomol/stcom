from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import CreateView,ListView

from django.views import generic

from .forms import PostForm
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'stmain/stmain.html'
    context_object_name = 'post_list'

    paginate_by = 4



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'stmain/post_detail.html'



class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'stmain/post_form.html'


    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def delete_blog(request,id):

    blog = Post.objects.get(id=id)

    if request.method == 'POST':
        blog.delete()
        return redirect('stmain:main')

    return render(request, 'stmain/blog_delete.html',{'blog': 'blog'})
