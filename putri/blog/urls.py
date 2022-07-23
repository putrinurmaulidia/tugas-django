from django.shortcurts import render

# Create your views here.

def index(request):
    context ={
        'judul':'blog'
    }
    return render(request,'blog/index.html',context)