from django.http import JsonResponse
# アメリカのブヘラファイル抽出の読み込みをする。
from .scraipingfilses.Bucherer.usaBuchererdataget import main 

def usaBuchererexcution(request):
    if request.method == "POST":
        result = main()
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'POSTリクエストを送信してください。'})



