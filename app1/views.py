from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'msg':"im there"}
    return render(request, 'app1/index.html', context_dict)
