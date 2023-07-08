from django.shortcuts import render
from django.http import HttpResponse
import json

def emp_data_view(request):
    emp_data= {
        'eno':100,
        'ename': 'rakhi',
        'esal': 1000,
        'eaddr': 'Surat',
    }
    resp = f"<h1>employee number{emp_data['eno']},<br>employee name:{emp_data['ename']},<br>employee salary:{emp_data['esal']},<br>employee adress:{emp_data['eaddr']}<h1>"

    return HttpResponse(resp)

def emp_data_jsonview(request):
    emp_data= {
        'eno':100,
        'ename': 'rakhi',
        'esal': 1000,
        'eaddr': 'Surat',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type = 'application/json')