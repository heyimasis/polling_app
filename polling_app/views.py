from django.shortcuts import render
from poll.models import Poll

def hello_world(request):
	polls = Poll.objects.all()
	print(polls)
	return render(request, 'poll/home.html', {'polls': polls})