from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku

def buku(request):
    # books = Buku.objects.all()
    #menampilkan buku jumla 32
    books = Buku.objects.filter(jumlah=32)

    #menampilkan buku sesuai kategori, [:1/2] untuk melimit jumlah yang ditampilkan
    books = Buku.objects.filter(kelompok_id__nama='produktif')[:1]

    konteks = {
        'books': books,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')

def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data berhasil disimpan"
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    else:
        form = FormBuku()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-buku.html', konteks)