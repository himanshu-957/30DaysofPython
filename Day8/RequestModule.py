import requests

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

response = requests.post('https://httpbin.org/post',
                         data={'id': 1, 'name': 'Himanshu'},
                         headers=newHeaders)

print("Status code: ", response.status_code)

response_Json = response.json()
print("Printing Post JSON data")
print(response_Json['data'])

print("Content-Type is ", response_Json['headers']['Content-Type'])