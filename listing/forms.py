from django import forms
from listing.models import Customer, Product
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
	name=forms.CharField(max_length=100, help_text = 'Please enter your name')
	email=forms.EmailField()
	password=forms.CharField(widget = forms.PasswordInput())

	class Meta:
		model = Customer
		fields = ('customername', 'email', 'password')

class ProductForm(forms.ModelForm):
	title=forms.CharField(max_length=500)
	image=forms.ImageField(upload_to= 'media/', widget = forms.ClearableFileInput)
	description=forms.CharField(max_length=10000, widget = forms.Textarea)
	price=forms.FloatField()
	time=forms.DateTimeField('date last edited', widget = forms.HiddenInput())

	owner=forms.ForeignKey(Customer,related_name="owner of Product", widget = forms.HiddenInput())

	class Meta:
		model = Product