from django.shortcuts import render

# Create your views here.
def tao_cookie(request):
    response = render(request,'first_app/tao_cookie.html')
    response.set_cookie('ho_ten','Nguyen Van A')
    return response
def doc_cookie(request):
   ho_ten = request.COOKIES.get('ho_ten')
   return render(request,'first_app/doc_cookie.html',{'ho_ten':ho_ten})

def xoa_cookie(request):
    response = render(request,'first_app/delete_cookie.html')
    response.delete_cookie('ho_ten')
    return response