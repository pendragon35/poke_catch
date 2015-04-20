import sys

NUM_POS = 0
NAME_POS = 1
CATCH_POS = 2

def make_dicts(fname):
  num_dict = {}
  name_dict = {}
  try:
    with open(fname,"r") as tables:
      entries = tables.read().split('\n')


      for entry in entries:
        items = entry.split(',')
        if (len(items) != 3):
          continue
        catch_rate = int(items[CATCH_POS])
        num_dict[int(items[NUM_POS])] = catch_rate
        name_dict[items[NAME_POS]] = catch_rate
  except IOError:
    print "File did not exist!"
    sys.exit()

  return num_dict,name_dict


def print_usage():
  print "Usage: calc.py -f filename"
  print "Files should be a csv or txt, with format:"
  print "001,bulbasaur,45"

def main(argv):
  if (len(argv) < 3):
    print_usage()

  for i in range(1,len(argv)):
    if (argv[i] == "-f"):
      fname = argv[i+1]

  nums, names = make_dicts(fname)
  print "nums is %d long and names is %d long" % (len(nums), len(names))

if __name__ == '__main__':
  main(sys.argv)