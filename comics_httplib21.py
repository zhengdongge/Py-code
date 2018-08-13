import httplib2, re

pat = re.compile('<DT><a href="[^"]+">(.+?)</a>')
http = httplib2.Http()
headers, body = http.request("http://18h.mm-cg.com/18H_5717.html")

li = pat.findall(body)
print(headers,body)