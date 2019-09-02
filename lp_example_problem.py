import pulp as plp

# Start with creating a problem instance
lp_prob = plp.LpProblem("transportationProblem", plp.LpMinimize)

# Supply
w1 = 8
w2 = 6
w3 = 3

# Demand
s1 = 4
s2 = 2
s3 = 3
dummy_demand = 8

# Delivery rates from shops to warehouses in USD
# Since there is an 8 unit surplus in supply, 
# We will created a dummy destination for that at USD 0 cost

s1_w1 = 7
s2_w1 = 3
s3_w1 = 4
sd_w1 = 0

s1_w2 = 4
s2_w2 = 2
s3_w2 = 2
sd_w2 = 0

s1_w3 = 2
s2_w3 = 1
s3_w3 = 5
sd_w3 = 0

# Decision variables
# We want the number of items transported from the i-th source
# To the j-th destionation

x = plp.LpVariable.dicts("item_quatity", list(range(1, 13)), lowBound = 0, cat = "Integer")

# Objective Function

lp_prob += (x[1] * s1_w1 + x[2] * s2_w1 + x[3] * s3_w1 + x[4] * sd_w1 
            + x[5] * s1_w2 + x[6] * s2_w2 + x[7] * s2_w3 + x[8] * sd_w2
            + x[9] * s1_w3 + x[10] * s3_w2 + x[11] * s3_w3 + x[12] * sd_w3)

# Constraints
# Supply Constraints

lp_prob += x[1] + x[2] + x[3] + x[4] == w1
lp_prob += x[5] + x[6] + x[7] * x[8] == w2
lp_prob += x[9] + x[10] + x[11] + x[12] == w3

# Demand Constraints

lp_prob += x[1] + x[5] + x[9] == s1
lp_prob += x[2] + x[6] + x[10] == s2
lp_prob += x[3] + x[7] + x[11] == s3
lp_prob += x[4] + x[8] + x[12] == dummy_demand

# Solve

lp_prob.solve()
plp.LpStatus[lp_prob.status]

# Print our decision variable values

print("Items from Warehouse 1 to Store 1 = {}".format(x[1].varValue))
print("Items from Warehouse 1 to Store 2 = {}".format(x[2].varValue))
print("Items from Warehouse 1 to Store 3 = {}".format(x[3].varValue))
print("Items from Warehouse 2 to Store 1 = {}".format(x[5].varValue))
print("Items from Warehouse 2 to Store 2 = {}".format(x[6].varValue))
print("Items from Warehouse 2 to Store 3 = {}".format(x[7].varValue))
print("Items from Warehouse 3 to Store 1 = {}".format(x[9].varValue))
print("Items from Warehouse 3 to Store 2 = {}".format(x[10].varValue))
print("Items from Warehouse 3 to Store 3 = {}".format(x[11].varValue))

# Print our objective function value

print("Total transportation cost is {}".format(plp.value(lp_prob.objective)))