from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this is our assumption data '
    d={'assumption':data,'sunil':'age is 23','job':'i want job as soon as possible'}
    return render(request,'data_render.html',d)
