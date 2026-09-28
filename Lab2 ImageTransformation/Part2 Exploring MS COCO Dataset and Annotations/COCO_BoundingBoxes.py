# Part II: Exploring MS COCO Dataset and Annotations
# Practice:
# Write a Python script that takes a folder of images from COCO dataset and json file as parameters of input, draw all the object bounding boxes based on the input json file and save those images in the new folder.
import cv2
import json
import os
import argparse

# ---- Inputs: folder of images, JSON file, and output folder ----
parser = argparse.ArgumentParser()
parser.add_argument("--images", default="val2017")
parser.add_argument("--json", default="instances_val2017.json")
parser.add_argument("--output", default="output_images")
args = parser.parse_args()

image_folder = args.images
json_file = args.json
output_folder = args.output

# ---- Read the JSON annotation file into a Python dictionary ----
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---- Sort the boxes by photo ID: {photo_id: [bbox, bbox, ...]} ----
boxes_by_image = {}
for ann in data["annotations"]:
    img_id = ann["image_id"]
    if img_id not in boxes_by_image:
        boxes_by_image[img_id] = []
    boxes_by_image[img_id].append(ann["bbox"])

# ---- Look up a photo's ID from its filename: {file_name: photo_id} ----
id_by_file_name = {}
for img_info in data["images"]:
    id_by_file_name[img_info["file_name"]] = img_info["id"]

# ---- Create the output folder if it doesn't exist yet ----
os.makedirs(output_folder, exist_ok=True)

# ---- Go through every photo, draw its boxes, and save it ----
for photo_name in os.listdir(image_folder):
    # Skip any file that isn't listed in the JSON
    if photo_name not in id_by_file_name:
        continue

    photo_id = id_by_file_name[photo_name]
    boxes = boxes_by_image.get(photo_id, [])   # empty list if the photo has no boxes

    photo = cv2.imread(os.path.join(image_folder, photo_name))
    if photo is None:
        print("Could not open:", photo_name)
        continue

    # bbox is [x, y, width, height]: convert to top-left and bottom-right corners
    for bbox in boxes:
        x, y, box_w, box_h = bbox
        top_left = (int(x), int(y))
        bottom_right = (int(x + box_w), int(y + box_h))
        cv2.rectangle(photo, top_left, bottom_right, (0, 255, 0), 2)   # green box

    cv2.imwrite(os.path.join(output_folder, photo_name), photo)
    print("Saved:", photo_name, "with", len(boxes), "boxes")