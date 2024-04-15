from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, "shop/index.html", {'courses': courses})

def single_course(request, course_id):
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/course.html', {'course': course})

