
from bs4 import BeautifulSoup
import requests
headers = {"authority": 'stockinvest.us' ,
"pragma": 'no-cache' ,
"cache-control": 'no-cache' ,
"upgrade-insecure-requests": '1' ,
"user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' ,
"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
"sec-fetch-site": 'same-origin' ,
"sec-fetch-mode": 'navigate' ,
"sec-fetch-user": '?1' ,
"sec-fetch-dest": 'document' ,
"referer": 'https://stockinvest.us/list/runners' ,
"accept-language": 'en-US,en;q=0.9' ,
"cookie":'__cfduid=d7e99a72ee7c7e3026747147104246fba1613668817; lbal=http://10.0.8.78:80; _sf=eyJpdiI6IlljYmd5M3E1Q3pGRjd1WDVZdnRWWFE9PSIsInZhbHVlIjoiREkrQ08zWkg3YjAzTUg4ckRhcUdWWCtuXC9jclBEcmI0aXlaMnRZNUw0OU5IaElWN2hBUVJCZmZDaTd5TDl1WEJYU1lXa3MrNk0yVXgrZ2UxNTc0MFByMUFHZHFTQXpOemFQKzRVNFZxaHJuOGpIRzdhTGVwWUJjYW15YXVRWVk3IiwibWFjIjoiZWIxMDUxNTdlYTQ1Nzg2YmIwMmU2NjVjNjQ5OTdiZmI5NDY3NDU3OGMwZmE2NzcyNjhhYmFlZjZlY2RkYzUxYiJ9; _gid=GA1.2.2018021303.1613668821; fpestid=XydmGlb1HGruqD6UO76YiKeCtzWjjUDA8e8Zl-tWFJUFcThA4TPfN3OXVLIF40Bn-mxH_A; usprivacy=1---; _awl=2.1613668828.0.4-73c48aa8-7d554bb8784a4f734e9da55efffce841-6763652d6575726f70652d7765737431-602ea1dc-0; __qca=P0-54308755-1613668828884; st_s=g7sYrxwKsiaGtHlRAsMtq9C5dMIsXdu9jMpcjKih; filter-exchanges=eyJpdiI6Imt4VEFhb2FVV2tkZ2xcL3MyTzJyQUNBPT0iLCJ2YWx1ZSI6InE2SkxnQUpVQWE5aDdNMWJQU1lGVkNJQXN0NGRPblg1dm1CalFwb3REUjA0aVBHRzlsOWRDWjloMFZRK2QxUGpcL2NXTmlEQ1E0cUpYVUlPNERNSFRqUT09IiwibWFjIjoiMWU0MjQ2N2JhOGY1OTlkOWNkMWRmYjU3Y2UxNTNjY2VhMTMwYzg2ZWY3ODgzN2FmZGM2MDA2MTVjMzU3MTdlMCJ9; XSRF-TOKEN=eyJpdiI6IkVMQU5EdEVGRU1Bb2hCWE0zWWN0Vnc9PSIsInZhbHVlIjoiQnM4Y3BNaTdtbDR3NGF4U1p3ZVRITXBTMVE0MWtDbXFnU1VzYlZ3dVhlUEx6cElFM3ZiTDRnVGxLa0hPVWU1TnpIYjNHWndTYzY1V3ZETkxvVDBaUjlubEJvcGxwNDU5QmU2RTQ0SVdkVFhzVHZBR0RcL2FjWUdhRFBDd1ZRclwveSIsIm1hYyI6IjE0NDg1NjFjNmJiYzlmY2ZhNWQxMjdjYWRiOGE0YzY5NWFjYjU1NTJhN2VkNDNjYzFjMDdlMGNmMTFkMDRkNGIifQ%3D%3D; _ga_PDGY9YVDNG=GS1.1.1613755987.3.1.1613761221.0; _ga=GA1.1.1699221961.1613668821' }
links = [{"type":"top candiates","link":"https://stockinvest.us/list/buy/top100","limit":50},{"type":"undervalued list","link":"https://stockinvest.us/list/undervalued","limit":25},{"type":"possible runner","link":"https://stockinvest.us/list/runners","limit":200},
{"type":"golden star long","link":"https://stockinvest.us/list/goldenstar-12","limit":25},{"type":"golden star short","link":"https://stockinvest.us/list/goldenstar","limit":25}]
def get_page_data(response):
    candidate = ''
    status = ''
    stop_loss = ''
    soup = BeautifulSoup(response)
    candidate_status = soup.find('span', {'class':'btn-group mb-20'})
    list_tag = []
    for i in candidate_status:
        if i=='\n':
            continue
        list_tag.append(i)
    candidate = list_tag[0].get_text().replace('\n','')
    status = list_tag[1].get_text().replace('\n','')
    if soup.find('span', {'class':'font-weight-400 float-right'}):
        stop_loss = soup.find('span', {'class':'font-weight-400 float-right'}).get_text()
    else:
        stop_loss = soup.find('b').get_text()
    stop_loss = stop_loss.replace('\n', '')
    next_3_months = ''
    all_p = soup.find_all('p', {'class':'text-justified'})
    for i in all_p:
        if 'next 3 months' in i.get_text():
            next_3_months = i.find_all('strong')[0].get_text()
            break
    return {
        'candidate': candidate,
        'status': status,
        'stop_loss': stop_loss,
        'next_3_months': next_3_months
    }

def get_zacks_data(response):
    soup = BeautifulSoup(response)
    rank = soup.find_all('p', {'class':'rank_view'})
    rates = rank[1].find_all('span',{'class':'composite_val'})
    value = rates[0].get_text()
    growth = rates[1].get_text()
    mom = rates[2].get_text()
    vgm = rates[3].get_text()
    return {
        'value': value,
        'growth': growth,
        'momentum': mom,
        'vgm': vgm,
        'rank': rank[2].find('a').get_text()
    }


import csv

stocks = []
s = requests.Session()
s.headers.update(headers)
# print()
# soup.find_all("div",{"class":"panel-body pt-10 pb-10"})[1].find("div",{"class":"media"}).find_all("p",{"class":"mb-0"})[0].find("strong").text score
# print(soup.find_all("div",{"class":"panel-body pt-10 pb-10"})[1].find("div",{"class":"media"}).find_all("p",{"class":"mb-0"})[0].find("strong").text.replace("\n",""))
# stock counter  soup.find_all("div",{"class":"panel-body pt-10 pb-10"})[1].find("div",{"class":"media"}).find_all("a",{"class":"comment-target-link text-underline overflow-text-ellipsis"})[0].text
def get_data_from_page(dic):
    limit = dic['limit']
    
    count = 0
    while count<limit :
        page=0
        response=s.get("{}?page={}".format(dic['link'],page)).content
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find_all("div",{"class":"panel-body pt-10 pb-10"})
        if len(table) < 2: break
        for i in range(1,len(table)):
            data = {}
            link = table[i].find("div",{"class":"media"}).find_all("a",{"class":"comment-target-link text-underline overflow-text-ellipsis"})[0]['href']
            r = s.get(link)
            data['stock_counter'] = table[i].find("div",{"class":"media"}).find_all("a",{"class":"comment-target-link text-underline overflow-text-ellipsis"})[0].text
            data["score"] = table[i].find("div",{"class":"media"}).find_all("p",{"class":"mb-0"})[0].find("strong").text
            d = get_page_data(r.content)
            data.update(d)
            data['type']=dic['type']
            stocks.append(data)
            count+=1
            if count>limit: break
        page+=1

for i in links:
    get_data_from_page(i)

# get_data_from_page(r.content)
# print(stocks)
csv_file = "Names.csv"
csv_columns = ['score','stock_counter','candidate','status','stop_loss','next_3_months','type']

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in stocks:
            writer.writerow(data)
except IOError:
    print("I/O error")
# curl 'https://stockinvest.us/list/buy/top100' \

url_zacks = 'https://www.zacks.com/esp/esp_buysell_data_handler.php'
headers_zacks = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '13',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_session=9acaa4926660df613307834b6540852f; AMCVS_3064401053DB594D0A490D4C%40AdobeOrg=1; _ga=GA1.2.867734770.1613669457; s_cc=true; _fbp=fb.1.1613669457116.1705067711; _vwo_uuid_v2=D64E30872A277B9ABDE2884A327CB184A|2f92e2894e6f2ac197a6c00c479bebfc; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D64E30872A277B9ABDE2884A327CB184A; _vwo_ds=3%241613669456%3A49.01995459%3A%3A; com.silverpop.iMAWebCookie=53605809-7e06-cddc-44b3-424ac9103612; cf60519feb1344e434b8444b746a915b=cdaeeeba9b4a4c5ebf042c0215a7bb0e; _gid=GA1.2.445744564.1613905398; report_name=7 Best Stocks for the Next 30 Days; welcome_back=1; trustedsite_visit=1; s_prdcts=%5B%5B%2735049%27%2C%271613905975776%27%5D%5D; HomeTradeBanner=1; s_v17=zp_prempage_beatearnings_espfilter; funnelCookie=premiumtrader; remember_me=1; CUSTOMER_ID=772270044; ZTOKENID=df9ae1e053a8c86c908b9a79b2a1e701; ZCCSUID=0e66b9ea49179f6184206ade6e573cb8; new_zacks_username=ehabwork0%40gmail.com; PHPSESSID=pro95qmok89hov4k3q36hnomk7; recentQuotes=CARG%2C; s_p42=premium%3A%20esp-buy; s_vnum=1614546000081%26vn%3D8; s_invisit=true; undefined_s=First%20Visit; _gat=1; AMCV_3064401053DB594D0A490D4C%40AdobeOrg=77933605%7CMCIDTS%7C18680%7CMCMID%7C02934501772713127552405615122030239818%7CMCAAMLH-1614554140%7C6%7CMCAAMB-1614554140%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1613956540s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18687%7CvVersion%7C4.5.1; s_nr=1613949340919-Repeat; s_gapv=Logged%20In; s_sq=%5B%5BB%5D%5D; FCCDCF=[["AKsRol8HXgVqpjI9ifEq9bn_JG45jGlYf4j0oc08HmMcarT0vtpsXwdb1N2EBOTfSyTdC3Jsn6sXLqvD3Jx2lqk2fq_Cw-gx1V1QmWodNnXcz1d-n1p4YrpUWzRNWtJLTVE5dclZVkOHrSARId-f079s6ZFZ8f1CZQ=="],null,["[[],[],[],[],null,null,true]",1613949341347],["CPB0msuPB0msuEsABBENBNCoAP_AAG_AACiQF9JD7T5FYSFCwOpZVJgAEAgTQECAAiQAAAQAAmABQAIQAAACkkAQEASgAAAAAAAAAABBAQAMCAAACQABwABAAAAAAAAABAAAIAAAgAEAAAAIAAACAIAAAAAIAAAAEAAAiwL6gRAALAAeABUAC4AGQAOAAgABEACoAGgAOQAeQBDAEUAJgATwApABWACwAF8AQgApQBowDUANUAewBEQCLAEcAMVAdIB1ADyAKRAU2AvMBfQAAA","1~1765.1716.1577.2202.574.66.70.2357.1301.1451.93.864.2526.571.108.122.1878.440.1097.2253.167.2571.2373.317.311.184.1276.817.2575.196.89.1365.2072.1201.241.149.338.253.588.259.1236.1211.1095.2568.1651.1449.1570.1205.1051.2531.2299.1171.162.1415.415.1126.1127.1870.448.449.1753.486.495.494.482.2677.981.1889.323","170B9EB7-5F57-4A81-8D1B-B25CB7028139"],null]',
    'Host': 'www.zacks.com',
    'Origin': 'https://www.zacks.com',
    'Referer': 'https://www.zacks.com/premium/esp-buy?adid=zp_prempage_beatearnings_espfilter&amp;icid=investment_services-zacks_premium-zp_internal-zacks_premium-top_stocks_to_beat_earnings-earnings_esp_filter',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}