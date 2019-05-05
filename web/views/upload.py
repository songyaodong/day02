from django.shortcuts import render, HttpResponse, redirect
import os


def upload(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('fafafa')
        f = open(os.path.join('upload', file_obj.name), 'wb')
        for line in file_obj.chunks():
            f.write(line)
        f.close()
    else:
        return render(request, 'upload.html')

    return HttpResponse('上传成功')
