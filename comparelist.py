# we are creating a program that compares two lists and prints a message depending on if the inputs are identical or not

def comparelist():
	if list1 == list2:
		print "The lists are the same"
# if both lists are identical, print "The lists are the same"
	else:
		print "The lists are not the same"
# if both lists are not identical, print "The lists are not the same"

list1 = [1,2,5,6,2]
list2 = [1,2,5,6,2]
comparelist()

list1 = [1,2,5,6,5]
list2 = [1,2,5,6,5,3]
comparelist()

list1 = [1,2,5,6,5,16]
list2 = [1,2,5,6,5]
comparelist()

list1 = ['celery','cauliflower','tomatoes','cashewmilk']
list2 = ['celery','cauliflower','tomatoes','coconutcream']
comparelist()
