import argparse

import torch
import json

from Trainer import Trainer

parser = argparse.ArgumentParser(description="Train and test the CLIPxRSVQA model.")
parser.add_argument("--dataset", metavar="dataset", type=str,
                    help="name of the dataset: RSVQA-LR, RSVQA-HR, RSVQAxBEN", required=True)
parser.add_argument("--epochs", metavar="epochs", type=int, help="maximum number of epochs during training", default=25)
parser.add_argument("--patience", metavar="patience", type=int,
                    help="patience for the training loop. If 0, patience is ignored", default=3)
parser.add_argument("--batch", metavar="batchSize", type=int, help="batch size to be used during training", default=120)
parser.add_argument("--resized", metavar="resized", type=bool, help="use resized dataset images", default=False)
parser.add_argument("--model", metavar="model_path", type=str, help=".pth file to be loaded", default=None)

args = parser.parse_args()
args = {"limit_epochs": args.epochs,
        "batch_size": args.batch,
        "patience": args.patience,
        "use_resized_images": args.resized,
        "dataset_name": args.dataset,
        "load_model": True if args.model != None else False,
        "model_path": args.model}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

args["device"] = device

trainer = Trainer(**args)
print("Trainer is ready.")

print("Starting testing session...")
print(trainer.test())
