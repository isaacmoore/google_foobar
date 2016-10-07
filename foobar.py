# a = [22.2, 46, 100.8]
# b = [23, 11.1, 50.4]

j = [2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002]
k = [23.0, 150.0, 1024.0, 34868.0]

##############
# Submission
##############

def answer(y, x):
	y_sort, x_sort = sorted(y), sorted(x)
	# If the len of y or x is one item, return 0
	if len(y) == 1 or len(x) == 1:
		return 0
	# If the two lists match lengths, perform operations.
	elif len(y_sort) == len(x_sort):
		out_list = [(int(round(100-x_sort[i] / y_sort[i]))) for i in range(len(x_sort))]
		return sum(out_list) / len(out_list)
	# If nothing else matches, return nothing.
	else:
	    return (1-(sum([int(round(time)) for time in x]) / sum([int(round(time)) for time in y]))) * 100


			# return int(sum(test1+test2+test3+test4) / total_len)

# print answer(a, b)
print answer([1.0],[1.0])
print answer(j, k)

# round(2.2222, 1)
# test1 = int(100-(x_sort[0]/y_sort[0]))
# test2 = int(100-(x_sort[1]/y_sort[1]))
# test3 = int(100-(x_sort[2]/y_sort[2]))
# test4 = int(100-(x_sort[3]/y_sort[3]))


###################################
# Online Solution -- Does not work
###################################
j = [2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002]
k = [23.0, 150.0, 1024.0, 34868.0]
def answer(x, y):
	return int(round((1-(sum(y)/sum(x))) * 100))
print answer([1.0],[1.0])
print answer(j, k)

###########################
# Another Online Solution
###########################
j = [2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002]
k = [23.0, 150.0, 1024.0, 34868.0]
def answer(x,y):
    return (1-(sum([int(round(time)) for time in x]) / sum([int(round(time)) for time in y]))) * 100

print answer([1.0],[1.0])
print answer(j, k)
    #improvement =
    # for time in x:
    #     totalTime1 += time
    # for time in y:
    #     totalTime2 += time
