import requests
head={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
s = requests.get("http://www.baidu.com",headers=head)
print(s.text)