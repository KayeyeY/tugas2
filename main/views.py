from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Kay Online Item',
        'name': 'Kevin Yehezkiel Manurung',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)