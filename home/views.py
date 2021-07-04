from django.shortcuts import render ,HttpResponse

def home_view(request):
    if request.user.is_authenticated:
        context={ 'isim':' ',
                  }
    else:
        context={
            'isim': 'Misafir',

        }
    return render(request,'home.html',context)
def info_view(request):
    context={
        'info':'SAKARYA ÜNİVERSİTESİ'
    }
    return render(request,'info.html',context)
