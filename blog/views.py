from django.shortcuts import render, redirect, reverse
from .models import Post, Category
from django.db.models import Q
from .forms import RegisterForm

def index(request):
    posts = Post.objects.filter(publish = 1).order_by('-views')[:3]
    sliders = Post.objects.filter(publish = 1).filter(views__gte = 10).order_by('-views')[:6]
    categories = Category.objects.all()[:12]
    context = {'news': posts,'sliders': sliders, 'categories': categories}
    return render(request, 'blog/index.html', context)

def news(request):
    posts = Post.objects.all()
    return render(request, 'blog/news.html', {'posts': posts})

def search_function(request):
    query = request.GET.get('search_input')
    posts = Post.objects.filter(Q(title__icontains = query))
    return render(request, 'blog/search.html', {"query": query, 'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__exact = slug)
    post.views += 1
    post.save()
    return render(request, 'blog/post_detail.html', {"post": post})

def category_detail(request, slug):
    category = Category.objects.get(slug__exact = slug)
    return render(request, 'blog/category_detail.html', {'category': category})

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'blog/register.html', {'form': form})
    return redirect('index')

def comment(request, slug):
    post = Post.objects.get(slug__exact = slug)
    if request.method == 'POST':
        post.comment_set.create(user = request.user, text = request.POST.get('text'))
        return redirect(reverse('post_detail_url', kwargs={'slug': post.slug}))
    return redirect(reverse('post_detail_url', kwargs={'slug': post.slug}))

def sort(request):
    query = request.GET.get('sort')
    posts = Post.objects.order_by(query)
    return render(request, 'blog/sort.html', {'posts': posts, 'query': query})