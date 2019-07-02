from constraint import *

problem = Problem()
for i in range(16):
    problem.addVariable('k{}'.format(i), range(10 + 26))

problem.addConstraint(lambda a, b:    (a + b) % 36      == 14, ('k0',  'k1'))
problem.addConstraint(lambda a, b:    (a + b) % 36      == 24, ('k2',  'k3'))
problem.addConstraint(lambda a, b:    (b - a + 36) % 36 == 6,  ('k0',  'k2'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 4,  ('k1',  'k3',  'k5'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 13, ('k2',  'k4',  'k6'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 22, ('k3',  'k4',  'k5'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 31, ('k6',  'k8',  'k10'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 7,  ('k1',  'k4',  'k7'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 20, ('k9',  'k12', 'k15'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 12, ('k13', 'k14', 'k15'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 27, ('k8',  'k9',  'k10'))
problem.addConstraint(lambda a, b, c: (a +b +c) % 36    == 23, ('k7',  'k12', 'k13'))

solution = problem.getSolution()

key = ''

for i in range(16):
    if solution['k{}'.format(i)] < 10:
        key += str(solution['k{}'.format(i)])
    else:
         key += chr(solution['k{}'.format(i)] - 10 + ord('A'))

print(key)