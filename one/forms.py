
from django import forms
from .models import score


class update_form(forms.ModelForm):
    # worker = WorkerMaster
    class Meta:
        model = score
        fields = ['team_name','vs','score','wicket','score2','wicket2']