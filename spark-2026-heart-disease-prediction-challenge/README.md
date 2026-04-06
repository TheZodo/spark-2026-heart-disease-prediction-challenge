Overview
SPARK 2026 | Chest X-Ray Pneumonia Classification Challenge
Welcome
Welcome to the SPARK Academy 2026 Mini Challenge. This is your team's opportunity to apply the deep learning knowledge built across the Foundation phase to a real medical imaging problem.

You will build a Convolutional Neural Network (CNN) from scratch in PyTorch to classify chest X-ray images as Normal or Pneumonia — the same task that sits at the heart of AI-assisted radiology research worldwide.

Background
Pneumonia kills over 800,000 children under five every year. In Africa, it accounts for nearly 20% of all child deaths under five, yet most hospitals lack the radiologist capacity to review chest X-rays in a timely manner. An AI model that can screen chest X-rays for pneumonia could serve as a frontline triage tool, flagging high-risk cases for urgent review in resource-limited settings.

This mini challenge, you will build that tool.

The Dataset
The competition data is derived from the Chest X-Ray Images (Pneumonia) dataset published alongside a landmark Cell paper by Kermany et al. (2018). It contains anterior-posterior chest X-ray images from pediatric patients collected at Guangzhou Women and Children's Medical Center, Guangzhou, China.

The images have been renamed using the SPARK standard naming convention and split into train, validation, and test sets. Your task is binary classification:

0 — Normal
1 — Pneumonia present
Goal
Build a CNN from scratch in PyTorch that classifies chest X-ray images as Normal or Pneumonia. Your model will be evaluated on a hidden test set using macro-averaged F1-Score. The team with the highest F1-Score on the leaderboard wins.

Deliverables
Each team must submit:

A valid .csv prediction file via Kaggle (format: id, target)
A fully executed Jupyter notebook emailed to the official SPARK Academy email address
A one-page PDF summary emailed alongside the notebook, containing your team name, names of participating members and their roles, a description of your CNN architecture and training strategy, and your best leaderboard F1-Score
Dataset Citation
Kermany, D., Goldbaum, M., Cai, W. et al. (2018). Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning. Cell, 172(5), 1122-1131. https://doi.org/10.1016/j.cell.2018.02.010

Prepared by: SPARK Academy 2026

Start

2 days ago
Close

4 days to go
Description
About This Mini Challenge
This mini challenge is part of the SPARK Academy 2026 Mini Challenge Series, designed for participants to apply the deep learning knowledge built during the Foundation phase to a real medical imaging dataset. Teams will design, train, and evaluate a CNN built from scratch in PyTorch to classify chest X-rays as Normal or Pneumonia.

The Clinical Problem
Pneumonia is one of the leading causes of death in children under five, particularly across Sub-Saharan Africa. The diagnosis is made from a chest X-ray, but in most African hospitals the ratio of patients to radiologists makes timely review impossible.

A reliable CNN that can screen chest X-rays for pneumonia could serve as a triage tool, flagging high-risk cases for urgent review. This is exactly what you will build.

The Data
The dataset comes from the Chest X-Ray Images (Pneumonia) dataset published alongside a Cell paper by Kermany et al. (2018). It contains anterior-posterior chest X-ray images from pediatric patients aged one to five years, collected at Guangzhou Women and Children's Medical Center, Guangzhou, China.

Images have been renamed using the SPARK standard naming convention (CXR_00001.jpeg, CXR_00002.jpeg, …) and reorganised into train, validation, and test sets.

Split Folder Structure Label Information
Train train/NORMAL/, train/PNEUMONIA/ Labels in folder names and train.csv
Val val/NORMAL/, val/PNEUMONIA/ Labels in folder names and val.csv
Test test/ (flat) No label folders, no labels in test.csv
Class Label Description
Normal 0 Clear lungs, no signs of infection
Pneumonia 1 Consolidation or infiltrates visible
The dataset is imbalanced — there are significantly more Pneumonia images than Normal. This is clinically realistic and must be addressed in your training strategy.

Your Approach
This is a supervised binary image classification problem. You are provided with labelled training and validation sets and asked to predict the target for a hidden test set. The test set is held out and used exclusively for leaderboard scoring — it will not be released at any point.

You must build your CNN entirely from scratch using PyTorch. Pre-trained models and transfer learning are not permitted.

Your pipeline should cover:

Image loading and preprocessing (resize, normalise)
Data augmentation to improve generalisation
A CNN architecture defined from scratch using torch.nn
A training loop with loss and accuracy tracked per epoch
Validation during training to monitor generalisation
Evaluation on the validation set using F1-Score, confusion matrix, and AUC-ROC
Prediction generation on the test set
Suggested PyTorch components include nn.Conv2d, nn.MaxPool2d, nn.BatchNorm2d, nn.ReLU, nn.Linear, nn.Dropout, and nn.BCEWithLogitsLoss or nn.CrossEntropyLoss.

Evaluation Metric
Submissions are evaluated using macro-averaged F1-Score:

The macro average treats both classes equally. Because the dataset is imbalanced, a model that always predicts Pneumonia will achieve poor scores on the Normal class and therefore a low macro F1. Your model must perform well on both classes to rank highly.

What to Submit

1. Kaggle prediction file A .csv file with two columns: id and target. One row per image in test.csv. See sample_submission.csv for the exact format.

2. Jupyter Notebook A clean, fully executed notebook emailed to the official SPARK Academy email address. All cells must run top-to-bottom without errors. Markdown commentary must explain your architecture choices, training decisions, and results.

3. One-Page PDF Summary Team name, names of participating members and their roles, a brief description of your CNN architecture and training strategy, and your best leaderboard F1-Score. Emailed alongside the notebook.

Dataset Citation
Kermany, D., Goldbaum, M., Cai, W. et al. (2018). Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning. Cell, 172(5), 1122-1131. https://doi.org/10.1016/j.cell.2018.02.010

Prepared by: SPARK Academy 2026

Evaluation
Submissions are evaluated on the macro-averaged F1-Score between the predicted class labels and the observed targets in the hidden test set.

The macro average computes the F1-Score independently for each class and takes the unweighted mean, ensuring both classes contribute equally regardless of class frequency.

The dataset is imbalanced, with significantly more Pneumonia images than Normal. A model that predicts 1 for every image will achieve a poor score on class 0. Your CNN must perform well on both classes to rank highly.

Submission File
For each id in the test set, you must predict a binary label for the target variable, where 0 indicates Normal and 1 indicates Pneumonia present.

The file should contain a header and have the following format:

id,target
CXR_04981,0
CXR_04982,1
CXR_04983,1
etc.
