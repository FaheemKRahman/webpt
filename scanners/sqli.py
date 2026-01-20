import requests
from copy import deepcopy


SQLI_PAYLOADS = [
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "' OR 1=1--",
]

SQL_ERRORS = [
    "sql syntax",
    "mysql",
    "sqlite",
    "odbc",
    "postgres",
    "syntax error"
]


def test_sqli(form):
    findings = []

    url = form["action"]
    method = form["method"]
    inputs = form["inputs"]

    # Build baseline data
    baseline_data = {}
    for inp in inputs:
        if inp["name"]:
            baseline_data[inp["name"]] = "test"

    try:
        if method == "post":
            baseline_response = requests.post(url, data=baseline_data, timeout=5)
        else:
            baseline_response = requests.get(url, params=baseline_data, timeout=5)
    except requests.RequestException:
        return findings

    baseline_length = len(baseline_response.text)

    for payload in SQLI_PAYLOADS:
        test_data = deepcopy(baseline_data)

        for param in test_data:
            test_data[param] = payload

            try:
                if method == "post":
                    response = requests.post(url, data=test_data, timeout=5)
                else:
                    response = requests.get(url, params=test_data, timeout=5)
            except requests.RequestException:
                continue

            content = response.text.lower()

            # Error-based detection
            for error in SQL_ERRORS:
                if error in content:
                    findings.append({
                        "type": "SQL Injection",
                        "parameter": param,
                        "payload": payload,
                        "evidence": error,
                        "url": url
                    })
                    break

            # Boolean-based detection
            if abs(len(response.text) - baseline_length) > 100:
                findings.append({
                    "type": "SQL Injection (Possible)",
                    "parameter": param,
                    "payload": payload,
                    "evidence": "Response length differed significantly",
                    "url": url
                })

    return findings
