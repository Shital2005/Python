
#if we want to store complete application flow and exception details in a  file we should go for python logging  


# levels:

# critical    50
# error       40
# Warning
# info
# debug
# notset

# import logging
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# logging.debug("this is debug info")
# logging.info("imp info")
# logging.error("jdnwj")
# logging.warning("warning")
# logging.critical("critical")

import logging 
logging.basicConfig(filename="newexception.txt",level=logging.DEBUG)
try:
   val1 = int(input("enter first value:"))
   val2 = int(input("enter secong number:"))
   print(val1/val2)

except (ValueError,ZeroDivisionError) as message:
     print(message)
     logging.exception(message)



