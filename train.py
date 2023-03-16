import argparse
from ultralytics import YOLO

#for gpu accelration
#os.environ['CUDA_VISIBLE_DEVICES']='0'

parser = argparse.ArgumentParser(description="Yolov8 training and validation script")
parser.add_argument(
    "--model_name",
    default="yolov8s",
    help="Name you'd like to give your model"
)
parser.add_argument(
    "--epochs",
    default=100,
    help="number of epochs to train the model"
    )

if __name__ == "__main__":
    args = parser.parse_args()
    
    model = YOLO(args.model_name+'.pt')

    # Use the model
    model.train(data="./TACO.yaml",
                epochs=args.epochs,
                patience=25,
                imgsz=640,
                device=0,
                name=f"{args.model_name}_{args.epochs}epochs",
                pretrained=True,
                optimizer='SGD',
                )

    metrics = model.val()

