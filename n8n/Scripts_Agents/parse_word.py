import sys
import docx
import json

def parse_word(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

if __name__ == "__main__":
    file_path = sys.argv[1]
    text = parse_word(file_path)
    print(json.dumps({"text": text}))

