#1.Install and import BeautifulSoup from the bs4 module.
#	.Write a simple program to parse a small HTML string.

from bs4 import BeautifulSoup
import requests

html_content='''
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <a href="https://example.com">Example</a>
    <a href="https://google.com">Google</a>
    <p>This is a paragraph.</p>
  </body>
</html>
'''

soup=BeautifulSoup(html_content,"html.parser")
print(soup.title.string)


#2.Given this HTML:
	#.Extract the title text.
	#.Extract the <h1> text.
	#.Extract the paragraph text.

print("Title:",soup.title.text)
print("Heading:",soup.h1.text)
print("para:",soup.p.text)

#3.Write a program to:
	#.Find the first <a> tag.
	#.Print its href attribute.
print(soup.find("a"))
print(soup.find("a").get("href"))


#4.Use .prettify() to format parsed HTML.
print(soup.prettify())

#5.What is the difference between:
	#.find()
	#.find_all()
print(soup.find("h1"))
print(soup.find_all("a"))

#2.Scrape product details from an e-commerce sample page:
'''	.Product name
	.Price
	.Rating
	.Availability
.Extract all image URLs from a webpage.'''

from bs4 import BeautifulSoup

html_content = """
<html>
  <body>
    <div class="product">
      <h2 class="product-name">Wireless Mouse</h2>
      <span class="price">$25</span>
      <span class="rating">4.5</span>
      <p class="availability">In Stock</p>
      <img src="https://example.com/mouse.jpg" />
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_content, "html.parser")

# Extract product details
product_name = soup.find("h2", class_="product-name").text
price = soup.find("span", class_="price").text
rating = soup.find("span", class_="rating").text
availability = soup.find("p", class_="availability").text

print("Product Name:", product_name)
print("Price:", price)
print("Rating:", rating)
print("Availability:", availability)



