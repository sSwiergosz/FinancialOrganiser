from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from organizer.models import Transaction


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class AddTransactionForm(forms.ModelForm):

	class Meta:
		model = Transaction
		fields = ('product', 'price', 'purchase_date', 'description', )