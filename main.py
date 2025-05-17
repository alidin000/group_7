# virtual environment =>
# компьютердин ичинде озунчо чойро. 
# библиотекаларды кочурсонуз (бир эле проектке тиешелуу)
# python 3.12 , python 3.9


# git => version control =бир канча адам бир проекттин устундо иштегенде колдонуучу инструмент
# github => бул ошол гиттин проекттердин интернеттеги сакталуучу жер

# tracking => 

import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(type(x))
print(x)



