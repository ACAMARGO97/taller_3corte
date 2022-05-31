from django.shortcuts import render, redirect
from apps.libro.form import LibroForm
from apps.libro.models import Libro

def listLibros(request):
    libros = Libro.objects.all().order_by('-id')
    context = {'libros': libros}
    return render(request, 'libro/listlibro.html',context)

def home(request):
    return render(request, 'base/base.html')

def libroCreate(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libro:listlibros')
    else:
        form = LibroForm()
    return render(request, 'libro/libro_form.html', {'form': form})

def libroUpdate(request, id_libro):
    mant = Libro.objects.get(pk=id_libro)

    if request.method == 'GET':
        form = LibroForm(instance=mant)
    else:
        form = LibroForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('libro:listlibros')
    
    return render(request, 'libro/libro_form.html', {'form': form})

def libroDelete(request, id_libro):
    mant = Libro.objects.get(pk=id_libro)
    if request.method == 'POST':
       mant.delete()
       return redirect('libro:listlibros')
    return render(request, 'libro/libroDelete.html', {'libro': mant})