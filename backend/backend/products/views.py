from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .scrap.olx import Olx, OlxOferta
from .scrap.aliexpress import Aliexpress
from .scrap.main import from_olx_get_aliexpress

from .models import Product, Photo

def products(request):
    # If request type is post
    if request.method == "POST":
        # Get the form data
        product_name = request.POST.get("product_name")
        search_count = request.POST.get("search_count")

        url = "https://www.olx.ro/oferte/q-" + product_name + "/?search[filter_float_price%3Ato]=1000"

        # Scrap new products
        products = Olx.get_oferte(url, int(search_count))

        print(products)

        # Save the products
        for product in products:
            p1 = Product(
                name=product.titlu,
                description="",
                price=product.pret,
                url=product.url,
                view_count=0,
            )
            p1.save()

            # # try:
            # p_ali = from_olx_get_aliexpress(url)
            # p2 = Product(
            #     name=p_ali.titlu,
            #     description="",
            #     price=p_ali.pret,
            #     url=p_ali.url,
            #     view_count=0,
            # )
            # p2.save()

            # p1.similar_products.add(p2)
            
            # except:
            #     print("Cautarea de produse similare pe Aliexpress, a dat eroare.")


    latest_product_list = Product.objects.order_by("-id")[:10]

    context = {
        "latest_product_list": latest_product_list,
    }

    return render(request, "products/index.html", context)

@login_required
def detail(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        try:
            p = OlxOferta(url=product.url)
            p.complete_fields()
            product.name = p.titlu
            product.store = "Olx"

            # photos
            for photo_url in p.photo_urls:
                photo = Photo(url=photo_url)
                photo.save()
                product.photos.add(photo)

            product.status = "complete"
        except:
            product.status = "error"
        product.save()

    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {"product": product, "photos": product.photos.all()})

url_aliseeks = "https://www.aliseeks.com/search/image?aref=ff-sbi&imageurl="

def similar(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        try:
            photo_url = product.photos.all()[0].url
            oferta_aliexpress = Aliexpress.get_oferte(url_aliseeks + photo_url, limit=1)[0]

            p_ali = Product(
                name="",
                url=oferta_aliexpress.url,
                view_count=0,
                store = "Aliexpress",
            )
            p_ali.save()
            product.similar_products.add(p_ali)
        
        except:
            print("Cautarea de produse similare pe Aliexpress, a dat eroare.")

    return render(request, "products/similar.html", {"product": product, "similar_products": product.similar_products.all()})

