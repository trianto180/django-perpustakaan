from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages

def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbarui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form' : form,
            'buku' : buku,
        }
    return render(request, template, konteks)

def buku(request):
    books = Buku.objects.all()
    #menampilkan buku jumla 32
    # books = Buku.objects.filter(jumlah=32)

    #menampilkan buku sesuai kategori, [:1/2] untuk melimit jumlah yang ditampilkan
    # books = Buku.objects.filter(kelompok_id__nama='produktif')[:1]

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