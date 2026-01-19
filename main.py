from crawler import crawl

if __name__ == "__main__":
    target = "http://testphp.vulnweb.com"
    pages = crawl(target)

    print("Discovered pages: ")
    for page in pages:
        print(page)
