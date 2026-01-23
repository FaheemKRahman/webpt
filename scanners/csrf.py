def test_csrf(form):
    findings = []

    if not form.get("csrf_token"):
        findings.append({
            "type": "CSRF",
            "url": form["action"],
            "parameter": "N/A",
            "payload": "N/A",
            "evidence": "No CSRF token detected",
            "severity": None,
            "score": None,
            "impact": "Attacker can force victims to submit authenticated requests",
            "remediation": "Implement anti-CSRF tokens and same-site cookies"
        })

    return findings
