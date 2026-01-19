import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl(start_url, max_pages=50):
    visited = set()
    to_visit = [start_url]

    domain = urlparse(start_url).netloc

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        try:
            response = requests.get(current_url, timeout=5)
        except requests.RequestException:
            continue

        visited.add(current_url)

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            absolute_url = urljoin(current_url, link["href"])
            parsed_url = urlparse(absolute_url)

            # Stay within the same domain
            if parsed_url.netloc == domain:
                clean_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
                if clean_url not in visited:
                    to_visit.append(clean_url)

    return visited
