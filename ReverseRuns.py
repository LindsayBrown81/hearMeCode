from pprint import pformat, pprint   # Pretty print output

with open('runs.txt', 'r') as runs_file:
	runs = runs_file.read().split('\n') #saves the list into the variable runs. And yes! like csv, it split the runs text pasted from notepad at new line
		
	runs.reverse();
	print runs

	#print each list item as a string formatted by each item on a new line
	# for run in runs:
	# 	print "{0}\n".format(run)

# Instead of just printing, save to new file:
with open('reversed.txt', 'w') as reversed_file:
	for run in runs:
		reversed_file.write('{0}\n'.format(run))



# for index, run in enumerate(runs): #enumerating resulted in each list item becoming its own list. No.
	# 	runs[index] = run.split(",")
	# print runs 



