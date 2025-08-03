import requests
import json

# Exemplo de payload Prometheus-style
data = {
    "streams": [
        {
            "stream": {"service": "EC2"},
            "values": [["1627316400000000000", "100.5"]]
        }
    ]
}

res = requests.post("http://<loki-endpoint>/loki/api/v1/push", data=json.dumps(data))
print(res.status_code, res.text)
