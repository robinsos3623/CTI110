# This project is a repetative structure in Python
# 07-06-2020
# CTI-110 P4T2- Bug Collector
# Sinclair Robinson

# This program will demonstrate a nestred loop design.

for row in range( 6 ):
    print( "#", end="", sep="" )
    for spaces in range( row):
        print( " ", end="", sep="" )
    print( "#" , sep="" )
