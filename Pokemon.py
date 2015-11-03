# Pokemon Name-Stat mining
# Toy hypothesis for Keiba competition
# 2015-10-30 11:42 v0.0
# Author: HoangNT


# Naming:
## pid: Pokemon Id: Integer value
##

# Imports


# Class Pokemon to store a Pokemon's name matrix and total stat.
# The name matrix of a Pokemon will be a 5x1
# Input: pid = INT Pokemon ID
#        name = Name Matrix 80x5
#        stat = INT Pokemon total base
class Pokemon:
    def __init__(self, pid, name, stat=0):
        self.pid = pid
        self.name = name[:]
        self.stat = stat


