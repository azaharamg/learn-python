user_weight = input("Write the weight of a package to determine the cheapest way to ship that package using Sal’s Shippers.")
weight = int(user_weight)

# Ground Shipping
cost_ground = 0.00
flat_charge = 20.00

if weight <= 2:
  cost_ground = 1.50 * weight + flat_charge
elif weight > 2 and weight <= 6:
   cost_ground = 3.00 * weight + flat_charge
elif weight > 6 and weight <= 10:
   cost_ground = 4.00 * weight + flat_charge
elif weight > 10:
   cost_ground = 4.75 * weight + flat_charge

print("Ground Shipping for package of" + " " + str(weight) + "lb, the cost is" + " " + str(cost_ground) + "$.")

# Ground Shipping Premium
cost_premium = 0.00
flat_charge = 125.00
cost_premium =  flat_charge

print("Ground Shipping Premium for package with any weight the cost is" + " " + str(cost_premium) + "$.")

# Drone Shipping
cost_drone = 0.00
flat_charge = 0.00

if weight <= 2:
  cost_drone = 4.50 * weight + flat_charge
elif weight > 2 and weight <= 6:
   cost_drone = 9.00 * weight + flat_charge
elif weight > 6 and weight <= 10:
   cost_drone = 12.00 * weight + flat_charge
elif weight > 10:
   cost_drone = 14.25 * weight + flat_charge

print("Drone Shipping for package of" + " " + str(weight) + "lb, the cost is" + " " + str(cost_drone) + "$.")
