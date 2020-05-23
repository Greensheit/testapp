from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Customer, Data
from django.core.files.storage import FileSystemStorage
import csv


def csv_upload(request):
    status = 200
    st = 'OK'
    if request.method == 'POST':
        try:
            FILE = request.FILES['csv_file']
            fs = FileSystemStorage()
            fs.save(FILE.name, FILE)
            with open('media/{}'.format(str(FILE.name)), encoding='utf-8') as file:
                csv_read_and_save(file)
        except:
            status = 500
            st = 'Error'
    return render(request, 'Test.html', status=status, context={'status': st})


def csv_read_and_save(file):
    reader = csv.DictReader(file, delimiter=',')
    for data in reader:
        new_customer = Customer(name=data['customer'])
        new_customer.save()
        new_data = Data(customer=new_customer, item=data['item'], date=data['date'], total=data['total'],
                        quantity=data['quantity'])
        new_data.save()


def get_data(request):
    data = Data.objects.reverse().order_by('total')[:5]
    return render(request, 'TEST_2.html', context={'response': data})
