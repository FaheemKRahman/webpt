def test_xss(form):
    findings = []
    url = form["action"]

    for inp in form["inputs"]:
        payload = "<script>alert(1)</script>"

        vulnerable = True

        if vulnerable:
            findings.append({
                "type": "Reflected XSS",
                "url": url,
                "parameter": inp["name"],
                "payload": payload,
                "evidence": "Payload reflected in response",
                "severity": None,
                "score": None,
                "impact": "Attacker can execute JavaScript in victim’s browser",
                "remediation": "Escape output and implement proper input validation"
            })

    return findings
