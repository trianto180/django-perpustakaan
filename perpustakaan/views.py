from django.shortcuts import render

def buku(request):
    judul = ["Belajar Django", "Belejar pthon", "Belajar bootstrap"]
    konteks = {
        'title': judul
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')
