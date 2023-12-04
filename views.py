from django.shortcuts import render
import requests
from requests.sessions import Session
import bs4
from bs4 import BeautifulSoup

# Create your views here.
def index(request): 
    if request.method == "POST":
        identity = request.POST.get('identity')
        url = f"https://consultaweb.ant.gob.ec/PortalWEB/paginas/clientes/clp_grid_citaciones.jsp?ps_tipo_identificacion=CED&ps_identificacion={identity}"
        session = Session()
        session.headers.update({
            'Cookie': 'JSESSIONID=XbEpS_TL2_OxbxZPLGZ29T0d5vHEF5sx3-qr7edHb0wy6nPJjGOx!-2023273006',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
        })

        try: 
            response = session.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            second_table = soup.find_all('table')[1]
            tercer_td = second_table.find_all('td')[2]
            tercer_td = int(tercer_td.text)
            return render(request, 'intro.html', {'tercer_td': tercer_td})
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return render(request, 'intro.html', {'message': e})

    return render(request, 'intro.html')