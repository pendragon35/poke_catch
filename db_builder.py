import urllib2
from bs4 import BeautifulSoup

MAX_POKE_NUM = 721 # get this from bulbapedia
S_URL_BEGIN = "http://serebii.net/pokedex-dp/"
S_URL_END = ".shtml"

def get_url(num):
  if (num < 10):
    num_str = "00" + str(num)
  elif (num < 100):
    num_str = "0" + str(num)
  else:
    num_str = str(num)

  return S_URL_BEGIN+num_str+S_URL_END

def main():
  curr_url = get_url(1)
  print curr_url


if __name__ == '__main__':
  main()