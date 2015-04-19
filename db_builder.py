import urllib2
import sys
from bs4 import BeautifulSoup

MAX_POKE_NUM = 721 # get this from bulbapedia
S_URL_BEGIN = "http://serebii.net/pokedex-dp/"
BEGIN_LEN = 30 # to avoid recalc
S_URL_END = ".shtml"
SOUP_LIM = 10

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
  fname = get_fname(curr_url)

  s_out = open(fname, "wb")
  curr_contents = curr_page.read()
  s_out.write(curr_contents)
  s_out.close()

  print "done writing %s to s_out" % fname

def make_dicts(num,source,outfile):
  curr_url = get_url(num)

  if (source == '-l'):
    fname = get_fname(curr_url)
    curr_html = open(fname,"r")
  elif (source == '-i'):
    curr_html = urllib2.urlopen(curr_url)


  soup = BeautifulSoup(curr_html)
  if (source == '-l'):
    curr_html.close()

  poke_name = soup.title.string.split(' ')[-1].lower().encode("ascii",'ignore')

  fooinfos = soup.findAll("td","fooinfo",limit=SOUP_LIM)
  catch_rate = int(fooinfos[-1].string)

  # print "fooinfos for %s" % poke_name
  # print fooinfos
  # print "\ncatch rate for %s is %d" % (poke_name,catch_rate)
  outfile.write("%d,%s,%d\n" % (num,poke_name,catch_rate))

def print_usage():
  print "Usage: db_builder.py [-s/-d] start end [-l/-i]"
  print "Enter pokemon numbers to start/end building. Use normal numbers, not computer indexing."
  print "-s to store, -d to build dict"
  print "For dict: -l to use local, -i for internet"

def main(argv):
  if (len(argv) == 1):
    print_usage()
    sys.exit()
  elif (argv[1] == "-s" and len(argv) == 4):
    for i in range(int(argv[2]),int(argv[3])+1):
      save_html(i)
  elif (argv[1] == "-d" and len(argv) == 5):
    with open("table.txt","a+") as outfile:
      #check if last line is > start or end
      outfile.seek(-100,1)
      last = outfile.readlines()[-1]

      last_num = int(last.split(',')[0])

      start = int(argv[2])
      end = int(argv[3])+1
      if (last_num >= start):
        start = last_num + 1
      if (last_num >= end - 1):
        print "Error: table exists past specified end number"
        print "Now quitting..."
        sys.exit()

      for i in range(start,end):
        make_dicts(i, argv[4], outfile)
        if (i % 10 == 0):
          print "finished #%d" % i
  else:
    print_usage()
    sys.exit()



if __name__ == '__main__':
  main(sys.argv)