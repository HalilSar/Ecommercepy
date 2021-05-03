from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Product,Category,Images,Comment,CommentForm
from home.models import Setting
from django.db.models import Q
from .form import SearchForm
def index(request):
    # product_list = Product.objects.get_queryset().order_by('id')
    products= Product.objects.all()
    categories =Category.objects.all()
    settings = Setting.objects.get(pk=1)
    # query = request.GET.get('q')
    # if query:
    #     product_list = product_list.filter(
    #         Q(title__icontains=query) |
    #         Q(description__icontains=query) 
    #     ).distinct()
    
    # paginator = Paginator(product_list, 3)
    # page_number = request.GET.get('page')
    # products = paginator.get_page(page_number)
    context = {
        'products': products,
        'categories' : categories,
        'settings': settings,
    }
    return render(request, 'product/search.html',context)
    

def GetById(request,product_id,slug):
    product = get_object_or_404(Product, pk = product_id)
    settings= Setting.objects.get(pk=1)
    images = Images.objects.filter(product_id=product_id)                                                                                                                                  
    relatedproducts = Product.objects.select_related('category')
    comments = Comment.objects.all()# Trur olmayanları getirmemeiz gerekir,status='True'
    context = {
        'product':product,      
        'settings':settings,
        'relatedproducts':relatedproducts,
        'images': images,
        'comments' : comments
    }
    return render(request, 'product/detail.html', context)


def GetByCategoryId(request,category_id,slug):
    
    products =Product.objects.filter(category_id=category_id)
    categories =Category.objects.all()
    categorydata = Category.objects.get(pk=category_id)
    settings = Setting.objects.filter(pk=1)
    # paginator = Paginator(product_list, 3)
    # page_number = request.GET.get('page')
    # products = paginator.get_page(page_number)
    context = {
        'products': products,
        'categories' : categories,
        'categorydata':categorydata,
        'settings': settings,
    }
    return render(request, 'product/category.html', context)

# @login_required(login_url='/login') # Login Kontrolü
def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Comment()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.ip = request.META.get('REMOTE_ADDR')
         data.product_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
        #  messages.success(request, "Mesajın gönderildi")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            category = Category.objects.all()
            products=Product.objects.filter(title__icontains=query)
            context = {'products': products, 'query':query,
                        'category': category }
            return render(request, 'product/search.html', context)
    return HttpResponseRedirect('/')
    