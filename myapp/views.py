from ipware.ip import get_client_ip
from django.shortcuts import HttpResponse
from model.loadModel import sentence_predict, sentence_predict_api
from django.http import JsonResponse
from myapp import info
# Create your views here.


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def index(request):
    print(style.GREEN+get_client_ip(request)[0]+style.RESET)
    return HttpResponse('''
    <html lang="ko> 
        <head>
            <meta charset="UTF-8">
            <title>한국어 욕설 분류</title>
            <link rel="stylesheet" href="https://unpkg.com/mvp.css">            
        </head>
        <body>
            <header>
                <h1>욕설 분류</h1>
                <a href="/info">server_pc_info</a>
            </header>
            <main>
                <form id='form'>
                    <input id="input" type="text" placeholder="여기에 욕설 분류할 문장을 입력하세요">
                    <input type="submit">
                </form>
            </main>
        </body>
        <script>
                const form = document.getElementById('form')
                const input = document.getElementById('input')
                function control(event) {
                    event.preventDefault();
                    location.href = '/check/'+input.value;
                }
                form.addEventListener('submit', control)
            </script>
    </html>
    ''')


def check(request, input):
    result = sentence_predict(input)
    print(f'{input} {result["result"]}')
    return HttpResponse(f'''
    <html lang="ko">
        <head>
            <meta charset="UTF-8" />
            <title>한국어 욕설 분류</title>
            <link rel="stylesheet" href="https://unpkg.com/mvp.css">
        </head>
        <body>
            <header>
                <h1>욕설 분류</h1>
            </header>
            <main>
                <h2>{input} {result['result']}</h2>
                <h3>{result['accuracy']}</h3>
                <a href="/">HOME</a>
            </main>
        </body>
    </html>
    ''')


def api(request, input):
    result = sentence_predict_api(input)
    print(f'{input} {result["result"]}')
    return JsonResponse({"input": input, 'result': result['result'], 'accuracy': result['accuracy']}, status=201, json_dumps_params={'ensure_ascii': False})


def pc_info(request):
    return HttpResponse(f'''
    <html lang="ko">
        <head>
            <meta charset="UTF-8" />
            <title>Server PC Info</title>
            <link rel="stylesheet" href="https://unpkg.com/mvp.css">
        </head>
        <body>
            <header>
                <h1>Server PC Info</h1>
            </header>
            <main>
                <h2> {info.OS_Info()}</h2>
                <h2> {info.CpuInfo()}</h2>
                <h2> {info.RamInfo()}</h2>
                <h2> {info.GpuInfo()}</h2>
                <a href="/">HOME</a>
            </main>
        </body>
    </html>
    ''')
