import json
from datetime import datetime

def generate_report(target, findings):
    findings.sort(key=lambda x: x["score"], reverse=True)

    report = {
        "target": target,
        "scan_date": datetime.utcnow().isoformat(),
        "total_findings": len(findings),
        "findings": findings
    }

    with open("scan_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\n[+] Report generated: scan_report.json")
