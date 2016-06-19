from django.shortcuts import render, HttpResponse
import json
import requests



def index(request):
    return HttpResponse("Welcome To Blockshare.IO")


def address(request):
    parsed_data = []
    if request.method == 'POST':
        addr = request.POST.get('address')
        response = requests.get('https://api.blockcypher.com/v1/btc/main/addrs/' + addr)
        json_list = []
        all_data = json.loads(response.text)
        json_list.append(response.json())
        parsed_data = []
        btc_data = {}
        for data in json_list:
            if data['final_n_tx'] != 0:
                btc_data['address'] = data['address']
                btc_data['final_balance'] = data['final_balance'] * 0.00000001
                btc_data['total_sent'] = data['total_sent'] * 0.00000001
                btc_data['total_received'] = data['total_received'] * 0.00000001
                btc_data['block_height'] = data['txrefs'][0]['block_height']
                btc_data['confirmations'] = data['txrefs'][0]['confirmations']
            else:
                btc_data['address'] = data['address']
                btc_data['final_balance'] = data['final_balance'] * 0.00000001
                btc_data['total_sent'] = data['total_sent'] * 0.00000001
                btc_data['total_received'] = data['total_received'] * 0.00000001
                btc_data['block_height'] = "Unavailable"
                btc_data['confirmations'] = "Unavailable"
        parsed_data.append(btc_data)
    return render(request, 'app/profile.html', {'data': parsed_data})
