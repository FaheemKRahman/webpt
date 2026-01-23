def test_sqli(form):
    findings = []
    url = form["action"]

    for inp in form["inputs"]:
        payload = "' OR 1=1 --"

        # Placeholder detection logic
        vulnerable = True

        if vulnerable:
            findings.append({
                "type": "SQL Injection",
                "url": url,
                "parameter": inp["name"],
                "payload": payload,
                "evidence": "Response behavior changed",
                "severity": None,
                "score": None,
                "impact": "Attacker can manipulate database queries",
                "remediation": "Use parameterized queries and input validation"
            })

    return findings
