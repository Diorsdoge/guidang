from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from luru.models import Dangan,Department,Gdyear
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search_form(request):
    riqi = Gdyear.objects.filter()
    bumen = Department.objects.filter()
    return render(request, 'search_index.html',{'riqi':riqi,'bumen':bumen})

def get_dangan(filter, page):
    dangan_list = Dangan.objects.filter(**filter)
    paginator = Paginator(dangan_list,20)
    try:
        dangan=paginator.page(page)
    except PageNotAnInteger:
        dangan=paginator.page(1)
    except EmptyPage:
        dangan=paginator.page(paginator.num_pages)
    return dangan

def search(request):     
    errors = []
    p = request.GET.get('p','')
    b = request.GET.get('b','')
    q = request.GET.get('q','')
    page = request.GET.get('page', 1)

    if len(q) > 20:
        errors.append('Please enter at most 20 characters.')
        return render(request, 'search_form.html', {'errors': errors})

    filter = {}
    if b and (b != 'buxian'):
        filter['gd_department_id'] = b

    if p and (p != 'buxian'):
        filter['gd_time'] = p

    if q:
        filter['gd_name__icontains'] = q
    dangan = get_dangan(filter=filter, page=page)
    riqi = Gdyear.objects.filter()
    bumen = Department.objects.filter()
    return render(request, 'search_form.html',{'dangan': dangan ,'p':p,'q':q,'b':b,'riqi':riqi,'bumen':bumen})
