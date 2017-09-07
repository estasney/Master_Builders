import requests
from lxml import html

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc3EXZ5zHZw_aabUdgVhE1vNMSSywNKFUIlTUKCLaboVAne6A/formResponse"

entry_price = 'entry.809504561'

def params_builder(entry_price, price):
    params_dict = {}
    params_dict[entry_price] = str(price)
    return params_dict



def post_google_form(form_url, params):
    try:
        r = requests.post(form_url, data=params, headers={"Content-type": "application/x-www-form-urlencoded"})
        return r.text
    except:
        return "Error Posting To Google"


headers_lowes = {'Cookie': '-stop_mobi=yes; akavpau_default=1503987953~id=0f6991883fa712fa2d8fe6d92b599cfc; ak_bmsc=D580834F6AA12795A24B45BC97D398251732E1E637110000C507A5599EB9E571~plsdW1LY0grbx4R78WyYDPYEx3NXXzXBBN3CoYN3GZ0eTiWH0+oDQILiU5nhA8ykFtJw/2UEuJS4lO7m2WL4bqtqJGUMrgoiV98AxVtFfnSGkFgHwkIxwVs5kXC29+L6h+YMITpcmAjuAJnzX6f3iLNmp7DCUkoiwO7T3VQ00zsyRm+A+pye2UVJ1Puc7l9R/26j0ZE7uHl0Yb8oTI2REM9calV08du8utAg3OLitaKcc=; bm_mi=289618183208F7A20D9C7C15D12BCF0A~aRuCn9H4nyCZ0KJNOLhERmwQO5kvO+4hkTthrd7uC46GZ4xy2e7uheUpdwbx03Aw04Zxj/BWlM5R9NDV3wGBCIXq2/EOrPYy1gU4OVJTCGawe5vJb1j01Qt1e3l0Sw40jp01FEK75CEkhgwlDJwiZYTCCIkqIcsfaZc6yn2ou4emZz6jLaGSqScNLOfXts8sXD+Qb2iBIxQLVNWbDO7mMh1V4ZIAEh2sYtKjTz3zV8gaS4bYeRqWCkeHfzDXQQESZCgpgQb4sUAZkbwgH86XWCjLuM49yv2rUQXUWjsMRPwu5JZfDU9YIzozrPE6Fsv5STsDnODRpF4Z9l5xc81rvw==; mbox=session#16adf727e75d455b886d79a7bed50135#1503989515; fsr.a=suspended; AMCVS_5E00123F5245B2780A490D45%40AdobeOrg=1; catSearchResult=50076909|; AMCV_5E00123F5245B2780A490D45%40AdobeOrg=-1176276602%7CMCIDTS%7C17408%7CMCMID%7C35512538991391542103696312338524935201%7CMCAAMLH-1504592454%7C7%7CMCAAMB-1504592454%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1503994854s%7CNONE%7CMCAID%7CNONE; JSESSIONID=0000xjvbcnxCGwLU3hSC9ihFmre:19oo490ir; bm_sv=F579A4DE5DE66A88E4BBF913C2168B0C~WM+KeMtn8h+HOdWDacLE5MEBeeVsXIRFtylUPcbc5yVfr5H8u8zD9PJIJx7QZTkgTEx7zARX2CJpkCQeJmyrfqbDRCTc+hk7Lp8HJb38ctlztovKvzJbrpRRgdruNek6DNPwTUN2a1ihEfmqPdRdxXxyzqNre0Ri5am+ssTHGrk=; sn=0488; user=%7B%22authToken1%22%3A%22%22%2C%22SSOToken%22%3A%22Guest%22%2C%22authToken2%22%3A%22Guest%22%2C%22storeNumber%22%3A%220488%22%2C%22segment%22%3Anull%2C%22zipPrompt%22%3Atrue%2C%22hasReloadedPage%22%3Atrue%7D; s_sess=%20e5%3D1%3B%20s_cpc%3D1%3B%20s_cc%3Dtrue%3B; s_visit=1; s_pers=%20s_vnum%3D1535523655284%2526vn%253D1%7C1535523655284%3B%20gpv_page%3Dlowes%253Adt%253Aoutdoors%253Agrass_grass_seed%253Agrass_seed%253Apdp%7C1503989455297%3B%20gpv_pgtype%3Dproduct-display%7C1503989455299%3B%20gpv_sec%3Doutdoors%7C1503989455301%3B%20s_invisit%3Dtrue%7C1503989455303%3B%20s_lv%3D1503987655304%7C1598595655304%3B%20s_lv_s%3DFirst%2520Visit%7C1503989455304%3B'}

url_lowes = "https://www.lowes.com/pd/Scotts-40-lb-Tall-Fescue-Southern-Gold-Seed/50076909"

page = requests.get(url_lowes, headers=headers_lowes)

tree = html.fromstring(page.content)

price_element = tree.xpath("//span[@itemprop='price']")

price = price_element[0].attrib['content']

post_google_form(form_url=form_url, params=params_builder(entry_price=entry_price, price=price))




