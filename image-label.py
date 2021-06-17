import cv2
import json
import os
import sys
import typing

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
# - Add a command-line interface
# - Set up a new git feature branch for Wando to dev on
#   - We will use pull-requests and be all proper about it

        
def read_dictionary(labels_file: str) -> dict:
    if os.path.exists(labels_file):
	    with open(labels_file, "r") as x:
		    return json.load(x)
    else:
        return {
            "smoke"    : [],
            "no_smoke" : []
        }

def write_dictionary(labels_file: str, labels: dict) -> None:
    with open(labels_file, "w") as f:
        json.dump(labels, f)


def label(image_directory: str, labels: dict) -> dict:

    def image_names() -> typing.List[str]:
        return os.listdir(image_directory)

    def already_labelled(image_name: str) -> bool:
        return image_name in labels["no_smoke"] or image_name in labels["smoke"]

    for image_name in image_names():
        if already_labelled(image_name):
            print("Already labelled: {}".format(image_name))
            continue
        full_path = os.path.join(image_directory, image_name)
        image = cv2.imread(full_path)
        cv2.imshow("pic", image) 
        k = cv2.waitKey(0)
        if k == ord("y"):
            labels["smoke"].append(image_name)
        elif k == ord("n"):
            labels["no_smoke"].append(image_name)
    return labels

		
def main() -> int:
    
    labels = read_dictionary("dictionary.json")

    labels = label(image_directory="pics", labels=labels)

    write_dictionary('dictionary.json', labels=labels)
    
    return 0



if __name__ == "__main__":
    sys.exit(main())
    
