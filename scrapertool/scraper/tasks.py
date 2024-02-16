from celery import shared_task
import requests
from scraper.models import Proxies

def get_records(limit, page_num):
    url = 'https://proxylist.geonode.com/api/proxy-list'

    headers = {
        'authority': 'proxylist.geonode.com',
        'path': f'/api/proxy-list?limit={limit}&page={page_num+1}&sort_by=lastChecked&sort_type=desc',
        'scheme': 'https',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Origin': 'https://geonode.com',
        'Referer': 'https://geonode.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    params = {
        'limit':limit,
        'page':page_num+1,
        'sort_by':'lastChecked',
        'sort_type':'desc'
    } 
    
    res = requests.get(url = url, headers= headers, params= params)
    data = res.json()
    records = data['data']
    num_pages = data['total'] // limit + 1
    
    return records, num_pages

@shared_task
def fetch_records():

    limit = 100
    page_num = 0
    all_records = []
    proxy_records= []

    records, toal_pages = get_records(limit, page_num)
    all_records = all_records + records

    for n in range(1, toal_pages):
        records, _ = get_records(limit, n)
        all_records = all_records + records

    for record in all_records:
        ipaddress = record['ip']
        port = record['port']
        protocols = record['protocols']
        country = record['country']
        uptime = record['upTime']
    
        proxy_data = Proxies(ipaddress= ipaddress, port= port, protocols= protocols, country= country, uptime= uptime)
        proxy_records.append(proxy_data)

    Proxies.objects.bulk_create(proxy_records, batch_size= 100)