import urllib2

response = urllib2.urlopen("https://github.com/zhou-dong")

html = response.read()

print html
