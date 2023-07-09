import requests, time
r = requests.get("http://localhost:8000?max=10", stream=True)
start = time.time()
r.raise_for_status()
for chunk in r.iter_content(chunk_size=None, decode_unicode=True):
    print(f"Got result {round(time.time()-start, 1)}s after start: '{chunk}'")