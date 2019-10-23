import sys
import os
import requests
from bs4 import BeautifulSoup

ip_list = []


def matchIP(str):
    url = "http://ip.chinaz.com/"
    url = url + str
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        file_handle = open(r'd:\test.txt', mode='a')

        for tag in soup.find_all('span', class_='Whwtdhalf w50-0'):
            tag_extractl = tag.get_text().encode('utf-8')
            if tag.get_text().find("IP的物理位置"):  # 过滤掉【IP的物理位置】这个字符
                ipp = str+'#'+tag.get_text()
                file_handle.write(ipp+'\n')
    except Exception as err:
        print('error')

def read_file(file_path):
    if not os.path.exists(file_path):
        print('Please confirm correct filepath !')
        sys.exit(0)
    else:
        with open(file_path, 'r') as source:
            for line in source:
                ip_list.append(line.rstrip('\r\n').rstrip('\n'))
    for ip in ip_list:
        matchIP(ip)


if __name__ == '__main__':
    read_file(r'D:\a.txt')

