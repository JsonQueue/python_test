from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
# Create your views here.

def index(request):
    print(_('你好'))
    return render(request,'index.html')