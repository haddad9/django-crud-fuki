from django.shortcuts import render,redirect
from .models import crud

# Create method
def create(request):
    if request.method == "POST":
        matkul = request.POST['matkul']

        dosen = request.POST['dosen']
        jumlah_sks = request.POST['jumlah_sks']
        if 'deskripsi' in request.POST:
            deskripsi = request.POST['deskripsi']
        else:
            deskripsi = False



        id = None
        obj = crud(id, matkul, dosen, jumlah_sks, deskripsi)
        obj.save()
        return redirect('/')
   
# Read method   
def read(request):
    try:
        obj = crud.objects.all()
    except crud.DoesNotExist:
        obj = None
    return render(request,'index.html',{'key':obj})

# Update method
def update(request,id):
    if request.method == "POST":
        matkul = request.POST['matkul']
        
        dosen = request.POST['dosen']
        jumlah_sks = request.POST['jumlah_sks']
        deskripsi = request.POST['deskripsi']


        obj1 = crud.objects.get(id=id)
        obj1.matkul = matkul
        obj1.dosen = dosen
        obj1.jumlah_sks = jumlah_sks
        obj1.deskripsi = deskripsi


        obj1.save()
        return redirect('/')
    else:
        try:
            obj = crud.objects.get(id=id)
        except crud.DoesNotExist:
            obj = None

        return render(request,'edit.html',{'key':obj})

# Delete method
def delete(request,id):
    try:
        obj = crud.objects.get(id=id)
    except crud.DoesNotExist:
        obj = None
    
    obj.delete()
    return redirect('/')
