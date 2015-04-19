import urllib2
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

def get_fname(curr_url):
  return "html/%s" % curr_url[BEGIN_LEN:]

def save_html(num):
  curr_url = get_url(num)
  print "**** opening %s" % curr_url

  curr_page = urllib2.urlopen(curr_url)
  # soup = BeautifulSoup(curr_page.read())

  fname = get_fname(curr_url)

  # s_out = io.open(fname, "w", encoding = 'utf8')
  s_out = open(fname, "w")
  # s_out.write(soup.prettify())
  curr_contents = curr_page.read()
  s_out.write(curr_contents)
  s_out.close()
  print "done writing %s to s_out" % fname

# def make_dicts(num):

# def write_dicts(num):

def main(argv):
  if (len(argv) != 3):
    print "Usage: db_builder.py start end"
    print "Enter pokemon numbers to start/end building. Use normal numbers, not computer indexing."
    sys.exit()

  # add option to save html/build dict later with flags

  for i in range(int(argv[1]),int(argv[2])+1):
    save_html(i)


if __name__ == '__main__':
  main(sys.argv)