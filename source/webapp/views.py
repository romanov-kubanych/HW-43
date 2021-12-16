from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'index.html')

def calculate_view(request):
    first_number = int(request.POST.get('first_number'))
    second_number = int(request.POST.get('second_number'))
    operation = request.POST.get('operations')
    symbol = None
    check = False

    if operation == 'add':
        result = first_number + second_number
        symbol = '+'
    elif operation == 'subtract':
        result = first_number - second_number
        symbol = '-'
    elif operation == 'multiply':
        result = first_number * second_number
        symbol = '*'
    elif operation == 'divine':
        try:
            result = first_number / second_number
            symbol = '/'
        except:
            result = "Bad request"
            check = True
    context = {
        'number1': first_number,
        'number2': second_number,
        'result': result,
        'symbol': symbol,
        'check': check
    }
    return render(request, 'result.html', context)



