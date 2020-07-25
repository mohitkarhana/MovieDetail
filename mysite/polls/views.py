from django.shortcuts import render

from .forms import MovieForm
from .models import movie_data
from django.shortcuts import render, get_object_or_404


def index(request):
    context = {}
    form = MovieForm(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)


def save_data(request):
    if  request.method =='POST':
        post=movie_data()
        post.movie_name=request.POST.get('movie_name')
        post.movie_poster=request.POST.get('movie_poster')
        post.movie_description=request.POST.get('movie_description')
        post.movie_created_date = request.POST.get('movie_created_date')
        post.movie_release_date = request.POST.get('movie_release_date')
        post.save()
        return render(request,'home.html')
    else:
        return render(request,'home.html')
def get_data(request):
    movie_name = request.GET.get('movie_name')
    context={}
    data1= get_object_or_404(movie_data, movie_name=movie_name)
    context["data"] = get_object_or_404(movie_data, movie_name=movie_name)
  
    if data1.movie_name==movie_name:

        return render(request,'getdata.html',context)

    else:
        p='movie name does not exist'
        return render(request,'getdat.html',p)