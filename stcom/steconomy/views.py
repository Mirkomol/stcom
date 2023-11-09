import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense




def index(request):

    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))

    #logic to calc 365 days

    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_data = data.aggregate(Sum('amount'))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_data = data.aggregate(Sum('amount'))


    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_data = data.aggregate(Sum('amount'))

    daily_sum = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    categorical_sum = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))

    expense_form = ExpenseForm()

    return render(request, 'steconomy/index.html', {'expense_form':expense_form, 'expenses':expenses,
                                                    'total_expenses':total_expenses,
                                                    'yearly_data':yearly_data,
                                                    'monthly_data':monthly_data,
                                                    'weekly_data':weekly_data,
                                                    'daily_sum':daily_sum,
                                                    'categorical_sum':categorical_sum})



def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)

    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('steconomy')
    return render(request, 'steconomy/edit.html',{'expense_form':expense_form})




def delete(request, id):
    if request.method == 'POST' and 'ecodelete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('steconomy')