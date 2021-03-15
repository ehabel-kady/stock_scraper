from bs4 import BeautifulSoup
import requests
from datetime import date
headers = {
    "authority": "stockinvest.us",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://stockinvest.us/list/runners",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "_sf=eyJpdiI6IkFOME1lUkNNQW1FMmoxaEh1ZVIrNEE9PSIsInZhbHVlIjoiQWdNcXZWWDNwVnlLWWpOQVJvT1NlU1hcL3N2ODJrY2hIbHkrTUpPMlA5SzU1S0VkXC9rMWJWQUVTQzZuWkNGSjl0ekVzNklBeEtGbnFiVWZkOHZReGtYWnY3cnVhcVRqSkRld1VwTHNGSFg0Z2twaHp2eUpNRGQ4S1hVamZhRU1OKyIsIm1hYyI6ImY4OTNmZmQ5MTk3MGM4ZjEwOTk2YjgzZmMwNGI0YTIxNmU4MWI3Y2UzYzBjZWQzNjljNTA2ZWZjMTE0NjYwNGYifQ==; __qca=P0-673845176-1612835299136; _admrla=2.0-4ab43ef4-9242-024d-3b98-ba200c5cacc7; __stripe_mid=47fc5b22-61df-4e90-a53c-e2d1402f830fdae719; cf_clearance=8fb3df4ed100eb3fc0c1a97adc2cdc3d9b9befc1-1613094182-0-250; _ga=GA1.1.1413685881.1612835295; lbal=http://10.0.8.77:80; _gid=GA1.2.1572658842.1615213700; __cfduid=df6b462c38f145934f197f3b29bd945a01615427459; filter-exchanges=eyJpdiI6IloxWTZkN294aGJEaWwzWUIydTdkK1E9PSIsInZhbHVlIjoiNThhNnN3YXFnNmdGTEhmaE5xXC95QXJTVEFhODdaS2FoaXBzZGpsN1RhdmZIRkxTd002bGl1UlJUak5cL0hkR3M0NDZ1OEF5WE5QcTQyc2s1SFFDQkpSUT09IiwibWFjIjoiNzIzM2ExYzg5Y2RjZmZkYWJiZDNjNmNmNWE4YWJkNjI0NjkxMzE0MjhiMGI0Y2E2ZGYwOTM5Mjg1MTRlMDdiMSJ9; __cf_bm=3f353ac5ce00a3aa50bc8c7540d7724b331da46e-1615724622-1800-ASZml8Jvmeebmtl/xnFR/4MQCqxfAQxp6gHTI1DcKD3Si5POAth3Eol5jF6cWr135uG18U2Su1iuOjMBSrv4XoNTatPheZjr80Sr4Htej1kFmyI7f8qbWsTtC3QkM13hHA==; IC_ViewCounter_stockinvest.us=5; _awl=2.1615724745.0.4-6a967648-4ab43ef49242024d3b98ba200c5cacc7-6763652d617369612d6561737431-604e00c9-3; st_s=Gp2MLamGfNzTngoxEPaDcQUQD6sScGtWrwmnuhPG; XSRF-TOKEN=eyJpdiI6IitaN0MrYUVKbjRISWJwdVN6QkYyNFE9PSIsInZhbHVlIjoicHkycGJZclVVbCtJYk9ObFlzdytLd3BtZ01SV2IrZ2s4OXBYamtSU2daRmtGY2s3OHAzUlpqaFlwZ3lEdkpUSEpjeUZSSm5PUGxYaUw0ajBGSThlK21MTVk5WDRoVExMSnMzWUFaeU5XK1JaZCtoZ2tFYXFud0tWZjBBXC9leHNmIiwibWFjIjoiZWMzNWYzYTUyYTYwYzgzZDNlZTI0ZWE4NTczMDlhODczOGRmZWIwMmI2NDNiOWFlYjBjOWFjNWJlNDExZDY1YSJ9; _gat=1; _ga_PDGY9YVDNG=GS1.1.1615724621.103.1.1615724890.0; _ga=GA1.1.1413685881.1612835295",
}
links = [
    {
        "type": "top candiates",
        "link": "https://stockinvest.us/list/buy/top100",
        "limit": 50,
    },
    {
        "type": "undervalued list",
        "link": "https://stockinvest.us/list/undervalued",
        "limit": 25,
    },
    {
        "type": "possible runner",
        "link": "https://stockinvest.us/list/runners",
        "limit": 200,
    },
    {
        "type": "golden star long",
        "link": "https://stockinvest.us/list/goldenstar-12",
        "limit": 25,
    },
    {
        "type": "golden star short",
        "link": "https://stockinvest.us/list/goldenstar",
        "limit": 25,
    },
]


def get_page_data(response):
    candidate = ""
    status = ""
    stop_loss = ""
    soup = BeautifulSoup(response)
    candidate_status = soup.find("span", {"class": "btn-group mb-20"})
    list_tag = []
    for i in candidate_status:
        if i == "\n":
            continue
        list_tag.append(i)
    candidate = list_tag[0].get_text().replace("\n", "")
    status = list_tag[1].get_text().replace("\n", "")
    if soup.find("span", {"class": "font-weight-400 float-right"}):
        stop_loss = soup.find(
            "span", {"class": "font-weight-400 float-right"}
        ).get_text()
    else:
        stop_loss = soup.find("b").get_text()
    stop_loss = stop_loss.replace("\n", "")
    next_3_months = ""
    all_p = soup.find_all("p", {"class": "text-justified"})
    for i in all_p:
        if "next 3 months" in i.get_text():
            next_3_months = i.find_all("strong")[0].get_text()
            break
    ident = soup.select(".animsition-link > strong")[0].text
    return {
        "candidate": candidate,
        "status": status,
        "stop_loss": stop_loss,
        "next_3_months": next_3_months,
        "id": ident,
    }


def get_zacks_data(response):
    soup = BeautifulSoup(response)
    rank = soup.find_all("p", {"class": "rank_view"})
    rates = rank[1].find_all("span", {"class": "composite_val"})
    value = rates[0].get_text() if len(rates) >= 1 else 'N/A'
    growth = rates[1].get_text() if len(rates) >= 2 else 'N/A'
    mom = rates[2].get_text() if len(rates) >= 3 else 'N/A'
    vgm = rates[3].get_text() if len(rates) >= 4 else 'N/A'
    return {
        "value": value,
        "growth": growth,
        "momentum": mom,
        "vgm": vgm,
        "rank": rank[2].find("a").get_text(),
    }


import csv

stocks = []
s = requests.Session()
s.headers.update(headers)


def find_by_value(k):
    for i in range(len(stocks)):
        # print(stocks[i])
        if "id" in stocks[i].keys():
            if stocks[i]["id"] == k:
                # print("found")
                return stocks[i]


# print()
# soup.find_all("div",{"class":"panel-body pt-10 pb-10"})[1].find("div",{"class":"media"}).find_all("p",{"class":"mb-0"})[0].find("strong").text score
# print(soup.find_all("div",{"class":"panel-body pt-10 pb-10"})[1].find("div",{"class":"media"}).find_all("p",{"class":"mb-0"})[0].find("strong").text.replace("\n",""))
# stock counter  soup.find_all("div",{"class":"panel-body pt-10 pb-10"})[1].find("div",{"class":"media"}).find_all("a",{"class":"comment-target-link text-underline overflow-text-ellipsis"})[0].text
def get_data_from_page(dic):
    limit = dic["limit"]

    count = 0
    while count < limit:
        page = 0
        response = s.get("{}?page={}".format(dic["link"], page)).content
        soup = BeautifulSoup(response, "html.parser")
        table = soup.find_all("div", {"class": "panel-body pt-10 pb-10"})
        if len(table) < 2:
            break
        for i in range(1, len(table)):
            data = {}
            link = (
                table[i]
                .find("div", {"class": "media"})
                .find_all(
                    "a",
                    {
                        "class": "comment-target-link text-underline overflow-text-ellipsis"
                    },
                )[0]["href"]
            )
            r = s.get(link)
            data["stock_counter"] = (
                table[i]
                .find("div", {"class": "media"})
                .find_all(
                    "a",
                    {
                        "class": "comment-target-link text-underline overflow-text-ellipsis"
                    },
                )[0]
                .text
            )
            data["score"] = (
                table[i]
                .find("div", {"class": "media"})
                .find_all("p", {"class": "mb-0"})[0]
                .find("strong")
                .text
            )
            data["price"] = (
                table[i]
                .find("div", {"class": "media"})
                .find_all("p", {"class": "mb-0"})[1]
                .text.strip()
                .split("\n")[0]
            )

            d = get_page_data(r.content)
            data.update(d)
            data["type"] = dic["type"]
            stocks.append(data)
            count += 1
            if count > limit:
                break
        page += 1


import json

# get_data_from_page(r.content)
# print(stocks)
# curl 'https://stockinvest.us/list/buy/top100' \

url_zacks = "https://www.zacks.com/esp/esp_buysell_data_handler.php"
headers_zacks = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '13',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.2.1755220486.1612835394; _vwo_uuid_v2=DD9B13EC83712CC7105E869866530358F|922973e0ce085fb30f098b3763b8c2c5; _vwo_uuid=DD9B13EC83712CC7105E869866530358F; _vwo_ds=3%241612835393%3A63.66285342%3A%3A; remember_me=1; CUSTOMER_ID=336423313; ZTOKENID=6f51fb928f5765d30f2d0b0dcaeada92; ZCCSUID=c6606bcf1f26ac63b8b2255da5783850; _vis_opt_exp_97_combi=1; com.silverpop.iMAWebCookie=45d94d34-1e11-2984-aa88-eea249b0688d; _vis_opt_exp_104_combi=2; PHPSESSID=crrmim7h3jlhnipf9g0g1r9tm0; AMCVS_3064401053DB594D0A490D4C%40AdobeOrg=1; s_cc=true; _vis_opt_s=9%7C; _vis_opt_test_cookie=1; _vwo_uuid_v2=DD9B13EC83712CC7105E869866530358F|922973e0ce085fb30f098b3763b8c2c5; funnelCookie=ultimatetrader; user_session=9afc74e9a007410c29ce7b5b8461dff9; s_v17=DEF; _gid=GA1.2.591498006.1615725959; AMCV_3064401053DB594D0A490D4C%40AdobeOrg=77933605%7CMCIDTS%7C18700%7CMCMID%7C01328758401439657211450758052371291862%7CMCAAMLH-1616330759%7C3%7CMCAAMB-1616330759%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615733159s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.1; s_gapv=Logged%20In; s_vnum=1617206400990%26vn%3D26; s_invisit=true; undefined_s=First%20Visit; recentQuotes=JEF%2CCADE%2CTROW%2CPLAY%2C; s_cm=Other%20Natural%20Referrersundefinedwww.upwork.com; s_cpc=0; _vwo_sn=2890565%3A6; ts_zt_ad_id=2; s_sq=%5B%5BB%5D%5D; _gat=1; s_nr=1615730142043-Repeat; s_p42=premium%3A%20esp-buy; FCCDCF=[["AKsRol_pJ3DLnSj264g1oKFQBCgwCJ0nNvSJcDuFK-ZYb097UKjRsRRn44_Q6rC5LbSKP_rV_jPB-0HGv_YeCaZw0HhaYNTLWBhwr5LLfpJukvPakL-5umdb-FQlQ6QP6AKMro37BDR9uihv_iAwlTRxzOQUpHFIgQ=="],null,["[[],[],[],[],null,null,true]",1615730142251]]',
    'Host': 'www.zacks.com',
    'Origin': 'https://www.zacks.com',
    'Referer': 'https://www.zacks.com/premium/esp-buy?adid=zp_prempage_beatearnings_espfilter&amp;icid=investment_services-zacks_premium-zp_internal-zacks_premium-top_stocks_to_beat_earnings-earnings_esp_filter',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
zacks_session = requests.Session()
zacks_session.headers.update(headers_zacks)


def extract_data_from_json(response):
    response_convert = json.loads(response)
    for i in response_convert["data"]:

        sympol = BeautifulSoup(i[0]).find("button")["rel"]
        link = "https://www.zacks.com/stock/quote/{}".format(sympol)
        r = zacks_session.get(link)
        print(r.content)
        data = get_zacks_data(r.content)
        data["last_updated"] = i[8]
        data["id"] = sympol
        dic = find_by_value(sympol)
        if dic:
            dic.update(data)
        else:
            stocks.append(data)


for i in links:
    get_data_from_page(i)

# find_by_value("ABR")
r = zacks_session.get(url_zacks)
print(r.content)
extract_data_from_json(r.content)   
today = date.today()
csv_file = "stock_data_{}.csv".format(today.strftime("%d/%m/%Y"))
csv_columns = [
    "id",
    "score",
    "price",
    "stock_counter",
    "candidate",
    "status",
    "stop_loss",
    "next_3_months",
    "type",
    "value",
    "growth",
    "momentum",
    "vgm",
    "rank",
    "last_updated",
]

try:
    with open(csv_file, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in stocks:
            writer.writerow(data)
except IOError:
    print("I/O error")
