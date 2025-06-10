from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category

# Create your views here.

def browse(request):
	query = request.GET.get('query', '')
	category_id = int(request.GET.get('category_id', 0))
	categories = Category.objects.all()
	items = Item.objects.filter(
		is_sold=False
	)

	if category_id:
		items = items.filter(
			category_id=category_id
		)
	if query:
		items = items.filter(
			Q(name__icontains=query) | Q(description__icontains=query)
		)

	return render(request, 'item/browse.html', {
		'items': items,
		'query': query,
		'categories': categories,
		'category_id': category_id,
	})

def detail(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	related_items = Item.objects.filter(
		category=item.category,
		is_sold=False,
	).exclude(id=item_id)[:3]
	return render(request, 'item/detail.html', context={
		'item': item,
		'related_items': related_items,
	})

@login_required
def new_item(request):
	if request.method == 'POST':
		form = NewItemForm(request.POST, request.FILES)
		
		if form.is_valid():
			item = form.save(commit=False)
			item.created_by = request.user
			item.save()
			return redirect('item:detail', item_id=item.id)
	else:
		form = NewItemForm()

	return render(request, 'item/forms.html', {
		'title': 'Add new item',
		'form': form,
	})

@login_required
def edit_item(request, item_id) :
	item = get_object_or_404(Item, id=item_id, created_by=request.user)
	if request.method == 'POST':
		form = EditItemForm(request.POST, request.FILES, instance=item)
		
		if form.is_valid():
			form.save()
			return redirect('item:detail', item_id=item.id)
	else:
		form = EditItemForm(instance=item)

	return render(request, 'item/forms.html', {
		'title': 'Edit item',
		'form': form,
	})

@login_required
def delete_item(request, item_id):
	item = get_object_or_404(Item, id=item_id, created_by=request.user)
	item.delete()

	return redirect('dashboard:index')
