from django.http import JsonResponse


# Create your views here.


def fibonacci(request, num):
    if num > 100 or num < 1:
        data = {
            "message": "error"
        }
        return JsonResponse(data)
    else:
        num = int(num)
        sequence = list()
        for i in range(0, num):
            if i > 1:
                number = sequence[i - 1] + sequence[i - 2]
                sequence.append(number)
            else:
                sequence.append(i)

        total = sum(sequence)

        data = {
            "member-count": num,
            "sequence": sequence,
            "total": total
        }
        return JsonResponse(data)
