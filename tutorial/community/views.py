from django.shortcuts import render
from community.forms import *

# Create your views here.
def list(request) :
    articleList = Article.objects.all()
    return render(request, 'index.html', {'articleList': articleList})


def write(request) :
    if request.method == 'POST' :
        form = Form(request.POST)
        if form.is_valid() :
            form.save()
    else :
        form = Form()

    return render(request, 'write.html', {'form': form})


def view(request, id="1") :
    article = Article.objects.get(id=id)
    return render(request, 'view.html', {'article': article})
