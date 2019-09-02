import pulp as plp

# Start with creating a problem instance
lp_prob = plp.LpProblem(name = "transportationProblem", plp.LpMinimize)

# Supply
w1 = 8
w2 = 6
w3 = 3
total_supply = w1 + w2 + w3

# Demand
s1 = 4
s2 = 2
s3 = 3
dummy_demand = 8
total_demand = s1 + s2 + s3

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
item_quantity = plp.LpVariable.dicts("item_quatity", list(range(1, 13)), lowBound = 0, cat = "Integer")

