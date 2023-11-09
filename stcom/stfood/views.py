from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from . models import Item
from .forms import ItemForm


class IndexClassView(ListView):
    model = Item
    paginate_by = 4

    template_name = 'stfood/index.html'
    context_object_name = 'item_list'


    def get_queryset(self):
        query = self.request.GET.get('item_search')
        if query:
            return Item.objects.filter(item_name__icontains=query)
        else:
            return Item.objects.all()






class  FoodDetail(DetailView):
    model = Item
    template_name = 'stfood/detail.html'



#
# class CreateItem(CreateView):
#     model = Item
#     fields = ['item_name', 'item_desc', 'item_price', 'item_image']
#     template_name = 'stfood/item_form.html'
#
#
#     def form_valid(self, form):
#
#         form.instance.user_name = self.request.user
#         return super().form_valid(form)
#
#


@login_required
def CreateFood(request):
    if request.method == 'POST':
        form = ItemForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user_name = request.user
            new_item.save()
            return redirect('stfood:stfood')
    else:
        form = ItemForm(data=request.GET)
    return render(request, 'stfood/item_form.html', {'form': form})





def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)


    if form.is_valid():
        form.save()
        return redirect('stfood:stfood')

    return render(request, 'stfood/item_form.html',{'form':form, 'item':item})



def delete_item(request,id):

    item = Item.objects.get(id=id)


    if request.method == 'POST':
        item.delete()
        return redirect('stfood:stfood')

    return render(request, 'stfood/item_delete.html',{'item':item})
