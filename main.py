from crawler import crawl
from form_parser import extract_forms
from scanners.sqli import test_sqli
from scanners.xss import test_xss
from scanners.csrf import test_csrf

if __name__ == "__main__":
    target = "http://testphp.vulnweb.com"

    pages = crawl(target)
    all_forms = []

    for page in pages:
        forms = extract_forms(page)
        all_forms.extend(forms)

    print("\nVulnerability test results:\n")

    for form in all_forms:
        findings = []
        findings.extend(test_sqli(form))
        findings.extend(test_xss(form))
        findings.extend(test_csrf(form))


        for finding in findings:
            print(f"[!] {finding['type']}")
            print(f"    URL: {finding['url']}")
            print(f"    Parameter: {finding['parameter']}")
            print(f"    Payload: {finding['payload']}")
            print(f"    Evidence: {finding['evidence']}")
            print("-" * 50)



        #print(f"Page: {form['page']}")
        #print(f"Action: {form['action']}")
        #print(f"Method: {form['method']}")
        #print("Inputs:")
        #for inp in form["inputs"]:
         #   print(f"  - {inp['name']} ({inp['type']})")
        #print("-" * 40)
