#!/usr/bin/python
import urllib
import sys

def get_curr(currency,my_currency,outfile,to_address,t,inter=False):

  outfile = open(outfile,'a')
  exch = currency+my_currency
  myurl = urllib.urlretrieve("https://www.google.com/finance?q=CURRENCY%3A"+exch+"&hl=en")
  fo = open(myurl[0],'r')
  rate = 0
  for l in fo:
    if l.startswith('1 '+currency):
      rate = float(l.strip().split('>')[1].split('<')[0].split()[0])
      break
  outfile.write(str(rate)+'\n')
  if inter:
    print 'The current rate between',currency,'and',my_currency,'is',rate
  elif rate < t:
    import smtplib
    fromaddr = 'superinsecure@gmail.com'
    toaddrs = to_address
    msg = 'Today is a good day to buy '+currency+' tickets!  The exchange rate is '+str(rate)
    # Hard code your own here
    username = 'superinsecure'
    password = 'password123'

    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit() 

if __name__ == '__main__':
  # Default params
  currency = 'AUD'
  my_currency = 'USD'
  outfile = 'rates'
  to_address = 'youremailaddress@gmail.com'
  t = 1 # Rate threshold 
  inter = False
  for i,a in enumerate(sys.argv):
    if a == '--cur':
      currency = sys.argv[i+1]
    elif a == '--mycur':
      my_currency = sys.argv[i+1]
    elif a == '--out':
      outfile = sys.argv[i+1]
    elif a == '--to':
      to_address = sys.argv[i+1]
      while '@' not in to_address:
        to_address = raw_input('Please specify a complete address')
    elif a == '--rate':
       t=float(sys.argv[i+1])
    elif a == '--inter':
       inter = True

  get_curr(currency,my_currency,outfile,to_address,t,inter)
