import requests

if __name__ == "__main__":
    res = requests.get(
        url='http://127.0.0.1:8080/resource/t4'
    )
    print(res.status_code)
    print(res.json())

    res = requests.get(
        url='http://127.0.0.1:8080/resource_location/2'
    )
    print(res.status_code)
    d = res.json()
    print(d)
    print(d['sensor_id'])
    print(d['temperature'])
    print(d['location'])
    print(d['datetime'])