from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from listing.forms import ProductForm, CustomerForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

#def index(request):
#    return HttpResponse("views setup done")

def register(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		customer_form = CustomerForm(data=request.POST)

		if customer_form.is_valid():
			customer = customer_form.save()
			customer.set_password(customer.password)
			customer.save()

			registered = True
		else:
			print customer_form.errors

	else:
		customer_form = CustomerForm()

	return render_to_response(
		'listing/register.html',
		{'customer_form': customer_form, 'registered': registered}, context)

def add_product(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ProductForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors

	else:
		form = ProductForm()

	return render_to_response('listing/add_product.html', {'form': form}, context)

def customer_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/listing/')
			else:
				return HttpResponse("Your Listing account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render_to_response('listing/login.html', {}, context)

@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text. Chill out!")

@login_required
def customer_logout(request):
	logout(request)
	return HttpResponseRedirect('/listing/')