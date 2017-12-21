from lxml import html
import requests

pages = []

for x in range(1, 101):

  page = requests.get('https://www.yoursitehere.com.br/category/page/' + str(x) + '/')
  tree = html.fromstring(page.content)

  pages.append(tree.xpath('//li[@class="name-class-here"]/text()'))

  print "done page " + str(x)

file = open('file.txt', 'w')

count = 0
for page in pages:
  for exam in page:
    file.write("%s\n" % exam.encode('utf8'))
    count+=1

print "all done! " + str(count) + " itens"
