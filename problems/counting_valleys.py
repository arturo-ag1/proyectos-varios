#!bin/python3

# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
# During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step.
# Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude.

# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
# For example, if Gary's path is s = [DDUUUUDD] , he first enters a valley  units deep.
# Then he climbs out an up onto a mountain  units high.
# Finally, he returns to sea level and ends his hike.

path = "UDDDUDUU"

# Way 1 - Iterate over the string to count the valleys
# First we have to check if the next character is the same as the actual
# and it has to be a D (down)
#
# then, if the character two positions from the actual is not a D, we know
# it's a two level valley.
#
# if it is, we check for the next index that is not going to be a D, and we
# set the index there, to keep checking.
def getValleys(numberSteps,path):

	# variable that's going to be returned
	numberOfValleys = 0

	# index, just to iterate the word
	index = 0;

	# I decided to use a while loop because I needed to jump some indexes, and the for loop
	# didn't allow me that
	#
	# Iteration of the string:
	while index < len(path)-1:

		# If the next character is a D and the actual character is also a D
		if path[index] == path[index+1] and path[index] == "D":

			# Of tje cjatacyer two positions from the actual index is also a D
			# we keep iterating the string to know where the valley ends, then
			# we continue from there. We also add 1 to the numberOfValleys variable
			if path[index+2] == "D":
				tmpIndex = index+1;
				checking = True;
				while checking:
					tmpIndex+=1;
					if tmpIndex <= len(path)-1:
						if path[tmpIndex] == path[index+1]:
							numberOfValleys+=1
						else:
							index = tmpIndex + 1;
							checking = False
					else:
						index = tmpIndex
						checking = False

			# If the character two positions from the actual index is not a D
			# we just add 1 to the numberOfValleys variable, because it's a two
			# level alley.
			else:
				numberOfValleys+=1
				index+=1
		else:
			index+=1



	return numberOfValleys;

numberOfValleys = getValleys(len(path),path)

print("Counting Valleys: \nFrom:")
print(path)
print("-----------\nTo:")
print(numberOfValleys)
