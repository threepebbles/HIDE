from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .myfile_views import network_state_check

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