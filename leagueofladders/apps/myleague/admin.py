from django.contrib import admin

from leagueofladders.apps.myleague.models import League, Membership


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    fields = ('name', 'owner', 'is_public')
    inlines = [MembershipInline]
    list_display = ('name', 'owner', 'is_public', 'date_modified')
    list_filter = ['date_modified', 'is_public']
    search_fields = ['name', 'owner__username']