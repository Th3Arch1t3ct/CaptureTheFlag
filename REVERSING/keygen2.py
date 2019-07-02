from constrain import *

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

problem = Problem()
for i in range(16):
    problem.addVariable('k{}'.format(i))