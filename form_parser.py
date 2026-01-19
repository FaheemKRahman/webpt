import requests 
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_forms(url):
    forms = []
    try:
        response = requests.get(url, timeout=5)
    except requests.RequestsException:
        return forms
    
    soup = BeautifulSoup(response.text, "html.parser")

    for form in soup.find_all("form"):
        form_details = {
            "page": url,
            "action": urljoin(url, form.get("action", "")),
            "method": form.get("method", "get").lower(),
            "inputs": []
        }

        for input_tag in form.find_all(["input", "textarea", "select"]):
            input_details = {
                "name": input_tag.get("name"),
                "type": input_tag.get("type", "text")
            }
            form_details["inputs"].append(input_details)

        forms.append(form_details)

    return forms