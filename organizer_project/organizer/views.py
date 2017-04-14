from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from organizer.models import Transaction
from organizer.forms import SignUpForm, AddTransactionForm

def index(request):
	
	return render(request, 'organizer/index.html')


@login_required(login_url='/login/')
def home(request):

    transaction_list = Transaction.objects.all().order_by('-id')[:3]

    context = {
        'transaction_list': transaction_list,
    }

    return render(request, 'organizer/home.html', context)

    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'organizer/home.html')
    else:
        form = SignUpForm()
    return render(request, 'organizer/signup.html', {'form': form})


def add_transaction(request):
    if not request.user.is_authenticated():
        return render(request, 'organizer/login.html')
    else:
        form = AddTransactionForm(request.POST or None)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.product = form.cleaned_data.get('product')
            t.price = form.cleaned_data.get('price')
            t.purchase_date = form.cleaned_data.get('purchase_date')
            t.description = form.cleaned_data.get('description')
            t.save()
            return render(request, 'organizer/test.html')

    return render(request, 'organizer/add-transaction.html', {'form': form})
