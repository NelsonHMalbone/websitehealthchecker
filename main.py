import requests


try: # to make sure website is valid
    url = 'https://www.google.com'
    re = requests.get(url)
    status_code = re.status_code
    response_time = re.elapsed
    header_date = re.headers['date']
    # checking status of 200 or not
    status = 'Online' if status_code == 200 else 'Offline'
    print(status)
    print(status_code)
    print(response_time.microseconds, 'ms')
    print(header_date)

except:
    print('n/a')
    print('offline')
