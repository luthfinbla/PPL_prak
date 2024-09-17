from django.shortcuts import render

def UseCaseDiagram(request):
    context = {
        'nama' : 'hello world',
    }
    return render(request, 'UseCaseDiagram.html', context)
