from django.contrib import admin
from .models import score
# Register your models here.

@admin.register(score)
class a(admin.ModelAdmin):
    list_display = ['team_name','score','wicket','vs','id','score2','wicket2','logo']