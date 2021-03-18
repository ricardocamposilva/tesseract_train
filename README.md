# Tesseract Train (intended for train with Ground Truth)

## Introduction
This project is configured tesstrain with all the necessary params to train your ground truth image lines to Tesseract OCR

# Setup
First of create your tessdata dir using: `mkdir -p tesstrain/usr/share/tessdata`
Into data folder you need to create your ground truth directory, this directory have to follow the rules below:
- 1: Let's suppose that you want to call your model as spa_001
- 2: You need to create a folder using your model name + -ground-truth and the result is the follow -> `spa_001-ground-truth`
- 3: This folder has to be created inside data folder: Eg: `mkdir -p tesstrain/data/spa_001-ground-truth`
- 4: Ground Truth files has to be sequential numbers like 001.jpeg, 001.gt.txt (This pair is required)
- 5: Inside data folder you have to create .numbers, .punc, .wordlist with your model name as prefix: Eg: `spa_001.punc`
- 6: If you want to continue from some start model, you have to move the start model traineddata file into `tesstrain/usr/share/tessdata` folder.

## After all set, you have to start your training using
`make training MODEL_NAME=spa_001 PSM=7 START_MODEL=spa`

Where: 
- `MODEL_NAME` is the name of your new model (we used it as `spa_001`)
- `PSM` is the Page Segmentation Mode (7 is for line data)
- `START_MODEL` is the model you want to continue training from (we used standard spa.traineddata from tesseract repositories)
    - You can found initial models in: https://github.com/tesseract-ocr/tessdata_best
