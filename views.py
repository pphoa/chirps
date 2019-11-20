from django.shortcuts import render
from django.http import HttpResponse
from .models import ChirpItem

# Create your views here.
def chirpView(request):
	chirp_elements = ChirpItem.objects.all()
	return render(request, 'index.html',
		{'all_chirps': chirp_elements})
