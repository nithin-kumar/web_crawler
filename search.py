#Author: Nithin Kumar KV
#Discription: Web crawler
import re
import sys

#to return all links in apge
def get_all_links(page):
  #f=open(page,'r')
  #text=f.read()
  #regx for a link
  links=re.findall(r"<a\s+href\s*=\s*['\"](\w[\w.:/\d]*)['\"][/>]",page)
  #print text
  return links

def union(a,b):
  for i in b:
    if i not in a:
      a.append(i)
      
#Function to get the page from web    
def get_page(page):
  try:
    import urllib
    return urllib.urlopen(page).read()
  except:
    print "Something bad happend.........."
    return 
  
#Function to crawl, seed is the src web page
def crawl_web(seed):
  tocrawl=[seed]
  crawled=[]
  index={}
  while tocrawl:
    page=tocrawl.pop()
    if page not in crawled and len(crawled)< 3:
      content=get_page(page)
      if content:
        add_page_to_index(index,page,content)
        union(tocrawl,get_all_links(content))
        crawled.append(page)
        return index
      else:
	return
     # print len(crawled)
  
#INDEX

#Add keyword,url to index
def add_to_index(index,keyword,url):
  if keyword in index:
    index[keyword].append(url)
  else:
    index[keyword]=[url]
  
#Add page to index:
def add_page_to_index(index,url,content):
  keywords=content.split()
  for keyword in keywords:
    add_to_index(index,keyword,url)

#LOOKUP
def lookup(index,keyword):
  if keyword in index:
    return index[keyword]
  return None

    
def main():
  crawl_web("http://en.wikipedia.org/wiki/State_Bank_of_India")
  #print lookup(index,'the')
  #print index
if __name__=='__main__':
  main()
