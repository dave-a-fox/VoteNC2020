from django.contrib import admin

# Register your models here.
from .models import Candidate, BallotText, District


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 6


class BallotTextAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['ballot_text']})]
    inlines = [CandidateInline]


admin.site.register(BallotText, BallotTextAdmin)
admin.site.register(District)

