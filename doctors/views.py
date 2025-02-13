from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def create_booking(request):
    if request.method=='POST':
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'booking.html', {'form':form})
    else:
        form= BookingForm()
    return render(request, 'booking.html', {'form':form})

def viewbook(request):
    data=Booking.objects.all()
    return render(request, 'viewbooking.html' , {'data':data})

def updatebook(request,id):
    data=Booking.objects.get(pk=id)
    if request.method=='POST':
        form=BookingForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('viewbook')
    else:
        form=BookingForm(instance=data)
    return render(request, 'update.html', {'form':form})

def deletebook(request,id):
    data=Booking.objects.get(pk=id)
    data.delete()
    return redirect('viewbook')

def dep(request):
    return render(request,'department.html')

def services(request):
    return render(request,'services.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')



