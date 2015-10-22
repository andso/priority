from django.shortcuts import render
from models import Team
from models import Ticket
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    teams_list = Team.objects.all()
    return render_to_response('priority/index.html', {'teams_list': teams_list})


def backlog(request, team_id):
	stories_backlog = Ticket.objects.all()
	print 'here'
	
	return render_to_response('priority/backlog.html', {'stories_backlog': stories_backlog}, context_instance=RequestContext(request) )
