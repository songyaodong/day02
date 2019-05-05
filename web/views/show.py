from django.shortcuts import render, HttpResponse, redirect


def showStu(request):
    if request.method == 'GET':
        data = Student.objects.all()
        result = {
            'result': data
        }
        return render(request, 'show.html', result)
