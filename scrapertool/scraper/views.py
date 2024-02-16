from django.shortcuts import render
from celery.result import AsyncResult
from scraper.tasks import fetch_records

def index(request):
    result = fetch_records.delay()
    return render(request, "scraper/home.html", {'result':result})

def check_result(request, task_id):
    
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    return render(request, 'scraper/result.html', {'result':result})