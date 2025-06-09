from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
	path('new/', views.new_item, name='new_item'),
	path('<int:item_id>/', views.detail, name='detail'),
	path('<int:item_id>/delete/', views.delete_item, name='delete_item'),
	path('<int:item_id>/edit/', views.edit_item, name='edit_item'),
]