__author__ = 'Jussi'
from mypolls.models import Poll
from django.contrib import admin
from mypolls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        
    ]
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin,)
admin.site.register(Choice)