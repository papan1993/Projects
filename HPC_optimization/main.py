import os                  
import sys
import shutil               #remove dir
import errno
import time                 # access current time

path = "/home/soumyadeep/Documents/semester_1/research/hpc"       # path of where all the files are, this file should also be in this directory 

files = []
for r,d,f in os.walk(path):   #add all files in the directory that we're going to run except .txt files and this file
    for file in f:
        if file != "main.py":
            if not file.endswith(".txt"):
                files.append(os.path.join("",file))

                  
                  
                             #code for testing all the files in the directory are read correctly!!!
for f in files:
    print(f)

                         # depending on what file you're testing, we can easily swap the executable needed
exe = "python3 "              # works for C/C++ executables and executables in general,  python would be " python3 " 

#path2 = path + "/output"
#try:
#    os.makedirs(path2)                         # makes a folder with name output if the folder does not exist
#except OSError as exception:
#    shutil.rmtree(path2)                       # removes previous output folder and makes new one
#    os.makedirs(path2) 
#    if exception.errno != errno.EEXIST:
#        raise


for f in files:
    fileout = ""  
    counter = 0
    for i in range(0,len(f)):                        # loop to get everything up to '.' for file output name
        if f[i] != '.' and counter == 0:
            fileout = fileout + f[i] 
        else:
            counter = 1
                                                   # 28 hpcs, 4 hpcs per txt file -> 7 files
    fileout1 = fileout + "1.txt"                        #now have output file name stored ex. a.py -> a1.txt
    fileout2 = fileout + "2.txt"                        #now have output file name stored ex. a.py -> a2.txt
    fileout3 = fileout + "3.txt"                        #now have output file name stored ex. a.py -> a3.txt
    fileout4 = fileout + "4.txt"                        #now have output file name stored ex. a.py -> a4.txt
    fileout5 = fileout + "5.txt"                        #now have output file name stored ex. a.py -> a5.txt
    fileout6 = fileout + "6.txt"                        #now have output file name stored ex. a.py -> a6.txt
    fileout7 = fileout + "7.txt"                        #now have output file name stored ex. a.py -> a7.txt
        
     
    # load the strings to be passed as an argument for running perf 
    # string is loaded with terminal command and correct parameters like what instruction to look at
    # and what file should be ran
    #exe can be changed depending on what file you're running


####################### use this instead

#for python files:
#  sudo perf stat -o -C 1 -A -I 1 --interval-count 100 -o filename.txt --append -e hpcsyouwanthere python3 filenameofexecutable.py

# for regular executable
#  sudo perf stat -o -C 1 -A -I 1 --interval-count 100 -o filename.txt --append -e hpcsyouwanthere ./filenameofexecutable

# -C used for which CPU to run on 
#-I get hpc every 1 ms
#interval-count get 100 hpc
#-o put output into file you specifed -> filename.txt 
#--append doesn't overwrite files
#-e use this and then call up to 4 hpcs at a time
# some hpcs dont work like node-loads etc.
# I only get 20/28 hpcs for mine




    temp  = "sudo perf stat -v -C 0-3 -A -I 10 -o " + fileout1 + " --append -e branch-instructions,branch-misses,bus-cycles,cache-misses " + exe  + f
    print("temp--",temp)
    temp1 = "sudo perf stat -v -C 0-3 -A -I 10 -o " + fileout2 + " --append -e cache-references,cpu-cycles,instructions,ref-cycles "  + exe  + f
    temp2 = "sudo perf stat -v -C 0-3 -A -I 10 -o " + fileout3 + " --append -e L1-dcache-load-misses,L1-dcache-loads,L1-dcache-stores,L1-icache-load-misses " +  exe  + f
    temp3 = "sudo perf stat -v -C 0-3 -A -I 10 -o " + fileout4 + " --append -e LLC-load-misses,LLC-loads,LLC-store-misses,LLC-stores "  + exe  + f
    temp4 = "sudo perf stat -v -C 0-3 -A -I 10 -o " + fileout5 + " --append -e branch-load-misses,branch-loads,dTLB-load-misses,dTLB-loads "  + exe  + f
    temp5 = "sudo perf stat -v -C 0-3 -A -I 10 -o " + fileout6 + " --append -e dTLB-store-misses,dTLB-stores,iTLB-load-misses,iTLB-loads "  + exe  + f
    temp6 = "sudo perf stat -v -C 0-3 -A -I 10 -o " + fileout7 + " --append -e node-load-misses,node-loads,node-store-misses,node-stores "  + exe  + f
     
    # we take the current time and run the program for X seconds based off of how long the program takes
    # We want 100 samples so we run for 8 seconds for this specific C program
    # adjust variable end for different programs
    start = time.time()
    end = 30
    counter = 1
    while(time.time() - start) < end:
        os.system(temp)
        print(counter)
        counter = counter + 1
    start = time.time()
    while(time.time() - start) < end:
        os.system(temp1) 
    start = time.time()
    while(time.time() - start) < end:
        os.system(temp2)
    start = time.time()
    while(time.time() - start) < end:
        os.system(temp3)
    start = time.time()   
    while(time.time() - start) < end:
        os.system(temp4)
    start = time.time()
    while(time.time() - start) < end:
        os.system(temp5)
    start = time.time()
    while(time.time() - start) < end:
        os.system(temp6)
      
    #the os.system(temp) calls will create the files so now that we have them in our directory
    # this section of code will move them to the directory output which we created earlier
    # a warning/error will appear saying can't move to subdirectory which should be ignored
    # this warning goes off when we move a file into an empty directory
    # since we create an new output folder (replace old if exists) we'll always get this warning
    #os.system("mv " + fileout1 + ' ' + path + ' ' +  path2)
    #os.system("mv " + fileout2 + ' ' + path + ' ' +  path2)
    #os.system("mv " + fileout3 + ' ' + path + ' ' +  path2)
    #os.system("mv " + fileout4 + ' ' + path + ' ' +  path2)
    #os.system("mv " + fileout5 + ' ' + path + ' ' +  path2)
    #os.system("mv " + fileout6 + ' ' + path + ' ' +  path2)
    #os.system("mv " + fileout7 + ' ' + path + ' ' +  path2) 


