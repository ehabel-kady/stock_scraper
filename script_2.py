from bs4 import BeautifulSoup
import requests

url = 'https://www.zacks.com/esp/esp_buysell_data_handler.php'
headers = {
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
res = requests.get(url=url, headers=headers)




print(res.content)