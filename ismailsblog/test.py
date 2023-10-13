import requests

url = 'https://sld.verzekerjeauto.nl/api/v1/verify-token'
data ={
    'token':'eyJzbGRJZCI6IjIiLCJkZWFsZXJJZCI6IjI2IiwidXNlcklkIjoiNjMiLCJleHAiOjE2OTU2MzkxNzYsInRpbWVzdGFtcCI6MTY5NTYzOTExNn0=.ea0335564d6cc571def9ee3c443312431f6f92324127efc3135ab867f43cb14c'
}
result = requests.post(url,json=data)
print(result.status_code)
print(result.json())
