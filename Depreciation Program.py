# Calvin Comstock-Fisher and Natalie Scholz
# 10/26/20
# Depreciation Program

# Depreciation = (Cost-Salvage Value)/Useful Life
asset = input("What is the asset's name? ")

# Step 1: Ask the user for their asset name, salvage value of asset, useful life of asset.
# Step 2: Calculate depreciation using formula.
# Step 3: Print values from step 1 and step 2.
# Step 4: Repeat if user prompts.

while asset != "exit":
  # Step 1: 
  cost = int(input("How much did " +asset+ " cost?\n"))
  salvageValue = int(input("What is the salvage value of " +asset+ "?\n"))
  usefulLife = int(input("What is the useful life of " +asset+ "?\n"))
  # Step 2:
  diffCostSalv = cost - salvageValue
  depreciation = diffCostSalv / usefulLife
  # Step 3: 
  print("{:>0}{:>20}".format("Name:", asset))
  print("{:>0}{:>20}{:<10.2f}".format("Cost:", "$",cost))
  print("{:>0}{:>10}{:<10.2f}".format("Salvage Value", "$",salvageValue))
  print("{:>0}{:>10}".format("Useful Life:", usefulLife))
  print("{:>0}{:>10}{:<10.2f}".format("Depreciation", "$",depreciation))
  # Step 4: 
  asset = input("What is the name of another asset? Type exit to quit. ").lower()
