import cv2
import os

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
f = open("dictionary.txt", "w")
f.write( str(dictionary) )
f.close()

x = open('dictionary.txt', 'r+')
new_dictionary = dict(x.read() )
x.close()


print("Smoke")
print(yresults)
print("No smoke")
print(nresult)
