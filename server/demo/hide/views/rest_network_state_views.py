from django.contrib.auth.decorators import login_required

from ..models import NetworkState
from ..forms import NetworkStateForm
from django.http import HttpResponse, JsonResponse

def network_state_check(request):
    my_network_state = NetworkState.objects.filter(author=request.user)
    if len(my_network_state)==0:
        form = NetworkStateForm()
        ns = form.save(commit=False)
        ns.author = request.user
        ns.network_state = "False"

        ns.save()
        print("network state created")
        print(ns)
    else:
        print(my_network_state)
    return list(NetworkState.objects.filter(author=request.user))[0].network_state


@login_required(login_url='rest-auth:rest_register')
def rest_get_network_state(request):
    my_network_state = network_state_check(request)
    print('my_network_state: ' + str(my_network_state))
    new_dict = {'result': 'success', 'network_state': my_network_state}

    if request.method == "POST":
        return JsonResponse(new_dict,
                            json_dumps_params={'ensure_ascii': True})
    else:
        return JsonResponse({'result': 'fail', 'message': 'use POST'}, json_dumps_params={'ensure_ascii': True})