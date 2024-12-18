import requests

"input"
def send_requests_to_websites(filepath):
    with open(filepath, 'r') as file:
        try:
            for line in file:
                url = line.strip()  # removes any whitespaces
                response = requests.get(url)
                response.raise_for_status()
                print(f'response for {url}: {response.status_code}')
        except:

            print(f'An error occured:')


filepath = 'websites.txt'
send_requests_to_websites(filepath)