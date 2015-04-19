import urllib2, io
import sys
from bs4 import BeautifulSoup

MAX_POKE_NUM = 721 # get this from bulbapedia
S_URL_BEGIN = "http://serebii.net/pokedex-dp/"
BEGIN_LEN = 30 # to avoid recalc
S_URL_END = ".shtml"

def get_url(num):
  if (num < 10):
    num_str = "00" + str(num)
  elif (num < 100):
    num_str = "0" + str(num)
  else:
    num_str = str(num)

  return S_URL_BEGIN+num_str+S_URL_END

def save_html(num):
  curr_url = get_url(num)
  print "**** opening %s" % curr_url

  curr_page = urllib2.urlopen(curr_url)
  soup = BeautifulSoup(curr_page.read())

  fname = "html/%s" % curr_url[BEGIN_LEN:]

  s_out = io.open(fname, "w", encoding = 'utf8')
  s_out.write(soup.prettify())
  s_out.close()
  print "done writing %s to s_out" % fname

def main():
  for i in range(16,21):
    save_html(i)


if __name__ == '__main__':
  main()