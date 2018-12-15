from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'second_app/index.html')

def danh_sach(request):
    return render(request,'second_app/danh_sach.html')

def chi_tiet(request):
    return render(request,'second_app/chi_tiet.html')

def tin_tuc(request):
    return render(request,'second_app/tin_tuc.html')