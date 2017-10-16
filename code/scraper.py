# This script will scrape bicycles for sale from
# craigslist, and print the title + a link on the termina.

from html.parser import HTMLParser
import requests

# Scrap craigslist for bicycles.
URL = "https://memphis.craigslist.org/search/bia"


class BikeParser(HTMLParser):
    """
    This class implements an HTML parser. It simply looks for links on
    the page of the form:

        <a href="..." class="result-title"> ... </a>

    And then prints the link and the content from inside the tag.

    """
    ok = False
    href = ''

    def handle_starttag(self, tag, attrs):
        self.ok = False  # Assume we haven't seen an <a> tag yet.
        self.href = ''

        if tag == "a":
            # Look for all the html class names
            classes = [value for attr, value in attrs if attr == "class"]
            classes = " ".join(classes)

            # Look for all the href values (ie the links; there should be 1)
            href = [value for attr, value in attrs if attr == "href"]

            if 'result-title' in classes:
                self.ok = True  # We found the right link!
                self.href = "".join(href)

    def handle_data(self, data):
        if self.ok:
            print(data)
            print(self.href)
            print('-----------------')


# 1. Scrape the page...
response = requests.get(URL)
if response.status_code == 200:
    # 2. Decode content from bytes to a string.
    content = response.content.decode("utf8")

    # Create an intance of our parser and parse the results.
    parser = BikeParser()
    parser.feed(content)
