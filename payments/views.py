from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from cart.models import CartItem
from orders.models import OrderedItem
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from orders.forms import OrderForm


# Create your views here.
def start_payment(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    cart = CartItem.objects.get(user=request.user)
    all_products = cart.products.all()
    if len(all_products) == 0:
        return HttpResponse("No items in your cart")
    total_cost = 0
    order_items = []
    for product in cart.products.all():
        no_of_items = cart.items[f"{product.id}"]
        subtotal = no_of_items * product.price
        order = OrderedItem(user=request.user, product=product, no_of_items=no_of_items,
                            cost=subtotal)
        order.save()
        order_items.append(order.id)
        total_cost += subtotal
    request.session['orders'] = order_items
    request.session['total_cost'] = str(total_cost)

    form = OrderForm(request.POST or None)

    return render(request, "payment.html", {"cart": cart, "form": form})


def checkout(request):
    if request.method == "GET":
        return HttpResponse('Request not valid')
    if not request.user.is_authenticated:
        return redirect("/login")
    try:
        order_items = request.session['orders']
        total_cost = request.session['total_cost']
        del request.session['orders']
        del request.session['total_cost']
    except KeyError:
        return HttpResponse("error")
    payment_method = request.POST['payment_method']
    if len(order_items) == 0:
        return HttpResponse('No items in your cart')
    for order_id in order_items:
        order = OrderedItem.objects.get(id=order_id)
        order.is_payment_complete = True
        order.payment_method = payment_method
        order.save()
    if request.user.email is not None:
        cart = CartItem.objects.get(user=request.user)
        user = request.user
        c = {'username': request.user.username, "cart": cart, "total_cost": total_cost}
        html_content = render_to_string('emails/order_complete.html', c)
        text_content = strip_tags(html_content)
        cart.items = {}
        cart.products.clear()
        cart.save()
        email = EmailMultiAlternatives('Purchase complete', text_content)
        email.attach_alternative(html_content, "text/html")
        email.to = [user.email]
        email.send()
    return HttpResponse("success")
