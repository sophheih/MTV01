from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseNotFound
from mysite.models import Product
import random
# Create your views here.

def homepage(request):
    return HttpResponse('我的首頁')

def about(request):
    quotes = ['今日事，今日畢',
            '要怎麼收穫，先那麼栽',
            '知識就是力量',
            '一個人的個性就是他的命運']
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())   
def about(request):
    html = '''
    About Myself
    '''
    return HttpResponse(html)
def listing(request):
    products = Product.objects.all().order_by('price')	
    return render(request, 'list.html', locals())


def disp_detail(request, sku):
    try:	
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')

    return render(request, 'disp.html', locals())
