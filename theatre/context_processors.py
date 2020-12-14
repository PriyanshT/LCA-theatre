from .models import Coin


def get_spare_coin_to_context(request):
    user = request.user
    try:
        spareCoin = Coin.objects.get(user=user.username)
        return {
            'spareCoin': spareCoin
        }
    except:
        return {
            'spareCoin': 0
        }
