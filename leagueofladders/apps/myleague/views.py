from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from leagueofladders.apps.myleague.models import League


def details(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    return render(request, 'MyLeague/details.html', {'league': league})


def edit(request, league_id):
    return HttpResponse('TODO: edit league %d' % league_id)


def create(request):
    return HttpResponse('TODO: create league')