import time
import os
from queue import LifoQueue

#declare global variables

def main():

   global compositNumber
   global productLength
   global maxFactorLength 
   global factorsStack
   global position
   global factor_saved
   global reset
   global factors_found

#   compositNumber = 1017822610193        # 13 digits, factors 1010329 & 1007417
#   compositNumber = 573889                # 6 digits, factors 647 & 887
#   compositNumber = 323                # 3 digits, factors 17 & 19
   compositNumber = 402257


   start = time.time()
   
   factors_found = False
   productLength = len(str(compositNumber))   
   maxFactorLength = round(productLength/2)+1    #two factors will be of equal lengts or upto max 2 digits of diff length


   factorsStack = LifoQueue(maxsize=100000)
   firstDigit(factorsStack)

   while (factorsStack.empty() == False):
      position = 2
      if (getNextDigit()):
         break

   end = time.time()

   logfile = open("log.txt", "a")
   logtext = "Took " + format_seconds_to_hhmmss(end - start) + " to complete !!!\n"
   logfile.write(logtext)
   logfile.write("\n...............\n")
   logfile.close()

def getNextDigit():

   global position
   global factor_saved
   global factorsStack
   global factors_found

   if (factors_found):
      return True

   factor = factorsStack.get()
   print("Checking next pair for position %d factors %d and %d" % (position, factor[0], factor[1]))

   if (factor[0] == factor[1]):
      iter = 6
   else:
      iter = 10

   for i in range(iter):
      t1 = (i*pow(10,position-1))+factor[0]
      for j in range(10):
         t2 = (j*pow(10,position-1))+factor[1]
         t1t2 = t1 * t2
         matchDigits = getLastNDigits(compositNumber,position)
         print("loop counters - %d, %d factors %d and %d prod %d position %d matchdigits %d" % (i, j, t1, t2, t1t2, position, matchDigits))
         if (getLastNDigits(t1t2,position) == matchDigits):
            if (eureka(t1t2, t1, t2)):
               factors_found = True
               return(True)
            else:
               position += 1
               if (position > maxFactorLength):
                  print("Position exceeding maxFactorLength %d" % (position))
                  position = 2
                  return(False)
               else:
                  factorsStack.put([t1,t2])
                  print("Pushed in stack %d and %d" % (t1,t2))
                  getNextDigit()


def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


def closure(logfile, start, end, writeFile, lineCount):
   logtext = "Processed  " + writeFile + " writing " + str(lineCount) + " records in " + format_seconds_to_hhmmss(end - start) + " time !!! " + time.ctime() + "\n"
   logfile.write(logtext)
   logfile.close()  

def getLastNDigits(num,places):
   return(num % pow(10,places))

def firstDigit(factorsStack):

   lastDigit = compositNumber%10
#   print("in firstdigit ",lastDigit)
   if (lastDigit == 1):                                     # all primes, except 2, are odd so last digit
      factorsStack.put([1,1])                               # has to be odd number except 5. No prime ends with 5.
      factorsStack.put([3,7])
      factorsStack.put([9,9])                      
   else:
      if (lastDigit == 3):
         factorsStack.put([1,3])
         factorsStack.put([7,9])
      else:
         if (lastDigit == 7):
            factorsStack.put([1,7])
            factorsStack.put([3,9])
         else:
            factorsStack.put([1,9])                               
            factorsStack.put([3,3])
            factorsStack.put([7,7])  
   return

def eureka(n, n1, n2):
   if (n == compositNumber):
      logfile = open("log.txt", "a")
      logtext = "   --> Factors of " + str(compositNumber) + " are P1 = " + str(n1) + " and P2 = " + str(n2) + "\n"
      logfile.write(logtext)
      logfile.close()
      factors_found = True
      return True
   else:
      return False


if __name__== "__main__":
   main()

