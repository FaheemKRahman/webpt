import requests
from copy import deepcopy 

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>"
]


def test_xss(form):
    findings = []

    url = form["action"]
    method = form["method"]
    inputs = form["inputs"]

    base_data = {}
    for i in inputs:
        if i["name"]:
            base_data[i["name"]] = "test"

    for payload in XSS_PAYLOADS:
        test_data = deepcopy(base_data)

        for param in test_data:
            test_data[param] = payload

            try:
                if method == "post":
                    response = requests.post(url, data=test_data, timeout=5)
                else:
                    response = requests.get(url, params=test_data, timeout=5)
            except requests.RequestException:
                continue

            if payload in response.text:
                findings.append({
                    "type" : "Reflected XSS",
                    "url" : url,
                    "parameter" : param,
                    "payload" : payload,
                    "evidence" : "Payload reflected unescaped in response"
                })

    return findings