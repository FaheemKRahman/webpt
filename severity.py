def assign_severity(finding):
    vulnerability_type = finding.get("type", "").lower()

    if "sql injection" in vulnerability_type:
        severity = "High"
        score = 9.0
    elif "xss" in vulnerability_type:
        severity = "Medium"
        score = 6.0
    elif "csrf" in vulnerability_type:
        severity = "Medium"
        score = 6.0
    else:
        severity = "Low"
        score = 2.0

    finding["severity"] = severity
    finding["score"] = score

    return finding