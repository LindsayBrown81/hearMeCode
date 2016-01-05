from pprint import pformat, pprint   # Pretty print output

with open('Change S to FL_12-31-15.txt', 'r') as StoFLs_file:
	StoFLs = StoFLs_file.read().split('\n') #saves the list into the variable. And yes! like csv, it split them text pasted from notepad at new line
		
	
# Instead of just printing, save to new file:
with open('CorrectedFLs2.txt', 'w') as CorrectedFLs_file:
	for StoFL in StoFLs:
		#print each list item as a string formatted by each item on a new line
		print "{0}\n".format(StoFL)
		StoFL = StoFL.replace('S','FL')
		CorrectedFLs_file.write('{0}\n'.format(StoFL))


# for index, run in enumerate(runs): #enumerating resulted in each list item becoming its own list. No.
	# 	runs[index] = run.split(",")
	# print runs 



