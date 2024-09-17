from django.shortcuts import render

def use_case_result(request):
    context = {
        'nama' : 'hello world',
    }
    return render(request, 'use_case_result.html', context)
