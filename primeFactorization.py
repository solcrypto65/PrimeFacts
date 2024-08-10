import time
import os
from millify import millify

def main():

   #test_bed = [159947, 86563, 327121, 566477, 41581, 402257, 573889, 121103, 6237241, 17114513, 10889999, ]
   #test_bed = [59444051, 16016003, 1186449732607, 108467929]
   #test_bed = [17114513, 16016003, 10889999, 159343969, 1017822610193]
   #test_bed = [1017822610193]
   #test_bed = [4937808266176958849]
   #test_bed = [79011694142334890191]
   #test_bed = [1021199129711, 9981220219745933, 954870980561]
   test_bed = [6237241, 17114513, 10889999]
   #test_bed = [159947,79011694142334890191,1017822610193,100000658721084779927,4937808266176958849]
   #test_bed = [999818398240193429]
   #test_bed = [932844833507]
   #test_bed = [999999999810542000008973540177]
   #test_bed = [1017822610193]
   #test_bed = [100000658721084779927]
   #test_bed = [1000006587, 21084779927, 99999905389, 506308981135137]

   # TEST WITH ONE COMOSITE NUMBER AT A TIME

   start = time.time()
   
   for indx, product in enumerate(test_bed):
      factors_found = False
      max = len(str(product))                   

      logfile = open("log.txt", "a")
      logtext = "Finding prime factors of " + str(product) + " a " + str(max) + " digit number \n"
      logfile.write(logtext)
      logfile.close()

      max = (max/2)+2      #Assuming two factors will be of equal length or differ in length by max 2 digits 
                           # ie if one factor is of 10 digits, second will be of 8,9 or 10 digits big.

      d1List = firstDigit(product)
 
      for indx2, factor in enumerate(d1List):
         position = 1
         f = open('factors1.txt','w')
         f.write(str(factor[0])+' '+str(factor[1])+'\n')
         f.close()
         while not factors_found and (position < max):
            position = position + 1
            factors_found = getPossibleFactors(product,position,'False')
            if (factors_found):
               break

         if (factors_found):
            break


   end = time.time()

   logfile = open("log.txt", "a")
   logtext = "Took " + format_seconds_to_hhmmss(end - start) + " to complete !!!\n"
   logfile.write(logtext)
   logfile.write("\n...............\n")
   logfile.close()

def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)

def getPossibleFactors(product, position, factors_found):
      matchDigits = getLastNDigits(product,position)
      
      writeFile = "factors"+str(position)+".txt"
      fw = open(writeFile, "w")
      lineCount = 0

      readFile = "factors"+str(position-1)+".txt"
      fr = open(readFile,"r")
      line = fr.readline()
      start = time.time()
      bufferedWrite = ""
      bwCount = 0
      
      logfile = open("log.txt", "a")      

      while line != "":
         factor1 = line.split()
         factor1[0] = int(factor1[0])
         factor1[1] = int(factor1[1])
         line = fr.readline()                            # read next line from readfile

         if (factor1[0] == factor1[1]):                  # if possible factors are same, 1 & 1 or 334 & 334 then iterate 6 times
            iter = 6
         else:
            iter = 10

         for i in range(iter):
            t1 = (i*pow(10,position-1))+factor1[0]
            for j in range(10):                                         # Code in inner 'for' loop will get executed billions of
               t2 = (j*pow(10,position-1))+factor1[1]                   # time as we move left from least significant digit 
               t1t2 = t1 * t2                                           # Any focus on optimizing this part of code will give
               if (getLastNDigits(t1t2,position) == matchDigits):       # significant performance benefit
                  if (eureka(t1t2, t1, t2, product)):
                     end = time.time()
                     closure(logfile,start,end, writeFile, lineCount)
                     fw.close()
                     fr.close() 
                     if os.path.exists(writeFile):
                        os.remove(writeFile) 
                     if os.path.exists(readFile):
                        os.remove(readFile)    
                     return(True)
                  else:
                     bufferedWrite = bufferedWrite + (str(t1)+" "+str(t2)+'\n')
                     bwCount += 1
                     lineCount += 1
                  break                               #for a value of i, applicable value of j is found so close inner loop
   
         if (bwCount > 50000):                        # instead of writing one line at a time , buffer the lines in list
            fw.write(bufferedWrite)                   # and write when 50k lines are gathered.
            bufferedWrite = ""                        # But this has not given any performance benefit.
            bwCount = 1
            
      if (bufferedWrite != ""):
         fw.write(bufferedWrite)                
         bufferedWrite = ""
         bwCount = 1

      end = time.time()
      fw.close()
      fr.close()  
#      fileSize = (os.path.getsize(fw)) / (1024 ** 3)     # get file size in bytes and convert to GB - not working
      closure(logfile,start,end, writeFile, lineCount)
      
      if os.path.exists(readFile):
        os.remove(readFile)                                   # remove the previous readfile

      return(False)                                            # coud not find the prime factors, try with next digit                                        


def closure(logfile, start, end, writeFile, lineCount):
   logtext = "Processed  " + writeFile + " writing " + millify(lineCount, precision=2) + " records " + format_seconds_to_hhmmss(end - start) + " time !!! " + time.ctime() + "\n"
   logfile.write(logtext)
   logfile.close()  

def getLastNDigits(num,places):
   return(num % pow(10,places))

def firstDigit(product):

   ld = getNthDigit(product,0)

   d1List = []

   if (ld == 1):                                            # all primes, except 2, are odd so last digit
      d1List = [[1,1],[3,7],[9,9]]                          # has to be odd number except 5. No prime ends with 5.
   else:
      if (ld == 3):
         d1List = [[1,3],[7,9]]
      else:
         if (ld == 7):
            d1List = [[1,7],[3,9]]
         else:
            d1List = [[1,9],[3,3],[7,7]]

   return d1List

def eureka(n, n1, n2, product):
   if (n == product):
      logfile = open("log.txt", "a")
      logtext = "   --> Factors of " + str(product) + " are P1 = " + str(n1) + " and P2 = " + str(n2) + "\n"
      logfile.write(logtext)
      logfile.close()
      return True
   else:
      return False

def getNthDigit(num, place):

   #print(num, place)
   if num < (pow(10,place)):
      return 0
   else:
       return int(str(num)[-1-place])


if __name__== "__main__":
   main()

