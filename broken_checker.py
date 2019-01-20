import requests
from bs4 import BeautifulSoup


# This script doesn't check all the website page, just the one entered
# during input prompt.
# In the future, it might be useful to add the ability to test all the web pages
# not just one web page.


def get_links(url):
    """
    Go on the url entered and try to get all the links on the website.
    Return a list of all the URL that have the root domain in them
    """
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        links = []
        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all('a'):
            if url in link.get("href"):
                links.append(link.get("href"))
        return links


def check_links(links):
    """
    Take a list of all the links gathered with function get_links()
    return a list of only broken links.
    """
    broken_links = []
    for link in links:
        r = requests.get(link)
        if r.status_code != requests.codes.ok:
            broken_links.append(link)
    return broken_links


def main():
    """
    Ask the user to input a valid root domain.
    Get all the links from the web page.
    Check all the links to see which ones are broken.
    Print all the broken links
    """
    url = input("Enter the ROOT domain you want to check. (Format: http:// or https://)\n> ")
    links = get_links(url)
    broken_links = check_links(links)
    if len(broken_links) > 0:
        for link in broken_links:
            print("Broken: " + link)
    else:
        print("No broken links! Congratulations")


main()
