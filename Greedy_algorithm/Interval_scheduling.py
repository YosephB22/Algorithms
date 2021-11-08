def print_shows(show_list):
	"""
	takes a list of show tuples as defined above and prints in order of start time 
	the list of shows that Angusina should attend, as obtained using the algorithm 
	in the lecture notes.
	show_list = (title, start_time, duration)
	"""
	new_list = []
	for value in show_list:
		value = list(value)
		end_time = value[1] + value[2]
		value.append(end_time)
		new_list.append(value)
		new_list.sort(key=lambda x:x[3])
		end_time_cutrrent = new_list[0][3]
		result = [(new_list[0][0], new_list[0][1], new_list[0][3])]
		for i, j in enumerate(new_list, start=1):
			if i == 1:
				pass
			else:
				if end_time_cutrrent <= j[1]:
					end_time_cutrrent = j[3]
					result.append((j[0], j[1], j[3]))
		for final in result:
			print(*final)

# ------------test1---------------------------------
# The example from the lecture notes
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4), 
    ('h', 8, 3)])
# ---------------------------------------------------