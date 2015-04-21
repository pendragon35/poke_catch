import urllib2
import sys, os
from bs4 import BeautifulSoup

# make these a list!
MAX_POKE_NUM = [151,251,386,493,649,720]

# LIST THIS TOO! yay
S_URL_BEGIN = "http://www.serebii.net/pokedex"
S_URL_GEN = ["/","/","-rs/","-dp/","-bw/","-xy/"]
BEGIN_LEN = [31, 31, 34, 34, 34, 34]

S_URL_END = ".shtml"

SOUP_LIM = [-1,-1,598,10,10,9]
NAME_IDX = [-1,-1,35,0,0,1]
tnames = ["na.txt","na.txt","table_rs.csv","table_dp.csv","table_bw.csv","table_xy.csv"]

def get_url(num,gen):
  if (num < 10):
    num_str = "00" + str(num)
  elif (num < 100):
    num_str = "0" + str(num)
  else:
    num_str = str(num)

  return S_URL_BEGIN+S_URL_GEN[gen]+num_str+S_URL_END

def get_fname(curr_url,gen):
  return "html/%s" % curr_url[BEGIN_LEN[gen]:]

def save_html(num,gen):
  curr_url = get_url(num,gen)
  print "**** opening %s" % curr_url

  curr_page = urllib2.urlopen(curr_url)
  fname = get_fname(curr_url,gen)

  s_out = open(fname, "wb")
  curr_contents = curr_page.read()
  s_out.write(curr_contents)
  s_out.close()

  print "done writing %s to s_out" % fname

def make_dicts(num,source,outfile,gen):
  curr_url = get_url(num,gen)

  if (source == 'l'):
    fname = get_fname(curr_url,gen)
    curr_html = open(fname,"r")
  elif (source == 'i'):
    curr_html = urllib2.urlopen(curr_url)


  soup = BeautifulSoup(curr_html)
  if (source == 'l'):
    curr_html.close()

  if (gen+1 != 3):
    infos = soup.findAll("td","fooinfo",limit=SOUP_LIM[gen])
  else:
    infos = soup.findAll("td",limit=SOUP_LIM[gen])

  try:
    poke_name = infos[NAME_IDX[gen]].string.split()[0].encode("ascii",'ignore').lower()
    catch_rate = int(infos[-1].string)
    # print "&*&* rate: " + str(catch_rate)
    outfile.write("%d,%s,%d\n" % (num,poke_name,catch_rate))

  except AttributeError:
    print "infos for %d" % num
    print infos
    print "skipped %d, please add manually: %s" % (num, curr_url)
  except IndexError:
    pass
    # print "infos for %d" % num
    # print infos

  # debugging stuff
  # cr_str = infos[-1].string
  # print cr_str


  # print "\ncatch rate for %s is %d" % (poke_name,catch_rate)

def print_usage():
  print "Usage: db_builder.py -f [s/d] -g [gen] -r [start end]  -s [l/i]"
  print "Enter pokemon numbers to start/end building. Use normal numbers, not computer indexing."
  print "-s to store, -d to build dict"
  print "For dict: -l to use local, -i for internet"

def get_range(a, b, gen):
  start = a
  end = b + 1
  if (start > MAX_POKE_NUM[gen]):
    print "no pokemon past this range!"
    start = -1
  if (end > MAX_POKE_NUM[gen] + 1):
    end = MAX_POKE_NUM[gen] + 1

  return start,end


def main(argv):
  # -g for gen
  # -r to indicate range
  # -f for function (s or d)
  # -s for source (l or i)

  if (len(argv) < 8):
    print_usage()
    sys.exit()

  for i in range(1,len(argv)):
    if (argv[i] == "-f"):
      function = argv[i+1]
    elif (argv[i] == "-g"):
      gen = int(argv[i+1]) - 1
      if (gen+1 > 6 or gen+1 < 1):
        print "Invalid generation."
        sys.exit()
      if (get+1 == 3):
        print "Sorry, Gen III not currently supported. Please use Gen IV."
        sys.exit()
    elif (argv[i] == "-r"):
      start, end = get_range(int(argv[i+1]), int(argv[i+2]), gen)
      if (start == -1):
        sys.exit()

    elif (argv[i] == "-s"):
      source = argv[i+1]

  if (function == "s"): # save files
    for i in range(start, end):
      save_html(i,gen)

  elif (function == "d" and len(argv) == 10): # write db
    if (gen <= 1):
      print "Gen I and II don't have catch rates for individual pokemon. No need to build db!"
      print "Now quitting..."
      sys.exit()

    with open(tnames[gen],"a+") as outfile:
      # check if last line is > start or end

      try:
        # helpful code from SO by Trasp
        outfile.seek(-2, 2)            # Jump to the second last byte.
        while outfile.read(1) != "\n": # Until EOL is found...
          outfile.seek(-2, 1)          # ...jump back the read byte plus one more.
        last = outfile.readline()      # Read last line.

        last_num = int(last.split(',')[0])

        if (last_num >= MAX_POKE_NUM[gen]):
          print "All pokemon already have been imported. Now quitting..."
          sys.exit()
        if (last_num >= start):
          start = last_num + 1          
        if (last_num >= end - 1):
          print "Error: table exists past specified end number"
          print "Now quitting..."
          sys.exit()

      except IOError: #file didn't exit to read last line, skip that
        print "Making new file... If you didn't start at 1, rm and run again starting at 1"

      for i in range(start,end):
        make_dicts(i, source, outfile, gen)
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE) 
        print "finished #%d" % i


    print "Done!"
  else:
    print_usage()
    sys.exit()



if __name__ == '__main__':
  main(sys.argv)