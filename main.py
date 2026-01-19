from crawler import crawl
from form_parser import extract_forms

if __name__ == "__main__":
    target = "http://testphp.vulnweb.com"

    pages = crawl(target)
    all_forms = []

    for page in pages:
        forms = extract_forms(page)
        all_forms.extend(forms)

    print("\nDiscovered forms:\n")

    for form in all_forms:
        print(f"Page: {form['page']}")
        print(f"Action: {form['action']}")
        print(f"Method: {form['method']}")
        print("Inputs:")
        for inp in form["inputs"]:
            print(f"  - {inp['name']} ({inp['type']})")
        print("-" * 40)
