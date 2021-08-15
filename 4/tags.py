import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""

    xml_root = ET.fromstring(content)
    categories = [el.text for el in list(xml_root.iter('category'))]
    counts = Counter(categories)
    ranks = list(counts.items())
    ranks.sort(key=lambda p: p[1], reverse=True)
    return ranks[:n]
