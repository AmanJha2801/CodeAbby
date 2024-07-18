input_list = '''7 3 5
15 20 40
300 550 137'''

#split the list from string into integer
lst = list(map(int, input_list.split()))
def find_median_elements(lst):
	result = []
	for i in range(0, len(lst), 3): # the variable i will iterate the list in steps of 3
		sublist = lst[i:i+3] #a sublist is created for the first 3 elements when i=0
		print(sublist)
		sublist.sort() #that sublist of 3 elements is sorted
		print(sublist)
		middle_index = len(sublist) // 2 #from that sorted sublist, the middle element is taken out
		print(middle_index)
		result.append(sublist[middle_index]) #the middle element is appended into a final list to print
	return ' '.join(map(str,result)) #formatting the list for desired output


print(find_median_elements(lst))  # [5, 20, 300]
