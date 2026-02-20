'''
1) Parse HTML – Extract title and h1

from bs4 import BeautifulSoup

html = '''
#<html>
#<head><title>My Page</title></head>
#<body>
#<h1>Welcome</h1>
#<p>This is a paragraph.</p>
#</body>
#</html>
'''

'''

from bs4 import BeautifulSoup
import requests

html = """
<html>
<head><title>My Page</title></head>
<body>
<h1>Main Heading</h1>
<h2>Sub Heading</h2>

<p>First paragraph</p>
<p>Second paragraph</p>

<a href="https://google.com">Google</a>
<a href="https://openai.com">OpenAI</a>

<b>Bold Text</b>

<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>Alice</td><td>25</td></tr>
<tr><td>Bob</td><td>30</td></tr>
</table>

<img src="img1.jpg"/>
<img src="img2.png"/>
</body>
</html>
"""
soup = BeautifulSoup(html,"html.parser")
print(soup.title.text)

print(soup.p.text)


#2) Extract All Paragraphs

print(soup.find_all("p"))

#3 Extract All Links and Count

links=soup.find_all("a")
print(len(links))
for link in links:
    print(link.text,link["href"])


#4) Extract Attributes

tag = soup.find("a")
print(tag.get("href"))

#5) Extract First h2

h2 = soup.find("h2")
print(h2.text)

#Extract Bold Text

for b in soup.find_all("b"):
    print(b.text)


#Extract All href Values
hrefs = [a.get("href") for a in soup.find_all("a")]
print(hrefs)

#Get All Text Without Tags

print(soup.get_text(strip=True))

#Extract Title from Website (Live URL)

url = "https://google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

# Extract All Headings (h1–h6)

for i in range(1, 7):
    for tag in soup.find_all(f"h{i}"):
        print(tag.text)

# Extract Table Data

table = soup.find("table")
print(table)

#Extract Images

image=soup.find_all("img")
for img in image:
    print(img.get("src"))