# <div align="center">Litter Detection with Yolov8</div>
![demo](https://github.com/jeremy-rico/litter-detection/raw/master/assets/litter-detection.gif)
     
## Summary

This is a demo for detecting trash/litter objects with Ultralytics YOLOv8 and the Trash Annotations in Contect (TACO) dataset created by Pedro Procenca and Pedro Simoes. Included is a infer and train script for you to do similar experiments to what I did. There are also the results and weights of various training runs in runs/detect/train for you to experiment with or use as pretrained weights.

## INFERENCE

1. Create python or conda vitrual environment

     conda create -n yolov8 -python=3.7 pytorch=1.7

     conda activate yolov8

2. Install ultralytics yolov8

     python3 -m pip install ultralytics

3. Run infer script

     python3 infer.py src=path/to/your/test/data

See the ultralytics documentation on yolov8 for more information
https://docs.ultralytics.com/

## TRAINING

1. Download TACO dataset:
https://github.com/pedropro/TACO

Note: You can add more annotated data if you'd like. Just ensure labels are in proper YOLO format

2. Format the dataset

Organize the data into the directory structure below

     ├── yolov8
          └── train
               └── images (folder including all training images)
               └── labels (folder including all training labels)
          └── test
                └── images (folder including all testing images)
                └── labels (folder including all testing labels)
          └── valid
               └── images (folder including all testing images)
               └── labels (folder including all testing labels)

3. Create custom data yaml. 
I've provided the one I created for TACO. You will need to change the path at the top to your local TACO directory. It should look something like this:

custom_data.yaml:

     path:  (dataset directory path)
     train: (Complete path to dataset train folder)
     test: (Complete path to dataset test folder) 
     valid: (Complete path to dataset valid folder)

     #Classes
     nc: # replace according to your number of classes

     #classes names
     #replace all class names list with your classes names
     names: ['put', 'classes', 'here']

4. Run train.py
     python3 train.py

## Sources

Ultralytics Yolov8:

https://github.com/ultralytics/ultralytics

Trash Annotations in Context (TACO):

https://github.com/pedropro/TACO

http://tacodataset.org/
