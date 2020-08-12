import time
import urllib.request
#The opener that perform the opreations 
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Chrome/35.0.1916.47')]



#this function is Searching for the first link from the HTML file 
def getNextURL(URL): 
    infile = opener.open(URL)
    #decoding ('utf-8') to keep valid character code points in Unicode while reading 
    page = infile.read().decode('utf-8')
    mainPage = page[page.find('<p>'):page.find('<p>')+500] #Find the first <p> tag for the main body
    newPage = mainPage[mainPage.find('<a href="/wiki/')+15:mainPage.find('"',mainPage.find('<a href="/wiki/')+15)] #Find the first href for the link
    return newPage

#Read URL from user
print('Please Enter a valid Wikipedia link :')
URL=input()
newPage = getNextURL(URL)
#Stop when reaching the Philosophy page 
while newPage !='Philosophy':
    URL = 'http://en.wikipedia.org/w/index.php?title=' + newPage 
    #Creates the next link to go to (from the first link)
    newPage = getNextURL(URL)
    print (URL)
    # 0.5 second timeout between queries to avoid heavy load on Wikipedia
    time.sleep(0.5)
    

print(URL)
