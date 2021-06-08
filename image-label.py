import cv2
import os
import json


## TODO for Wando
# - Run through the code and make sure you understand what it does
#   - leave comments anywhere you can't work out! We will go through them
# - Rename any variables we named too vaguely the first time around. This is a subjective
#   matter, so just use your own judgement here
# - [NEW FEATURE] Implement a way to detect images that have already been labelled, and
#   skip them. i.e. only label images you haven't labelled yet
#   - With this feature, you will be able to continually add new photos to your dataset
#     and not have to re-label all the old ones
#   - We will break this down into more bite-sized chunks:

## TODO for Wando + Hamish
# - Segment this program into distinct groups using functions or comment blocks
# - Read files using `with ...`
# - Add a command-line interface
# - Set up a new git feature branch for Wando to dev on
#   - We will use pull-requests and be all proper about it


# "contents" is a bit vague, something more descriptive would be better.
#
# I at least partialy named this variable iirc, sorry to make you do it again :P
#
# When choosing variable names, think about what will make the most sense when you come
# back to this code to edit it later on. Trust me...
#
# e.g. pictureDirectoryContents or picture_directory_contents, whatever you prefer
#                                                                   (just be consistent)
#
# You may feel some of the other variables could be better named too, so have a look at
# all the variables in this program and apply the above thought process. Your future self
# will thank you
contents = os.listdir("pics")


yresults = []
nresults = []

for img in contents:
    path = os.path.join("pics", img)
    image = cv2.imread(path)
    cv2.imshow("pic", image) 
    k = cv2.waitKey(0)
    if k == ord("y"):
        yresults.append(img)
        print("Y pressed")
    elif k == ord("n"):
        nresults.append(img)
        print("N pressed")

dictionary = {
    "Smoke":yresults,
    "No smoke":nresults
}

# f = open("dictionary.txt", "w")
# f.write( str(dictionary) )
# f.close()
def writeDictionary():
    with open("dictionary.txt", "w") as f:
        json.dump(dictionary, f) 
        
writeDictionary()

def readDictionary():
	with open("dictionary.txt", "r+") as x:
		return json.load(x)
		
		
validation_dict = readDictionary()

#x = open('dictionary.txt', 'r+')
#new_dictionary = dict(x.read() )
#x.close()


#print("Smoke")
#print(yresults)
#print("No smoke")
#print(nresults)

print(dictionary)
print(validation_dict)