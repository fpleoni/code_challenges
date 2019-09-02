from pulp import *

# Start with creating a problem instance
lp_prob = LpProblem("transportationProblem", LpMinimize)

# Supply
w1 = 8
w2 = 6
w3 = 3

# Demand
s1 = 4
s2 = 2
s3 = 3



