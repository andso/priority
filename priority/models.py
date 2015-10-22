from django.db import models



class Sprint(models.Model):
    sprint_name = models.CharField(max_length=200)
    sprint_start_date = models.DateTimeField(null=True, blank=True)
    sprint_finish_date = models.DateTimeField(null=True, blank=True)
    sprint_allocation = models.IntegerField(null=True, blank=True)

    #SPRINT_STATUS = (
    #    (CURRENT, 'Current'),
    #    (CLOSED, 'Closed'),
    #    (PLANNING, 'Planning'),
    #)
    #sprint_status = CharField( max_length=2, choices = SPRINT_STATUS, default=PLANNING)
    
class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_cost = models.FloatField(null=True, blank=True)

class Client(models.Model):
	client_name = models.CharField(max_length=200)

class Ticket(models.Model):
    id_qualitor = models.IntegerField()
    priority = models.IntegerField()
    ticket_title = models.CharField(max_length=500, null=True, blank=True)
    ticket_estimation = models.IntegerField(null=True, blank=True)
    ticket_effort = models.IntegerField(null=True, blank=True)
    ticket_status = models.CharField(max_length=20)
    ticket_payback = models.IntegerField(null=True, blank=True)
    sprint = models.ForeignKey(Sprint) 
    team = models.ForeignKey(Team) 
    client = models.ForeignKey(Client) 

	
# Create your models here.
