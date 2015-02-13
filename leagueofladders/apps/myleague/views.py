from django.shortcuts import render
from django.http import HttpResponse

from leagueofladders.apps.myleague.models import League


def details(request, league_id):
    league = League.objects.get(pk=league_id)
    context = {'league': league}
    return render(request, 'MyLeague/details.html', context)


def edit(request, league_id):
    return HttpResponse('TODO: edit league %d' % league_id)


def create(request):
    return HttpResponse('TODO: create league')