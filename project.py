from mathdojo import MathDojo

# create an instance:
md = MathDojo()

# Write the add method and test it by calling it 3 times, with different numbers of arguments each time
x = md.add(2).add(2, 2).add(2, 2, 2).result
print(x)

# Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time
x = md.subtract(2).subtract(2, 2).subtract(2, 2, 2).result
print(x)

# Make sure you are able to chain methods as demonstrated above
# # to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5








