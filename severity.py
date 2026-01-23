def assign_severity(finding):
    if finding["type"] == "SQL Injection":
        finding["severity"] = "High"
        finding["score"] = 8.5

    elif finding["type"] == "Reflected XSS":
        finding["severity"] = "Medium"
        finding["score"] = 6.5

    elif finding["type"] == "CSRF":
        finding["severity"] = "Medium"
        finding["score"] = 6.0

    else:
        finding["severity"] = "Low"
        finding["score"] = 3.0

    return finding
