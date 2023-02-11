import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()
from rango.models import Category, Page

def populate():

	# 1) lists of dictionaries containing pages to add to each category
	# 2) dictionary of dictionaries for the categories.

	python_pages = [
		{'title': 'Official Python Tutorial', 
		'url': 'http://docs.python.org/3/tutorial/'},
		{'title': 'How to Think like a Computer Scientist', 
		'url': 'http://www.greenteapress.com/thinkpython/'},
		{'title': 'Learn Python in 10 Minutes', 
		'url': 'http://www.korokithakis.net/tutorials/python'}	]

	django_pages = [
		{'title': 'Official Django Tutorial',
		'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
		{'title': 'Django Rocks',
		'url': 'http://www.djangorocks.com/'},
		{'title': 'How to Tango with Django',
		'url': 'http://www.tangowithdjango.com/'}	]

	other_pages = [
		{'title': 'Bottle',
		'url': 'http://bottlepy.org/docs/dec/'},
		{'title': 'Flask',
		'url': 'http://flask.pocoo.org'}	]

	cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
			'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
			'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}}


	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data['views'], cat_data['likes']) 
		for p in cat_data['pages']:
			add_page(c, p['title'], p['url'])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print(f'- {c}: {p}')

#CHAPTER 5 TEST ISSUE - SHOWING VIEWS AND LIKES prior to fixing ln42, now shows 0
#1 error like this, but 3 errors (views/likes correct tho) if 42 reversed

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url = url
	p.views = views
	p.save()
	return p

def add_cat(name, views=0, likes=0):
	c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
	c.name = name
	c.views = views
	c.likes = likes
	c.save()
	return c

if __name__ == '__main__':
	print('Starting Rango population script...')
	populate()
