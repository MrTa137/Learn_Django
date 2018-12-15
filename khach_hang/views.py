from django.shortcuts import render
from khach_hang.models import *
from django.http import request
# Create your views here.
def dang_nhap(request):
    err=''
    if request.method=="POST":
        _ten=request.POST.get('ten_dang_nhap')
        _mat_khau=request.POST.get('mat_khau')
        kh = khach_hang.M_Khach_hang.objects.filter(ten_dang_nhap=_ten, mat_khau=_mat_khau)
        if kh.count()>0:
            request.session['username']=kh[0].ho_ten
            err='Da luu khach hang vao session'
        else:
            err='Dang nhap khong thanh cong'
    return render(request,'khach_hang/dang_nhap.html',{'err':err})
def dang_xuat(request):
    try:
        if request.session.has_key('username'):
            del request.session['usernamme']
    except:
        pass
    return redirect('dang_nhap')

def dang_ky(request):
    registered = False
    if request.method = 'POST'
    form_user = forms.FormDangKy(request.POST, KhachHang)
    ###################################
    hasher = PBKDF2PasswordHasher()
    ###################################
    if form_user.is_valid() and form_user.cleaned_data['mat_khau'] == form_user.cleaned_data['comfirm']:
        request.POST._mutable = True
        post = form_user.save(commit = False)
        post.ho_ten = form_user.cleaned_data['ho_ten']
        post.ten_dang_nhap = form_user.cleaned-data['ten_dang_nhap']
        ###################################
        post.mat_khau = hasher.encode(form_user.cleaned_data['mat_khau'],'123')
        post.email = form_user.cleaned_data['email']
        post.phone = form_user.cleaned-data['phone']
        post.email = form_user.cleaned_data['email']
        post.dia_chi = form_user.cleaned_data['dia_chi']
        post.save()
        print("Da ghi user vao CSDL")
    elif form_user.cleaned_data['mat_khau'] != form_user.cleaned_data['confirm']:
        form_user.add_error('confirm','The password do not match')
        print('Password and confirm password are not the same')
    

    else:
        form_user = form.FormDangKy()
    return render(request,"first_app/registration.html",{'user_form':form_user, 'registered':registered})