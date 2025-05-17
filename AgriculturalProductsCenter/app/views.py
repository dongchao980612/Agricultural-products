from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from app.form import CustomUserCreationForm
from app.models import Product, UserProfile


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('products')
        return render(request, 'app/login.html', {'form': form, 'error': '用户名或密码错误'})
    form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def user_profile(request):
    # 获取或创建用户资料
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    # 将用户和用户资料对象传递给模板
    return render(request, 'app/profile-easy.html', {'user': request.user, 'profile': profile})

def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'app/products.html',{'products': products})


def  product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # product = Product.objects.filter(id=product_id)[0]
    return render(request, 'app/product_detail.html', {'product':product})
