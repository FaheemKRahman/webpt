from crawler import crawl
from form_parser import extract_forms
from scanners.sqli import test_sqli
from scanners.xss import test_xss
from scanners.csrf import test_csrf
from severity import assign_severity
from report import generate_report

if __name__ == "__main__":
    target = "http://testphp.vulnweb.com"

    pages = crawl(target)
    all_forms = []

    for page in pages:
        forms = extract_forms(page)
        all_forms.extend(forms)

    findings = []

    print("\n[+] Running vulnerability tests...\n")

    for form in all_forms:
        findings.extend(test_sqli(form))
        findings.extend(test_xss(form))
        findings.extend(test_csrf(form))

    for finding in findings:
        assign_severity(finding)

        print(f"[!] {finding['type']}")
        print(f"    URL: {finding['url']}")
        print(f"    Parameter: {finding['parameter']}")
        print(f"    Payload: {finding['payload']}")
        print(f"    Evidence: {finding['evidence']}")
        print(f"    Severity: {finding['severity']} ({finding['score']})")
        print("-" * 50)

    generate_report(target, findings)
