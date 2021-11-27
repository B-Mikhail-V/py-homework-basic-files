import json
import os
from pprint import pprint
import collections
import xml.etree.ElementTree as ET
parser_1 = ET.XMLParser(encoding='utf-8')

path = os.path.join(os.getcwd(), 'newsafr.json')
path_2 = os.path.join(os.getcwd(), 'newsafr.xml')

def read_json(file_path, max_len_word=6, top_words=10):
    with open(path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend((description))
            counter_words = collections.Counter(description_words)
        return(counter_words.most_common(top_words))

if __name__ == '__main__':
    read_json(path)

pprint(read_json(path))

def read_xml(file_path, max_len_word=6, top_words=10):
    tree = ET.parse(path_2, parser_1)
    root = tree.getroot()
    description_words = []
    xml_descriptions = root.findall('channel/item/description')
    for xml_description in xml_descriptions:
        description_words_xml = [word for word in xml_description.text.split(' ') if len(word) > max_len_word]
        description_words.extend(description_words_xml)
        counter_words = collections.Counter(description_words)
    return counter_words.most_common(top_words)




pprint(read_xml(path))
