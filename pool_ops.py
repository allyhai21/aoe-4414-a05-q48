# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Allison Hai
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_in = float('nan') #input channel count
h_in = float('nan') #input height count 
w_in = float('nan') # input width count 
h_pool = float('nan') #avergae pooling kernel height count 
w_pool = float('nan') #avergae pooling kernal width count 
s = float('nan') #stride of average pooling kernel 
p = float('nan') #amount of padding on each of the four input map sides 


# parse script arguments
if len(sys.argv)==8:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    h_pool = float(sys.argv[4])
    w_pool = float(sys.argv[5])
    s = float(sys.argv[6])
    p = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'python3 c_in h_in w_in h_pool w_pool s p'\
    )
    exit()

# write script below this line
h_out = ((h_in +2*p -h_pool)/(s))+1
w_out = ((w_in +2*p -w_pool)/(s))+1
adds = c_in*h_out*w_out*(h_pool*w_pool - 1)
divs = c_in*h_out*w_out
muls = 0 #there are no multiplications performed in an average pooling operation
c_out = c_in #output channels remain the same as the input channels because pooling does not change the depth of the feature map

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed