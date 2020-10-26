# Calvin Comstock-Fisher and Natalie Scholz
# 10/26/2020
# PBS Pledge

# Step 1: Ask if user would like to enter a new pledge.
# Step 2: Ask what the donor's name is.
# Step 3: Ask how much they would like to pledge.
# Step 4: Repeat until user answers that they would not like to enter a new pledge.
# Step 5: Print out number of donors, total pledge, and average pledge.

count = 0
total = 0

# Step 1
newPledge = input("Would you like to enter a new pledge (yes/no)? ").lower()
# Step 4
while newPledge == "yes":
  # Step 2
  name = input("What is the donor's name? ")
  # Step 3
  amount = int(input("How much would " +name+ " like to pledge? "))
  total = total + amount
  count = count + 1
  newPledge = input("Would you like to enter a new pledge (yes/no)? ")

average = total/count

print("\t \nPBS Pledge Summary Report")
# Step 5
print("{:<0}{:>10}".format("Total # of Donors", count))
print("{:<0}{:>10}{:<10.2f}".format("Total Pledges", "$",total))
print("{:<0}{:>10}{:<10.2f}".format("Average Pledge", "$",average))
print("\nThank you for your donation!")