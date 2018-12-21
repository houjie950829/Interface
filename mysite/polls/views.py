from django.http import JsonResponse
from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
import time
import json
import os
import random
import socket
from models.readWritYmal import MyYaml
import sys
env = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(env)
from . report import HTML_REPORT, html_template
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.




# @csrf_exempt
# def return_img(request):
#     """在线展示图片"""
#     image_data = open('./polls/img/1.png', "rb").read()
#     return HttpResponse(image_data, content_type="image/png")


@csrf_exempt
def get_report(request):
    try:
        json_str = request.body
        req_data = json.loads(json_str)
        html_report_object = HTML_REPORT(req_data['report_title'], req_data['env_sign'], req_data['theme'], req_data['test_info'], req_data['report_table_title'], req_data['report_cases'])
        html = html_report_object.genHtmlReport(html_template)
        report_name = '{}.html'.format(time.time() + random.randint(1, 999999))
        dir_name = os.getcwd() + '/mysite/templates/{}'.format(report_name)
        with open(dir_name, 'wb') as f:
            f.write(html.encode('utf-8'))
        ip = MyYaml('ip').configYaml
        port = MyYaml('port').configYaml
        domain = MyYaml('domain').configYaml
        hostname = socket.gethostname()
        try:
            my_ip = socket.gethostbyname(hostname)
        except Exception:
            my_ip = '127.0.0.1'
        if ip is None:
            ips = my_ip
        elif ip == '127.0.0.1':
            ips = '127.0.0.1'
        elif ip == my_ip:
            ips = my_ip
        else:
            ips = False
        if domain is None:
            get_url = 'http://{}:{}/polls/report/?name={}'.format(ips, port, report_name)
        else:
            get_url = 'http://{}/polls/report/?name={}'.format(domain, report_name)
        if ips:
            return JsonResponse(
                {
                    'code': 0,
                    'data': {
                        'report_name': report_name,
                        'report_url': get_url,
                        'report_dir': os.path.join(BASE_DIR, 'templates/{}'.format(report_name)),
                    }
                }
            )
        else:
            return JsonResponse(
                {'code': 1001, 'data': '填写ip和本机ip不一致'}
            )
    except Exception as msg:
        return JsonResponse(
            {'code': 1000, 'data': msg}
        )


@csrf_exempt
def report(request):
    name = request.GET.get('name')
    return render(request, name)


