## USAGE
```
## import library
from easygis import egis
## Contries support: 'vietnamese' only now.
vi_gis = egis(country='vie')
## Load data
dataLoader = vi_gis.loadDatabase()
## Give an example location
pts = [21.038575823260388, 105.77209179475015]
result = vi_gis.findout(pts,dataLoader)
## Result
print(result)
-> {'ward': 'Mai Dịch', 'district': 'Cầu Giấy', 'province': 'Hà Nội'}
```