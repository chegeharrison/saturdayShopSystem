from django.shortcuts import render,redirect
from django.contrib import messages
from .models import  Product



def home(request):
    return render(request,'index.html')

def add_product(request):
    if request.method == "POST":
        product_name = request.POST.get('p-name')
        product_qtty = request.POST.get('p-qtty')
        product_price = request.POST.get('p-price')
        product_desc = request.POST.get('p-desc')

        data = Product(name=product_name,qtty=product_qtty,
                     price=product_price, desc=product_desc)
        data.save()
        messages.success(request,"Product saved successfully")
        return redirect("add-product-url")

    return render(request,'add-product.html')
def products(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request,'products.html',context)

def products(request):
    all_products =Product.objects.all()
    context = {"products": all_products}
    return render(request,'products.html', context)

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request,"Product deleted successfully")
    return redirect("products-url")

