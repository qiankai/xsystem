from django.shortcuts import render
from django.http import HttpResponse
import json
from models import Employee

def index(request):
    return render(request, 'employee/index.html')


def test(request):
    return render(request, 'employee/index.html')


def login(request):
    return render(request, 'login.html')


def getlist(request):
    if request.method == "GET":
        draw = int(request.GET.get('draw', -1))
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length'))
        search_regx = request.GET.get('search[regex]')
        search_value = request.GET.get('search[value]')
        print(draw)
        print(start)
        print(length)
        print(search_regx)
        print(search_value)
        if search_value == "":
            emp_list = Employee.objects.all()
            print(1)
        else:
            emp_list = Employee.objects.filter(work_no__contains=search_value)
            print(2)
        print(emp_list)
        if emp_list.count() > 0:
            emp_filter_list = emp_list[start*length:(start+1)*length]
            data = []
            print(emp_filter_list.count())
            if emp_filter_list.count() < length:
                for i in range(0, emp_filter_list.count()):
                    d = {
                        'id': str(emp_filter_list[i].id).replace('-', ','),
                        'real_name': emp_filter_list[i].real_name,
                        'mobile': emp_filter_list[i].mobile,
                        'department': emp_filter_list[i].emp_related_dt.dt_name,
                        'position': emp_filter_list[i].position,
                        'enter_time': emp_filter_list[i].mobile
                    }
                    data.append(d)
            else:
                for i in range(0, length):
                    d = {
                        'id': str(emp_filter_list[i].id).replace('-', ','),
                        'real_name': emp_filter_list[i].real_name,
                        'mobile': emp_filter_list[i].mobile,
                        'department': emp_filter_list[i].emp_related_dt.dt_name,
                        'position': emp_filter_list[i].position,
                        'enter_time': emp_filter_list[i].mobile
                    }
                    data.append(d)
            response_data = {'draw': draw, 'recordsTotal': emp_list.count(), 'recordsFiltered': len(data), 'data': data}
            return HttpResponse(json.dumps(response_data), content_type="application/json")




