bikes_full = ['buell','bullet','bmw','ducati','honda','indian','kawasaki','royal enfield','suzuki','triumph','yamaha']
print(f"We have {len(bikes_full)} bikes in stock")
bikes = bikes_full
print (bikes)
print ("Interesting - list = list is a pointer assignment. Note that both bikes and bikes_full show the same result")
print (bikes.pop())
print (bikes)
bikes.append('yamaha')
print (bikes.pop(4))
print (bikes)
print (bikes_full)
bikes.insert(2,'harley davidson')
print (bikes)
del bikes[4]
print (bikes)
print (bikes_full)
bikes_unsorted = ['indian','kawasaki','royal enfield','buell','honda','suzuki','bullet','bmw','ducati','triumph','yamaha']
print (bikes_unsorted)
print ("bikes_sorted from bikes_unsorted using sort method - it does in place sort of unsorted list")
print ("you cannot assign it - the sort() method is a procedure not a function")
bikes_sorted = bikes_unsorted.sort()
# sort() method permanently sorts your list
# Above sort method works as a procedure and not a function, and in place in the list - like a procedure
# It does the sort in place and does not assign the result to the LHS
# Need to confirm if this is also inconsistent with other dot usage.
print (bikes_sorted)
print ("it sorts the bikes_unsorted in place also:")
print (bikes_unsorted)
print ("bikes_sorted using sorted() from bikes_unsorted:")
bikes_unsorted = ['indian','kawasaki','royal enfield','buell','honda','suzuki','bullet','bmw','ducati','triumph','yamaha']
print(sorted(bikes_unsorted))
print (bikes_unsorted)
bikes_sorted = sorted(bikes_unsorted)
print (bikes_sorted)
print (bikes_unsorted)
print ("bikes_sorted reversed:")
bikes_sorted.reverse()
print (bikes_sorted)
print ("bikes_sorted reversed back to original:")
bikes_sorted.reverse()
print (bikes_sorted)
