from django.shortcuts import render
from app1.models import AllServers

# Create your views here.
def index(request):
    servers_list = AllServers.objects.all()
    context_dict = {'msg':servers_list,'var1':"Index Page"}
    return render(request, 'app1/index.html', context_dict)
