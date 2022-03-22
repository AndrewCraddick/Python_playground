# --------- FROM FPGA --------------------------------------------

#read_result = fpga.read_frame(0x00, 1)
#print(f"FPGA Version: {read_result[0]}")

# PARAMETERS
address = 0x400
number_of_words = 1024
#write_values = [*range(0,1024)]
write_values = [-2]*number_of_words
print(f"Write Values: {write_values}")

# BEFORE WRITE
read_result_before = fpga.read_frame (address, number_of_words)
print(f"BRAM Before:  {read_result_before}")

# AFTER WRITE
fpga.write_frame (address, write_values)
read_result_after = fpga.read_frame (address, number_of_words)
print(f"BRAM After:   {read_result_after}")


def compareResults(write_values, read_result_after):
    if (write_values == read_result_after):
        return "PASS"
    else:
        return "FAIL"

print(f"Words: {number_of_words}")
print(f"Test:  {compareResults(write_values,read_result_after)}")

# --------------------------------------------------------------------


import random
import sys

x = [1,2,4,3]
y = [*range(1,5)]



d = [1]*3
#print(d)
start = 1
end = 4
step = 1

section_of_list = slice(start,end,step)

print (x[section_of_list])


def compareList(x,y):
    if(x==y):
        return "PASS"
    else:
        return "FAIL"

#print(f"Test: {compareList(x,y)}")

num_of_bytes = 10
a = random.randbytes(num_of_bytes)
#print(a)
l = []
for n in a:
    l.append  (n)
#print (l)
