import requests

try: # to make sure website is valid

    re = requests.get('https://www.github.com')
    status_code = re.status_code
    response_time = re.elapsed
    # checking status of 200 or not
    if status_code == 200:
        print('online')
    else:
        print('offline')

    print(status_code)
    print(response_time.microseconds, 'microseconds')

except:
    print('n/a')
