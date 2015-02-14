from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from leagueofladders.apps.myleague.models import League


def details(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    return render(request, 'myleague/details.html', {'league': league})


@login_required
def edit(request, league_id):
    return HttpResponse('TODO: edit league %d' % league_id)


@login_required
def create(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'myleague/create.html')