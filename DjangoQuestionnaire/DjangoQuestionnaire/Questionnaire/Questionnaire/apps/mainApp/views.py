from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, CreateNewAppointment, DetailAppointment
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Appointment, Doctor, Medical, Orders
from django.contrib import messages


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Невірний логін користувача')
    context = {}
    return render(request, 'login.html', context)


def regist(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def newApointment(request):
    form = CreateNewAppointment
    if request.method == "POST":
        form = CreateNewAppointment(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointments = Appointment.objects.all()
            finded = False
            for ap in appointments:
                if ap.date == appointment.date:
                    if ap.time == appointment.time:
                        finded = True
            if not finded:
                appointment.patietn = request.user
                print(appointment.patietn)
                appointment.symptoms = ''
                appointment.diagnosys = ''
                appointment.recomendations = ''
                print(appointment.id)
                appointment.save()
                return redirect('login')
            else:
                context = {'form': form}
                messages.info(request, 'Цей час вже зайнятий. Оберіть інший час.')
                return render(request, 'addAppointment.html', context)
    context = {'form': form}
    return render(request, 'addAppointment.html', context)


def delete_appointment(request, id):
    Appointment.objects.filter(id=id).delete()
    return redirect('index')

def logoutUser(request):
    logout(request)
    return redirect('login')

def find(request):
    name = request.POST.get('patient_name').split(' ')
    if name and len(name) > 1:
        first_name = name[0]
        last_name = name[1]
        print(first_name)
        appointments = Appointment.objects.filter(patietn__first_name = first_name, patietn__last_name = last_name)
        print(appointments)
        return render(request, 'find.html', {'appointments': appointments})
    else:
        return redirect('index')


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            appointments = Appointment.objects.all()
            return render(request, 'index.html', {'appointments': appointments})

        if request.user.role == 1:
            doctor = Doctor.objects.filter(user=request.user)
            if doctor is not None and len(doctor) > 0:
                appointments = Appointment.objects.filter(doctor=doctor[0])
                return render(request, 'index.html', {'appointments': appointments})
            else:
                return render(request, 'index.html', None)

        else:
            appointments = Appointment.objects.filter(patietn=request.user)
            return render(request, 'index.html', {'appointments': appointments})

    else:
        return render(request, 'main.html', None)


def about(request):
    return render(request, 'about.html', None)


def appointment_info(request):
    return render(request, 'appointment_info.html', None)


def lab_info(request):
    return render(request, 'lab_info.html', None)


def rules(request):
    return render(request, 'rules.html', None)


def advantages(request):
    return render(request, 'advantages.html', None)


def faq(request):
    return render(request, 'faq.html', None)


def news(request):
    return render(request, 'news.html', None)


def contacts(request):
    return render(request, 'contacts.html', None)


def detail_appointment(request, id):
    form = DetailAppointment
    if request.method == "POST":
        form = DetailAppointment(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            appointment = Appointment.objects.filter(id=id)[0]
            appointment.symptoms = data.symptoms
            appointment.diagnosys = data.diagnosys
            appointment.recomendations = data.recomendations
            appointment.save()
            return redirect('index')
    appoint = Appointment.objects.filter(id=id)
    context = {'form': form, 'appointment': appoint}
    return render(request, 'detailAppointment.html', context)


def medical(request):
    medicals = Medical.objects.all()
    context = {'medicals': medicals}
    return render(request, 'medicals.html', context)


def order(request, name):
    medical = Medical.objects.filter(name=name)[0]
    order = Orders(user=request.user, medical=medical)
    order.save()
    return redirect('medical')


def statistics(request):
    diagnoses = Appointment.objects.order_by().values('diagnosys').distinct()
    stats = []
    for diagnosys_str in diagnoses:
        if diagnosys_str['diagnosys'] != '':
            stats.append(diagnosys_str['diagnosys'] + ' — ' + str(
                len(Appointment.objects.filter(diagnosys=diagnosys_str['diagnosys']))))
    context = {'statistics': stats}
    return render(request, 'statistics.html', context)
