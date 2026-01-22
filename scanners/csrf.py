def test_csrf(form):
    findings = []

    if form["method"] != "post":
        return findings
    
    inputs = form["inputs"]

    token_found = False
    
    for inp in inputs:
        name = (inp.get("name") or "").lower()
        if "csrf" in name or "token" in name:
            token_found = True
            break

    if not token_found:
        findings.append({
            "type": "Possible CSRF",
            "url": form["action"],
            "parameter": "N/A",
            "payload": "N/A",
            "evidence": "POST form witout apparent CSRF token"
        })

    return findings