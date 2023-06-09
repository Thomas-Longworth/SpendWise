from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Budget
from .forms import ExpenseForm, BudgetForm
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home_page.html')


def exp_page(request):
    user_budget = Budget.objects.values_list('max_budget', flat=True)
    budget_total = sum(user_budget)
    numbers1 = Expense.objects.values_list('number', flat=True)
    total = sum(numbers1)
    last_object = Budget.objects.order_by('-id').first()
    leftover = budget_total-total
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses,
        'total': total,
        'budget_total': budget_total,
        'leftover': leftover,
        'last_object': last_object,
        'user': request.user
    }
    context = {
        'expenses': expenses,
        'total': total,
        'budget_total': budget_total,
        'leftover': leftover,
        'last_object': last_object,
    }
    return render(request, 'expenses_page.html', context)


def add(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            messages.success(request, f'You have added a new expense')
            form.save()
            return redirect('exp_page')
    form = ExpenseForm()
    context = {
        'form': form
    }
    return render(request, 'add_expenses.html', context)


def update(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            messages.success(request, f'You have updated a new expense')
            form.save()
            return redirect('exp_page')
    form = ExpenseForm(instance=expense)
    context = {
        'form': form
    }
    return render(request, 'update_expenses.html', context)


def delete(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    messages.success(request, f'You have successfully  deleted a new expense')
    return redirect('exp_page')


def add_budget(request):
    Budget.objects.all().delete()
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have added your new budget')
            return redirect('exp_page')
    form = BudgetForm()
    context = {
        'form': form,
    }
    return render(request, 'budget_page.html', context)
