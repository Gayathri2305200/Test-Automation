import requests

url="http://dummy.restapiexample.com/"

def get_verify_employees():
    r=requests.get(url)
    body=r.text
    print(body)
    #assert len(body)==100

get_verify_employees()