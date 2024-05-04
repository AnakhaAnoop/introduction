from django.shortcuts import render, redirect
from . models import product, Buyer
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')


def add(request):
    if request.method == 'POST':
        name = request.POST['p_name']
        price = request.POST['p_price']
        product.objects.create(product_name= name, product_price = price)
        
        return redirect('add')
    return render(request,'add_product.html')

    

def buyers(request):
    show = product.objects.all()
    if request.method == 'POST':
        try:
            name = request.POST['name']
            address = request.POST['addr']
            selected = request.POST['select']
            prod = product.objects.get(id = selected)
            
            data = Buyer(name=name,address=address,product=prod)
            data.save()
            return redirect('all')
        except:
            messages.info(request,'Select any products')
            
    context = {'show':show}
    return render(request,'add_buyers.html',context=context)


def buyer_details(request):
    byr = Buyer.objects.all()
    pro = product.objects.all()  
    context = {
        
        'byr': byr,
        'pro': pro
        
        }
    
    return render(request, 'buyer_details.html', context=context)

def prod_details(request):
    show = product.objects.all()
    context = {'show':show}
    return render(request,'prod_details.html',context=context)


def all(request):
    byr = Buyer.objects.all()
    show = product.objects.all()
    
    context = {
        'byr':byr,
        'show':show
    }
    return render(request,'all_details.html',context=context)



