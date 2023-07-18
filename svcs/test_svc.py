import requests, time
#r = requests.get("http://localhost:8000?max=10", stream=True)
data = {"prompt":"def add(a,b,c):","do_sample":False,"max_new_tokens":100, "return_full_text":False, "watermark":False} 
r =requests.post("http://127.0.0.1:8000/generate_stream", json=data, stream=True)
start = time.time()
r.raise_for_status()
for chunk in r.iter_content(chunk_size=None, decode_unicode=True):
    print(f"Got result {round(time.time()-start, 1)}s after start: '{chunk}'")





# # def generate_stream_text(client: Client, *args, **kwargs):
# #     for response in client.generate_stream(*args, **kwargs):
# #         if not response.token.special:
# #             yield response.token.text

# from text_generation import Client
# client = Client("http://127.0.0.1:8080")
# rq = {"prompt":"def add(a,b):","do_sample":False,"max_new_tokens":100, "return_full_text":False} 
# #print(client.generate("def add(a,b):", max_new_tokens=17).generated_text)
# # data = {"prompt":}
# for response in client.generate_stream("def add"):
#     if not response.token.special:
#         #yield response.token.text
#         print(response.token.text)