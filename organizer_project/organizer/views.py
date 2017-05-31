from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from decimal import Decimal
import json
from django.core.serializers.json import DjangoJSONEncoder

from datetime import datetime as dt, timedelta
from django.utils import timezone

from organizer.models import Transaction, Profile
from organizer.forms import SignUpForm, AddTransactionForm


def index(request):
	
	return render(request, 'organizer/index.html')

@login_required(login_url='/login/')
def home(request):
    username = request.user

    transaction_list = Transaction.objects.filter(user__username=username).order_by('-id')[:5]
    date = dt.now().date

    p = Profile.objects.get(user=request.user)

    last_7_days = (dt.now().date() - timedelta(days=7))
    cat_app_7 = cat_ent_7 = cat_food_7 = cat_skin_7 = cat_comp_7 = cat_book_7 = cat_oth_7 = 0

    for i in Transaction.objects.filter(user__username=username):
    #money spent within last 7 days        
        if i.purchase_date > last_7_days:
            if i.category == 'Apparel/Accesory':
                cat_app_7 += i.price
            elif i.category == 'Entertainment':
                cat_ent_7 += i.price
            elif i.category == 'Food/Beverage':
                cat_food_7 += i.price
            elif i.category == 'Skin care/Cosmetics':
                cat_skin_7 += i.price
            elif i.category == 'Computer/Mobile':
                cat_comp_7 += i.price
            elif i.category == 'Books/Newspapers':
                cat_book_7 += i.price
            elif i.category == 'Other':
                cat_oth_7 += i.price

    l_7 = [cat_app_7, cat_ent_7, cat_food_7, cat_skin_7, cat_comp_7, cat_book_7, cat_oth_7]

    context = {
        'transaction_list': transaction_list,
        'date': date,
        'weekly': sum(l_7),
        'balance': p.balance,
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
            email = form.cleaned_data['email']
            data = "Hello"
            send_mail('Welcome!', data, 'financizer@gmail.com', [email])
            login(request, user)
            return render(request, 'organizer/home.html')
    else:
        form = SignUpForm()
    return render(request, 'organizer/signup.html', {'form': form})

@login_required(login_url='/login/')
def add_transaction(request):
    if not request.user.is_authenticated():
        return render(request, 'organizer/login.html')
    else:
        if request.method == "POST":
            form = AddTransactionForm(request.POST)
            if form.is_valid():
                t = form.save(commit=False)
                p = Profile.objects.get(user=request.user)
                t.user = p.user
                t.product = form.cleaned_data.get('product')
                t.category = form.cleaned_data.get('category')
                t.price = form.cleaned_data.get('price')
                t.purchase_date = form.cleaned_data.get('purchase_date')
                t.description = form.cleaned_data.get('description')
                t.save()
                p.balance -= t.price
                p.save()
                return HttpResponseRedirect('/home/')
        else:
            form = AddTransactionForm()

    return render(request, 'organizer/add-transaction.html', {'form': form, })

@login_required(login_url='/login/')
def all_transactions(request):

    username = request.user
    transaction_list = Transaction.objects.filter(user__username=username)

    context = {
        'transaction_list': transaction_list,
    }

    return render(request, 'organizer/all_transactions.html', context)

@login_required(login_url='/login/')
def statistics(request):

    username = request.user
    amount_all = amount_monthly = amount_weekly = amount_daily = 0

    cat_app_30 = cat_ent_30 = cat_food_30 = cat_skin_30 = cat_comp_30 = cat_book_30 = cat_oth_30 = 0

    cat_app_24 = cat_ent_24 = cat_food_24 = cat_skin_24 = cat_comp_24 = cat_book_24 = cat_oth_24 = 0

    cat_app_7 = cat_ent_7 = cat_food_7 = cat_skin_7 = cat_comp_7 = cat_book_7 = cat_oth_7 = 0

    cat_app_all = cat_ent_all = cat_food_all = cat_skin_all = cat_comp_all = cat_book_all = cat_oth_all = 0

    last_30_days = (dt.now().date() - timedelta(days=30))
    last_7_days = (dt.now().date() - timedelta(days=7))
    last_24_hours = (dt.now().date() - timedelta(days=1))

    for i in Transaction.objects.filter(user__username=username):

        #money spent from the beginning
        if i.category == 'Apparel/Accesory':
            cat_app_all += i.price
        elif i.category == 'Entertainment':
            cat_ent_all += i.price
        elif i.category == 'Food/Beverage':
            cat_food_all += i.price
        elif i.category == 'Skin care/Cosmetics':
            cat_skin_all += i.price
        elif i.category == 'Computer/Mobile':
            cat_comp_all += i.price
        elif i.category == 'Books/Newspapers':
            cat_book_all += i.price
        elif i.category == 'Other':
            cat_oth_all += i.price

        #money spent within last 30 days
        if i.purchase_date > last_30_days:
            if i.category == 'Apparel/Accesory':
                cat_app_30 += i.price
            elif i.category == 'Entertainment':
                cat_ent_30 += i.price
            elif i.category == 'Food/Beverage':
                cat_food_30 += i.price
            elif i.category == 'Skin care/Cosmetics':
                cat_skin_30 += i.price
            elif i.category == 'Computer/Mobile':
                cat_comp_30 += i.price
            elif i.category == 'Books/Newspapers':
                cat_book_30 += i.price
            elif i.category == 'Other':
                cat_oth_30 += i.price

        #money spent within last 7 days        
        if i.purchase_date > last_7_days:
            if i.category == 'Apparel/Accesory':
                cat_app_7 += i.price
            elif i.category == 'Entertainment':
                cat_ent_7 += i.price
            elif i.category == 'Food/Beverage':
                cat_food_7 += i.price
            elif i.category == 'Skin care/Cosmetics':
                cat_skin_7 += i.price
            elif i.category == 'Computer/Mobile':
                cat_comp_7 += i.price
            elif i.category == 'Books/Newspapers':
                cat_book_7 += i.price
            elif i.category == 'Other':
                cat_oth_7 += i.price
        
        #money spent within last 24 hours
        if i.purchase_date > last_24_hours:
            if i.category == 'Apparel/Accesory':
                cat_app_24 += i.price
            elif i.category == 'Entertainment':
                cat_ent_24 += i.price
            elif i.category == 'Food/Beverage':
                cat_food_24 += i.price
            elif i.category == 'Skin care/Cosmetics':
                cat_skin_24 += i.price
            elif i.category == 'Computer/Mobile':
                cat_comp_24 += i.price
            elif i.category == 'Books/Newspapers':
                cat_book_24 += i.price
            elif i.category == 'Other':
                cat_oth_24 += i.price

    l_all = [cat_app_all, cat_ent_all, cat_food_all, cat_skin_all, cat_comp_all, cat_book_all, cat_oth_all]
    l_30 = [cat_app_30, cat_ent_30, cat_food_30, cat_skin_30, cat_comp_30, cat_book_30, cat_oth_30]
    l_7 = [cat_app_7, cat_ent_7, cat_food_7, cat_skin_7, cat_comp_7, cat_book_7, cat_oth_7]
    l_24 = [cat_app_24, cat_ent_24, cat_food_24, cat_skin_24, cat_comp_24, cat_book_24, cat_oth_24]

    context = {
        'amount_all': sum(l_all),
        'amount_monthly': sum(l_30),
        'amount_weekly': sum(l_7),
        'amount_daily': sum(l_24),
        'cat_app_all': cat_app_all,
        'cat_ent_all': cat_ent_all,
        'cat_food_all': cat_food_all,
        'cat_skin_all': cat_skin_all,
        'cat_comp_all': cat_comp_all,
        'cat_book_all': cat_book_all,
        'cat_oth_all': cat_oth_all,
        'cat_app_30': cat_app_30,
        'cat_ent_30': cat_ent_30,
        'cat_food_30': cat_food_30,
        'cat_skin_30': cat_skin_30,
        'cat_comp_30': cat_comp_30,
        'cat_book_30': cat_book_30,
        'cat_oth_30': cat_oth_30,
        'cat_app_7': cat_app_7,
        'cat_ent_7': cat_ent_7,
        'cat_food_7': cat_food_7,
        'cat_skin_7': cat_skin_7,
        'cat_comp_7': cat_comp_7,
        'cat_book_7': cat_book_7,
        'cat_oth_7': cat_oth_7,
        'cat_app_24': cat_app_24,
        'cat_ent_24': cat_ent_24,
        'cat_food_24': cat_food_24,
        'cat_skin_24': cat_skin_24,
        'cat_comp_24': cat_comp_24,
        'cat_book_24': cat_book_24,
        'cat_oth_24': cat_oth_24,
    }

    return render(request, 'organizer/statistics.html', context)

@login_required(login_url='/login/')
def statistics_ajax(request):

    increase_balance = Decimal(request.POST.get('the_balance'))

    p = Profile.objects.get(user=request.user)
    p.balance += increase_balance
    p.save()

    context = {
        'balance': p.balance
    }

    return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder))
    
