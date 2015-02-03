# Importing python library for fetching Internet resource and pattern searching
import urllib2
import re
from BeautifulSoup import BeautifulSoup

def scrap_input(usr_input):
    
    inp = usr_input.split()
    format_input = "+".join(inp)
    
    url = "http://www.junglee.com/mn/search/junglee/ref=nb_sb_iss_cat_00000_9?url=node%3Daps&field-keywords="+format_input+"&rush=n"

    #Grabbing Html from the url
    response = urllib2.urlopen(url)
    html = response.read()
    
    #Creating beautifulsoup object
    soup = BeautifulSoup(html)
    
    #Calling fuction for finding text in html
    products = get_product('a', "class", "title", soup)
	
    product_price = soup.findAll('span', attrs={'class':'price'})
    prices = get_price(product_price) #for removing innerHTml tags

	#Converting string into product list
    product_list = str_to_list(products)
    price_list = str_to_list(prices)

    return product_list, product_price

#Custom function for finding particular tag with specific attribute
def get_product(tag, attr, val, soup):
    ''' Accepts 4 parameters : tag - html tag name, attr - html tag attr
        , val - value of attribute, soup - containing html response. Returns the list of matching
        patterns'''
    #fetching tag using beautifulSoup Method
    titles = soup.findAll(tag, attrs={attr : val})
    
    #Fetching content of the tag using regular expression
    match = re.findall(r'<'+tag+'[^>]*?>(.*?)</'+tag+'>', str(titles))
    
    return str(match)

#Custom function for getting price
def get_price(price_text):
    '''Accepts a string of html content and return filterd price'''
    
    match = re.findall(r'</span[^>]*?>(.*?)</span>', str(price_text))
    return str(match)

def str_to_list(string):
    '''Accepts a string and returns list of by spliting'''
    
    return string.split("',")

    

