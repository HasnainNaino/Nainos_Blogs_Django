from django.shortcuts import render, get_object_or_404, redirect
from .models import BLog, Comment  
from .form import commentForm

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def list(request):
    posts = BLog.objects.all()
    carousel = BLog.objects.all().order_by('-id')[:4]
    comment = Comment.objects.all()
    return render(request, 'list.html', {'posts': posts, 'carousel': carousel, 'comments':  comment })


def detail(request, pk):
    posts = get_object_or_404(BLog, pk=pk)
    comments = posts.comment_set.all()

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = posts
            comment.save()
            return redirect('detail', pk=posts.pk)
    else:   
        form =  commentForm()

    return render(request, 'detail.html', {'posts': posts,'form':form, 'comments':  comments }) 

def post_like(request, pk):
    post = get_object_or_404(BLog, pk=pk)
    post.likes += 1
    post.save()
    return redirect('detail', pk=pk)

def search(request):
    query = request.GET.get('q', '')  # get the search query
    if query:
        results = BLog.objects.filter(title__icontains=query)
    else:
        results = BLog.objects.none()  # empty queryset if no query

    return render(request, 'search.html', {
        'results': results,
        'query': query
    })