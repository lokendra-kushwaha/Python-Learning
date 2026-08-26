# 🛠️ Command Line Utility (argparse)

## 📌 Overview
The argparse module is the standard Python library used to build powerful Command Line Interfaces (CLIs). It makes it easy to write user-friendly command-line programs by parsing arguments passed directly from the terminal and automatically generating help and usage messages.

## 🤖 Why is this important for AI/ML Engineers?
While you won't be building web servers, argparse is heavily used in Machine Learning and Deep Learning projects for Hyperparameter Tuning. 

Instead of hardcoding values inside your training script, you use a CLI utility to control parameters directly from the terminal when launching a training job:
python train_model.py --epochs 50 --batch-size 32 --learning-rate 0.001

## 🚀 Core Capabilities
* Positional Arguments: Required inputs that the user must pass (e.g., file paths, experiment names).
* Optional Arguments (Flags): Optional configurations prefixed with double dashes (e.g., --epochs, --learning-rate).
* Booleans (Actions): Toggle flags on/off (e.g., --gpu or --verbose).
* Auto-Generated Help: Automatically creates a built-in help manual when a user types --help.