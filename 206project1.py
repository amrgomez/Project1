import os
import filecmp
import csv
import operator

def getData(file):
	with open(file,'r') as m_csv:
	#Input: file nam
		r=csv.DictReader(m_csv)
		#header=next(r)
		l=[]

		for i in r:
			d={}
			#Create keys for "first","last", and "email"
			d['First']= i['First']
			d['Last']= i['Last']
			d['Email']= i['Email']
			d['Class']= i['Class']
			d['DOB']= i["DOB"]
			l.append(d.copy())
			#print(l)
		return(l)





#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.


#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
	f= sorted(data, key= lambda x: x[col])
#Output: Return a string of the form firstName lastName
	return (f[0]["First"]+ " " +f[0]["Last"])





#Create a histogram
def classSizes(data):
# Input: list of dictionaries
	c= {"Senior":0, "Junior":0, "Sophomore":0, "Freshman":0}
	for d in data:
		c[d["Class"]]+=1
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	#Your code here:
	classlist= list(c.items())
	classlist= sorted(classlist, key= lambda x: x[1], reverse= True)
	return classlist





# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
	dob={}
	l= []
	for x in a:
		y= x["DOB"]
		p= y.split('/')
		h= p[1]
		if h not in dob:
			dob[h]=1
		else:
			dob[h]+= 1
	for p in dob.keys():
		db=(p, dob[p])
		l.append(db)
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	f= sorted(l,key= lambda j: j[1], reverse= True)
	return int(f[0][0])




# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
	d= {}
	s=0
	for x in a:
		y= x["DOB"]
		h= y.split('/')
		s+=2017-int(h[2])
	avg= (round(s/(len(a))))
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB to find their current age.
	return avg

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
	f= sorted(a, key= lambda x: x[col])
	o_csv= open(fileName,'w')
# output each of the rows:
	for y in range(len(f)):
		h= (f[y]["First"]+ "," +f[y]["Last"]+ "," +f[y]['Email']+ ","+ f[y]['Class']+ ","+f[y]["DOB"]+ '\n')
		o_csv.write(h)
	o_csv.close()
	return None





################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
