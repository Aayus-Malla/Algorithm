from store.models import  Cart, Product
from django.db.models import Q

# Create your views here.

def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'store/cart.html', {'cart': cart})

def add_to_cart_with_options(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = request.session.get('cart', {})
    
    # Add product to cart (increase quantity if it already exists)
    if slug in cart:
        cart[slug]['quantity'] += 1
    else:
        cart[slug] = {'title': product.title, 'price': str(product.price), 'quantity': 1, 'image': product.product_image.url}
    
    request.session['cart'] = cart
    return redirect('cart')  # Redirect to cart page after adding


def product_related_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
        Q(title__icontains=query) | Q(short_description__icontains=query) | Q(detail_description__icontains=query)
    )
    context = {'products': products, 'query': query}
    return render(request, 'store/search_results.html', context)

