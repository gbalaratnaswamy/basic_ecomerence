from django.shortcuts import render, redirect
from product.models import Product
from .forms import ProductForm


# Create your views here.
def product_view(request, p_id):
    temp = Product.objects.get(pk=p_id)
    print(temp.image)
    return render(request, "product_template.html",
                  {"title": temp.title, "description": temp.description, "pk": temp.id, "image": temp.image,
                   "price": temp.price, "table": temp.table, "special_model": temp.special_model})


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect(f"http://127.0.0.1:8000/test/{form.id}")
    return render(request, "create_product.html", {"form": form})
