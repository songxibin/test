import random

num = random.choice([1, 2])
if num == 1:
    payload = {"key1": "value1", "key2": "value2"}
    r = requests.get("http://httpbin.org/get", param=payload)
else:
    print("current num is 2")
