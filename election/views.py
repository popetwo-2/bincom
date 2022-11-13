import datetime
from django.urls import reverse
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import PollingUnit, AnnouncedPuResults, Lga
from django.contrib import messages
from .forms import UploadResultForm
import random
from .utils import get_ip
from django.core.paginator import Paginator


# Create your views here.

def all_polling_units(request):  # index page
    units = PollingUnit.objects.all().order_by('polling_unit_name').exclude(
        polling_unit_name='')  # exclude polling units with empty values
    paginator = Paginator(units, 12)
    page_number = request.GET.get('page')
    units = paginator.get_page(page_number)
    local_govts = Lga.objects.all()
    context = {
        'units': units,
        'local_govts': local_govts
    }
    return render(request, 'polling_units.html', context)


def get_result_polling_unit(request, uniqueid):
    unit = PollingUnit.objects.get(uniqueid=uniqueid)
    lga = Lga.objects.get(lga_id=unit.lga_id)
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit.uniqueid)
    total = 0
    for x in results:
        total += x.party_score

    context = {
        'results': results,
        'total': total,
        'lga': lga,
        'unit': unit

    }
    return render(request, 'results.html', context)


def total_result_per_lga(request):
    if request.method == 'POST':
        local_govts = Lga.objects.all()
        uniqueid = request.POST['lga']
        lga = Lga.objects.get(uniqueid=uniqueid)
        total = 0
        if uniqueid:
            units = PollingUnit.objects.filter(lga_id=lga.lga_id)
            print(units.count())
            for unit in units:
                #   lga = Lga.objects.get(uniqueid=unit.lga_id)
                totals = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit.uniqueid)
                for x in totals:
                    total += x.party_score
                context = {
                    'total': total,
                    'local_govts': local_govts,
                    'lga': lga
                }

                return render(request, 'find.html', context)
    else:
        local_govts = Lga.objects.all()
    context = {
        'local_govts': local_govts,
    }
    return render(request, 'find.html', context)


def upload_results(request):
    if request.method == 'POST':
        form = UploadResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.user_ip_address = request.get_host()
            result.date_entered = datetime.datetime.now()
            result.save()
            print(result.user_ip_address)
            #   messages.success(request, 'successful.')
            return redirect('all_results')
    else:
        form = UploadResultForm()
    context = {
        'form': form,
    }
    return render(request, 'upload.html', context)


def results(request):
    res = AnnouncedPuResults.objects.all().order_by('date_entered')
    paginator = Paginator(res, 10)
    page_number = request.GET.get('page')
    res = paginator.get_page(page_number)
    context = {
        'res': res,
    }
    return render(request, 'all_results.html', context)
