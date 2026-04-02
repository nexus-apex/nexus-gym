import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import GymMember, FitnessClass, Trainer


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['gymmember_count'] = GymMember.objects.count()
    ctx['gymmember_monthly'] = GymMember.objects.filter(membership_type='monthly').count()
    ctx['gymmember_quarterly'] = GymMember.objects.filter(membership_type='quarterly').count()
    ctx['gymmember_annual'] = GymMember.objects.filter(membership_type='annual').count()
    ctx['fitnessclass_count'] = FitnessClass.objects.count()
    ctx['fitnessclass_yoga'] = FitnessClass.objects.filter(class_type='yoga').count()
    ctx['fitnessclass_crossfit'] = FitnessClass.objects.filter(class_type='crossfit').count()
    ctx['fitnessclass_zumba'] = FitnessClass.objects.filter(class_type='zumba').count()
    ctx['trainer_count'] = Trainer.objects.count()
    ctx['trainer_active'] = Trainer.objects.filter(status='active').count()
    ctx['trainer_on_leave'] = Trainer.objects.filter(status='on_leave').count()
    ctx['trainer_total_rating'] = Trainer.objects.aggregate(t=Sum('rating'))['t'] or 0
    ctx['recent'] = GymMember.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def gymmember_list(request):
    qs = GymMember.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(membership_type=status_filter)
    return render(request, 'gymmember_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def gymmember_create(request):
    if request.method == 'POST':
        obj = GymMember()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.membership_type = request.POST.get('membership_type', '')
        obj.join_date = request.POST.get('join_date') or None
        obj.expiry_date = request.POST.get('expiry_date') or None
        obj.status = request.POST.get('status', '')
        obj.emergency_contact = request.POST.get('emergency_contact', '')
        obj.save()
        return redirect('/gymmembers/')
    return render(request, 'gymmember_form.html', {'editing': False})


@login_required
def gymmember_edit(request, pk):
    obj = get_object_or_404(GymMember, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.membership_type = request.POST.get('membership_type', '')
        obj.join_date = request.POST.get('join_date') or None
        obj.expiry_date = request.POST.get('expiry_date') or None
        obj.status = request.POST.get('status', '')
        obj.emergency_contact = request.POST.get('emergency_contact', '')
        obj.save()
        return redirect('/gymmembers/')
    return render(request, 'gymmember_form.html', {'record': obj, 'editing': True})


@login_required
def gymmember_delete(request, pk):
    obj = get_object_or_404(GymMember, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/gymmembers/')


@login_required
def fitnessclass_list(request):
    qs = FitnessClass.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(class_type=status_filter)
    return render(request, 'fitnessclass_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def fitnessclass_create(request):
    if request.method == 'POST':
        obj = FitnessClass()
        obj.name = request.POST.get('name', '')
        obj.instructor = request.POST.get('instructor', '')
        obj.class_type = request.POST.get('class_type', '')
        obj.schedule = request.POST.get('schedule', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.enrolled = request.POST.get('enrolled') or 0
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/fitnessclasses/')
    return render(request, 'fitnessclass_form.html', {'editing': False})


@login_required
def fitnessclass_edit(request, pk):
    obj = get_object_or_404(FitnessClass, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.instructor = request.POST.get('instructor', '')
        obj.class_type = request.POST.get('class_type', '')
        obj.schedule = request.POST.get('schedule', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.enrolled = request.POST.get('enrolled') or 0
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/fitnessclasses/')
    return render(request, 'fitnessclass_form.html', {'record': obj, 'editing': True})


@login_required
def fitnessclass_delete(request, pk):
    obj = get_object_or_404(FitnessClass, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/fitnessclasses/')


@login_required
def trainer_list(request):
    qs = Trainer.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'trainer_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def trainer_create(request):
    if request.method == 'POST':
        obj = Trainer()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.specialization = request.POST.get('specialization', '')
        obj.experience_years = request.POST.get('experience_years') or 0
        obj.clients = request.POST.get('clients') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.certification = request.POST.get('certification', '')
        obj.save()
        return redirect('/trainers/')
    return render(request, 'trainer_form.html', {'editing': False})


@login_required
def trainer_edit(request, pk):
    obj = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.specialization = request.POST.get('specialization', '')
        obj.experience_years = request.POST.get('experience_years') or 0
        obj.clients = request.POST.get('clients') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.certification = request.POST.get('certification', '')
        obj.save()
        return redirect('/trainers/')
    return render(request, 'trainer_form.html', {'record': obj, 'editing': True})


@login_required
def trainer_delete(request, pk):
    obj = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/trainers/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['gymmember_count'] = GymMember.objects.count()
    data['fitnessclass_count'] = FitnessClass.objects.count()
    data['trainer_count'] = Trainer.objects.count()
    return JsonResponse(data)
