#
# ©PSchreiber2020
# Python Module that returns a "requests" compatible list of proxy-dicts
# from www.proxy-list.download
# 
import requests

def getProxyList(limit=1, proto="https", country="DE"):
    url = f"https://www.proxy-list.download/api/v1/get?type={proto}&country={country}&anon=elite"
    proxies = []
    r = requests.get(url)
    if r.status_code not in range(200,299):
        raise Exception(r.text)
    else:
        for line in r.text.splitlines():
            proxies.append({f"{proto}" : f"{line}"})
            
    return proxies[:limit]

if __name__ == "__main__":
    print(getProxyList())
