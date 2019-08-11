
from html.parser import HTMLParser 
import urllib.request

class TagParser(HTMLParser):
    result_dict = {}
    def handle_starttag(self, tag, attrs):
        if not tag in self.result_dict: self.result_dict[tag] = 0
        self.result_dict[tag] = self.result_dict[tag] + 1
    def feed(self, data):
        super().feed(data)
        return self.result_dict

def process_uri(uri):
    with urllib.request.urlopen(uri) as f:
        parser = TagParser()
        c = parser.feed(str(f.read()))
        return c

