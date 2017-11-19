import datetime
import re


def extract_number(text):
    p = re.compile(r'\d+')
    return p.findall(text)[0]

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
