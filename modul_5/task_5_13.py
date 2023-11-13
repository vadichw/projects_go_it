import re

def find_all_emails(text):
    return  re.findall(r"[a-zA-Z][\w\.]+@[a-z]+\.[a-z]{2,}", text)