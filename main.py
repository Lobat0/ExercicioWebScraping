import requests
from lxml import html
import pandas as pd


def requisition():

    headers = {
        'Host': 'www.scrapethissite.com',
        'Sec-Ch-Ua': '"Not(A:Brand";v="8", "Chromium";v="144"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'pt-BR,pt;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.scrapethissite.com/pages/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=0, i',
        # 'Cookie': '_gcl_au=1.1.1136579133.1770566299; _ga=GA1.2.308330386.1770566299; _gid=GA1.2.2020188484.1770566299; _gat=1; _fbp=fb.1.1770566300096.649157176127979125; _ga_09N5RQCFG4=GS2.2.s1770566299$o1$g1$t1770566300$j59$l0$h0',
    }

    response = requests.get('https://www.scrapethissite.com/pages/simple/',  headers=headers,
                            verify=False)


    tree = html.fromstring(response.content)
    paises = []
    for pais in tree.xpath("//div[@class='col-md-4 country']"):
        nome = pais.xpath(".//h3[@class='country-name']")[0].text_content().strip()
        capital = pais.xpath(".//span[@class='country-capital']")[0].text_content().strip()
        populacao = pais.xpath(".//span[@class='country-population']")[0].text_content().strip()
        area = pais.xpath(".//span[@class='country-area']")[0].text_content().strip()

        paises.append({'Pais': nome, 'Capital': capital, 'População': populacao, 'Area': area})

    df = pd.DataFrame(paises)
    df.to_csv('paises.csv', sep=';', index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    requisition()

