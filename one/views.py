from django.shortcuts import render
from .models import score
# Create your views here.
from .forms import update_form

def scorecard(request):
    data = score.objects.all()
    return render(request,'one/scorecard.html',{'data':data})


def manage_score(request):
    data = score.objects.all()
    return render(request,'one/manage_score.html',{'data':data})

def score_update(request,id):
    data = score.objects.all()
    pi = score.objects.get(pk=id)
    if request.method == 'POST':
        fm = update_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        fm = update_form(instance=pi)
    return render(request, 'one/manage_score.html', {'form': fm ,'data':data})
    
