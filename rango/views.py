from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category, Page

# Input views here.

def index(request):

	#Querying DB for a list of ALL categories currently stored; Order by desc. likes; 
	#Place list in context_dict which passes to the template engine.
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]

	context_dict = {}
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	context_dict = {'categories': category_list, 'pages': page_list} 

	return render(request, 'rango/index.html', context=context_dict)


def about(request):
	context_dict = {'author': 'This tutorial has been put together by Rachelle Deal.'}
	return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
	#Creates a context dict to pass to the template-rendering engine
	context_dict = {}

	try:
	#Can we find a slug w given name? if not, '.get()' raises a DNE exception.
	#.get() either returns a model instance or raises exception
		category = Category.objects.get(slug=category_name_slug)

		#Retrieves all associated pages; 'filter()' returns either list of page objects or empty
		pages = Page.objects.filter(category=category)

		#Adds results list to the template context under name pages
		context_dict['pages'] = pages

		#Adds category object from the DB to the context dict. Used in template to verify cat exists
		context_dict['category'] = category

	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None

	#Renders response and returns to client
	return render(request, 'rango/category.html', context=context_dict)



