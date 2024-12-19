from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# หน้าแรก
def home(request):
    return render(request, 'homepage.html')

# หน้าลงทะเบียน
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลลงในฐานข้อมูล
            messages.success(request, 'Registration successful! Please login.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
