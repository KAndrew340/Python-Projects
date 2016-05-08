# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:26:04 2015

@author: Kem
@date -  11/29/2015
@description - This program reads binder and ingredient data from
			   a text file. The program then calculates recipe costs
			   and displayswhich recipes can be madeusing the ingredients
			   that were read.

@resources -
"""

print "\nKem Andrew"
print "Contemporary Programming Languages"
print "12/02/2015"
print "Dr. Stringfellow\n"

#holds the name of the binder
bindername = []

#holds ingredients and cost
ingredients = {}

#holds info for each binder
info = []

# holds the names of each recipe
recipenames = []

# total for each recipe
totals = []

#total number of recipe in each binder
num_recipes_in_binder = []

#Chef Puck's budget
budget = []

#Output data
outputlist = []

# Loop counters
counter = 0
counter1 = 0
ct = 0

#grandtotal of each recipe
grandtotal = 0

# reads the file
try:
    data = open("C:\Users\Kem\SkyDrive\Code\Python\prog5Assignment\in2.txt", "r")
    #print "Name of file: ", data.name
except IOError:
    print "Cannot open file."
    import sys
    sys.exit(0)

# Displaying binder info : 
print "DISPLAYING BINDER INFO : " 
	
# first item in file
numbinders = int(next(data))
print numbinders

# This loops through each binder
while ct < numbinders:
    #Binder bane
    bindername.append(next(data))
    print "Binder name: ", bindername[ct]
    
    #binder info
    currentline = next(data)
    info = currentline.split()
    print "Binder info: ", info
    
    # budget
    budget.append(int(info[2]))
    print "Budget: ", budget
    
    # number of recipes
    numrecipes = int(info[1])
    print "Num recipes: ", numrecipes
    
    # This if statement saves the # of recipes ineach binder. Will
    # later be used for processing the display of results
    if ct == 0:
        num_recipes_in_binder.append(numrecipes)
    else:
        num_recipes_in_binder.append(numrecipes)
    
    #This loop reads the base ingredients into a dictionary
    #while counter1 < int(info[1])
    while counter < int(info[0]):
        # Split the current line into a list
        currline = next(data).split()
        
        # Add the list to a dictionary
        print currline
        ingredients[currline[0]] = int(currline[1])
        
        #ingredients.update(currentline.split())
        counter +=1
    print ingredients
    
    # Calculate cost of recipes in binder:
    # this loop goes through each recipe in the binder
    while counter1 < numrecipes:
        counter = 0
        recipename  = next(data)
        recipenames.append(recipename)
        numlines = int(next(data))
        
        # this loop goes through each ingredient in the recipe
        # and calculates the total for each recipe
        while counter < numlines:
            #this variable holds total of each ingredient
            total = 0
            
            #list containing ingredient name and cost N.B. both are strings
            ingrecost = next(data).split()
            
            # these next lines calculates the sum of the individual 
            # ingredients            
            name = ingrecost[0]
            x = ingredients[str(name)]
            total = int(x) * int(ingrecost[1])
            #print "total: ", total
            grandtotal = grandtotal + total
            
            #increment the counter for the amount of ingredients
            counter += 1
        #increment the counter for the # of recipes
        counter1 +=1
        print "Recipe names: ", recipenames
        
        #append total for each recipe to list
        totals.append(grandtotal)
        # reset grandtotal counter
        grandtotal = 0
        
    
    #reset the counters
    counter = 0
    counter1= 0
    
    #increment binder counter
    ct+=1
print totals
print num_recipes_in_binder
print "........finished processing!"
print "...running calculations on data..."
print "..." * 20

# counter variables
ct1 = 0
ct2 = 0

# This loop prints the results of the calculations
for i in range(len(bindername)):
    #ct = i
    print 
    print bindername[i].upper()
    x = int(num_recipes_in_binder[i])
    #print x
    
    while ct1 < x:
        #outputlist.append(tuple)
        if budget[i] < totals[ct2]:
            print (recipenames[ct2] + " Total: $" + str(totals[ct2]))
            print "Too expensive!"
        else:
            print (recipenames[ct2] + " Total: $" + str(totals[ct2]))
        ct1+=1
        ct2+=1
    ct1 = 0
    #for a in range(x):
        #print (recipenames[a] + " Total: " + str(totals[a]))
		
print "\n...Program run successfully!"
