from django.shortcuts import render, redirect
from django.http import HttpRequest
from . forms import IndustryTypeCreationForm, CompanyDetailsCreationForm
from . models import IndustryType, CompanyDetails


def industry_type_list_view(request: HttpRequest):
    form = IndustryTypeCreationForm()

    if request.method == 'POST':
        form = IndustryTypeCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('search-show')

    context = {
        'form': form,
    }

    return render(request, 'industry_type_form.html', context)


def create_company_detail_view(request: HttpRequest):
    form = CompanyDetailsCreationForm()
    
    if request.method == 'POST':
        form = CompanyDetailsCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('search-show')

    context = {
        'form': form,
    }

    return render(request, 'company_details_form.html', context)


def display(request: HttpRequest):
    industry_type = IndustryType.objects.all()
    companies = CompanyDetails.objects.all()

    context = {
        'industry_type': industry_type,
        'companies': companies,
    }

    return render(request, 'display.html', context)


def search_show_view(request: HttpRequest):
    q = ''
    if request.GET.get('q') is not None:
        q = request.GET.get('q')

    print(q)

    companies = CompanyDetails.objects.filter(industry_type__industry_type__startswith=q)

    context = {
        'companies': companies,
    }

    return render(request, 'search_show.html', context)