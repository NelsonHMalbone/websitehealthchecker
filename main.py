import requests

"input"
def send_requests_to_websites(filepath):
    with open(filepath, 'r') as file:
        try:
            for line in file:
                url = line.strip()  # removes any whitespaces
                response = requests.get(url)
                response.raise_for_status()
                respone_time = response.elapsed
                on_off_stat = ['online' if response.status_code <= 200 else 'Offline']
                print(f'response for {url}: {response.status_code} - {on_off_stat}')
        except requests.exceptions.RequestException as e:
            print(f'An error occured: {e}')


filepath = 'websites.txt'
send_requests_to_websites(filepath)