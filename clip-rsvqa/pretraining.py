import argparse

import torch

from PreTrainer import PreTrainer

parser = argparse.ArgumentParser(description="Pre-train the CLIPxRSVQA model with the NWPU-Captions dataset.")
parser.add_argument("--epochs", metavar="epochs", type=int,
                    help="maximum number of epochs during training", required=True)
parser.add_argument("--patience", metavar="patience", type=int,
                    help="patience for the training loop. If 0, patience is ignored",required=True)
parser.add_argument("--lr_patience", metavar="lr_patience", type=int,
                    help="patience for the learning rate decay. If 0, patience is ignored", required=True)


args = parser.parse_args()
args = {"limit_epochs": args.epochs,
        "patience": args.patience,
        "lr_patience": args.lr_patience}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

args["device"] = device
pretrainer = PreTrainer(**args)
print("Trainer is ready.")
pretrainer.run()
