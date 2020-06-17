# proxyList
Python module that returns a list of proxies from https://www.proxy-list.download

## Usage

```python
import proxyList

proxies = getProxyList()
```
Will get you a list of proxy-dict´s with this format: 
```python
{'http' : 'server:port', 'https' : 'server:port' }
``` 
wich you can pass into a 'requests' - request like 
```python
r = requests.get(url, proxies[0])
```

#### You can pass in the following arguments:
- `limit`: desired number of proxy-servers. 
  - default: `10`
- `proto`: protocol ('http', 'https', 'socks4', 'socks5') 
  - default: `'https'`
- `country`: location-code (i.e. 'US', 'DE')
  - default: `'DE'`
