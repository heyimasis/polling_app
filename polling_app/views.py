from django.shortcuts import render
from datetime import datetime, date, time, timedelta
from poll.models import Poll, Vote

def hello_world(request):
	polls = Poll.objects.filter(is_published=True)

	vote_count = Vote.objects.count()

	midnight = datetime.combine(date.today(), time.min)

	today_vote_count = Vote.objects.filter(datetime__gt=midnight).count()

	day_night_midnight = midnight
	next_day_midnight = day_night_midnight + timedelta(days=1)

	votes = []
	for i in range(10):
		votes.append(Vote.objects.filter(datetime__gt=day_night_midnight ,datetime__lt=next_day_midnight).count())
		next_day_midnight = day_night_midnight
		day_night_midnight = day_night_midnight - timedelta(days=1)
	
	return render(request, 'poll/index.html', {
												'polls': polls,
												'polls2': polls,
												'total_vote_count': vote_count,
												'today_vote_count': today_vote_count,
												'votes': votes
												}
	)
