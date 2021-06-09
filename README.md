# printful-api-python
Unofficial Printful API for Python

---

### Usage


```python

from printful_api import PrintfulAPI

pf = PrintfulAPI(key='<YOUR-API-KEY-GOES-HERE>')

print(pf.get('products'))
print(pf.get('orders'))

```