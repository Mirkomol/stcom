from django.shortcuts import render, redirect
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import DormPost



@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user_name = request.user
            new_item.save()
            return redirect('stdormpage')
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'stdorm/create.html', {'form': form})




def index(request):
    posts = DormPost.objects.all()
    return render(request, 'stdorm/index.html', {'posts': posts})