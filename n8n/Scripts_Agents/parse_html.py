import sys
from bs4 import BeautifulSoup
import json

def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text(separator='\n')
    return text

if __name__ == "__main__":
    file_path = sys.argv[1]
    text = parse_html(file_path)
    print(json.dumps({"text": text}))

