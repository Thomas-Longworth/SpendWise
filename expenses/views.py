from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home_page.html')   
def add(request):
    return render(request, 'add_expenses.html')   
def update(request):
    return render(request, 'update_expenses.html')
def exp_page(request):
    return render(request, 'expenses_page.html')