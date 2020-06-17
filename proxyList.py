#
# ©PSchreiber2020
# Python Module that returns a "requests" compatible list of proxies
# from www.proxy-list.download
# 
import requests

def getProxyList(limit=10, proto="https", country="DE"):
    url = f"https://www.proxy-list.download/api/v1/get?type={proto}&country={country}&anon=elite"
    proxies = []
    r = requests.get(url)

    if r.status_code not in range(200,299):
        raise Exception(r.text)
    else:
        for line in r.text.splitlines():
            proxies.append({'http' : f'{line}','https' : f'{line}'})

    return validateProxies(proxies)[:limit]

def validateProxies(proxies):
    approved = []
    url = "http://httpbin.org/ip"

    original_ip = requests.get(url).json()['origin']
    print("Checking proxies...")

    for item in proxies:
        print(item['http'], end="\r")
        try:
            r = requests.get(url, proxies=item)
        except:
            continue
        
        if r.json()['origin'].split(",")[0] != original_ip:
            approved.append(item)

    return approved

def rotatingProxies(limit=10, proto="https", country="DE"):
    proxies = getProxyList(limit=limit, proto=proto, country=country)
    for item in proxies:
        yield item

def main():
    # proxy = getProxyList()
    # print(f"Found {len(proxy)} proxy servers: ")
    for i in rotatingProxies():
        print(f"\t{i['http']}")

if __name__ == "__main__":
    main()
