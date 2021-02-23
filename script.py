from bs4 import BeautifulSoup
import requests

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
    "cookie": "__cfduid=d7e99a72ee7c7e3026747147104246fba1613668817; lbal=http://10.0.8.78:80; _sf=eyJpdiI6IlljYmd5M3E1Q3pGRjd1WDVZdnRWWFE9PSIsInZhbHVlIjoiREkrQ08zWkg3YjAzTUg4ckRhcUdWWCtuXC9jclBEcmI0aXlaMnRZNUw0OU5IaElWN2hBUVJCZmZDaTd5TDl1WEJYU1lXa3MrNk0yVXgrZ2UxNTc0MFByMUFHZHFTQXpOemFQKzRVNFZxaHJuOGpIRzdhTGVwWUJjYW15YXVRWVk3IiwibWFjIjoiZWIxMDUxNTdlYTQ1Nzg2YmIwMmU2NjVjNjQ5OTdiZmI5NDY3NDU3OGMwZmE2NzcyNjhhYmFlZjZlY2RkYzUxYiJ9; _gid=GA1.2.2018021303.1613668821; fpestid=XydmGlb1HGruqD6UO76YiKeCtzWjjUDA8e8Zl-tWFJUFcThA4TPfN3OXVLIF40Bn-mxH_A; usprivacy=1---; _awl=2.1613668828.0.4-73c48aa8-7d554bb8784a4f734e9da55efffce841-6763652d6575726f70652d7765737431-602ea1dc-0; __qca=P0-54308755-1613668828884; st_s=g7sYrxwKsiaGtHlRAsMtq9C5dMIsXdu9jMpcjKih; filter-exchanges=eyJpdiI6Imt4VEFhb2FVV2tkZ2xcL3MyTzJyQUNBPT0iLCJ2YWx1ZSI6InE2SkxnQUpVQWE5aDdNMWJQU1lGVkNJQXN0NGRPblg1dm1CalFwb3REUjA0aVBHRzlsOWRDWjloMFZRK2QxUGpcL2NXTmlEQ1E0cUpYVUlPNERNSFRqUT09IiwibWFjIjoiMWU0MjQ2N2JhOGY1OTlkOWNkMWRmYjU3Y2UxNTNjY2VhMTMwYzg2ZWY3ODgzN2FmZGM2MDA2MTVjMzU3MTdlMCJ9; XSRF-TOKEN=eyJpdiI6IkVMQU5EdEVGRU1Bb2hCWE0zWWN0Vnc9PSIsInZhbHVlIjoiQnM4Y3BNaTdtbDR3NGF4U1p3ZVRITXBTMVE0MWtDbXFnU1VzYlZ3dVhlUEx6cElFM3ZiTDRnVGxLa0hPVWU1TnpIYjNHWndTYzY1V3ZETkxvVDBaUjlubEJvcGxwNDU5QmU2RTQ0SVdkVFhzVHZBR0RcL2FjWUdhRFBDd1ZRclwveSIsIm1hYyI6IjE0NDg1NjFjNmJiYzlmY2ZhNWQxMjdjYWRiOGE0YzY5NWFjYjU1NTJhN2VkNDNjYzFjMDdlMGNmMTFkMDRkNGIifQ%3D%3D; _ga_PDGY9YVDNG=GS1.1.1613755987.3.1.1613761221.0; _ga=GA1.1.1699221961.1613668821",
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
    value = rates[0].get_text()
    growth = rates[1].get_text()
    mom = rates[2].get_text()
    vgm = rates[3].get_text()
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
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.zacks.com/premium/esp-buy",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": 'user_session=76fe92cf943242af31b1f14e2b8bd9e8; _vwo_uuid_v2=DFB06DE7B29975F3860F1AB07EB657FEC|a4addb05d2fb0654a7e7a4507f8dfc7e; _ga=GA1.2.713608766.1613671177; _fbp=fb.1.1613671197524.840183633; _vwo_uuid=DFB06DE7B29975F3860F1AB07EB657FEC; _vwo_ds=3%241613671171%3A86.53399098%3A%3A; _gid=GA1.2.1043937515.1613948858; com.silverpop.iMAWebCookie=c5682211-b902-c5d4-0512-a2496700404d; takeover=1; remember_me=1; CUSTOMER_ID=772270044; ZTOKENID=3c8584b1131de83cd8ce13fb27b4443a; ZCCSUID=0e66b9ea49179f6184206ade6e573cb8; new_zacks_username=ehabwork0%40gmail.com; recentQuotes=WING%2C%2CGLOG%2CXEC; PHPSESSID=9f7cpaotamisudhorf4b84g4f0; _fbc=fb.1.1614025956126.IwAR1mZqg3vHZJEA9O2D9fOsBXe7MtwkY9j18lJJgRNYVsRP9957dDW0ATpc0; AMCVS_3064401053DB594D0A490D4C%40AdobeOrg=1; s_cc=true; s_vnum=1614549600645%26vn%3D6; _vis_opt_s=2%7C; _vis_opt_test_cookie=1; __gads=ID=155dede9fdf007cf:T=1614037051:S=ALNI_MbqarCAwlCn_fLBA74OitQOnFLoSg; AMCV_3064401053DB594D0A490D4C%40AdobeOrg=77933605%7CMCIDTS%7C18680%7CMCMID%7C64589423075614544913980457553145528436%7CMCAAMLH-1614641857%7C6%7CMCAAMB-1614641857%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1614044257s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18684%7CvVersion%7C4.5.1; s_nr=1614037057239-Repeat; s_v17=DEF; s_sq=%5B%5BB%5D%5D; FCCDCF=[["AKsRol8TnasUmsG6lT2zZfys6MlPDomHSWGSwlf267c4nK2qI9SU-AJO5rj6iDCRMwMYwsI9NlZaSP5BCVvt3XZf8u2cAk2fuDGPHrkHXETFS6zRsapR-uy1KoFGUOzUc0EJArPjReZjzcmocZmEEcVN2SdzvA0pzQ=="],null,["[[],[],[],[],null,null,true]",1614037062328]]; _vwo_sn=369434',
}
zacks_session = requests.Session()
zacks_session.headers.update(headers_zacks)


def extract_data_from_json(response):
    response_convert = json.loads(response)
    for i in response_convert["data"]:

        sympol = BeautifulSoup(i[0]).find("button")["rel"]
        link = "https://www.zacks.com/stock/quote/{}".format(sympol)
        r = zacks_session.get(link)
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
extract_data_from_json(r.content)
csv_file = "Names.csv"
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
