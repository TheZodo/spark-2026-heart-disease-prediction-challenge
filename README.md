# spark-2026-heart-disease-prediction-challenge
Build a diagnostic classifier from real patient data, and help close Africa's cardiovascular care gap
Overview
ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.
The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted.

You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.

1. COMPETITION-SPECIFIC TERMS
1. COMPETITION TITLE
SPARK 2026 | Heart Disease Prediction Challenge

2. COMPETITION SPONSOR
SPARK Academy 2026, operated under CAMERA (Consortium for Advancement of MRI Education and Research in Africa)

3. COMPETITION SPONSOR ADDRESS
SPARK Academy 2026

4. COMPETITION WEBSITE
https://www.kaggle.com/competitions/spark-2026-heart-disease-prediction

5. TOTAL PRIZES AVAILABLE
No monetary prizes are offered for this competition. This is an internal academic competition. Rankings and performance will be recorded as part of the SPARK Academy 2026 Hackathon Phase evaluation.

6. WINNER LICENSE TYPE
Non-Exclusive. Winners hereby grant to the Competition Sponsor a worldwide, non-exclusive, sub-licensable, transferable, fully paid-up, royalty-free, perpetual, irrevocable right to use, reproduce, distribute, and create derivative works of the winning Submission and the source code used to generate it, for educational and research purposes, without further approval by or payment to the winner.

7. DATA ACCESS AND USE
Competition Use and Non-Commercial & Academic Research. You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

The dataset is derived from the UCI Heart Disease Dataset. Users of this data must credit the following principal investigators in any publication or public-facing work:

Andras Janosi, M.D., Hungarian Institute of Cardiology, Budapest
William Steinbrunn, M.D., University Hospital, Zurich, Switzerland
Matthias Pfisterer, M.D., University Hospital, Basel, Switzerland
Robert Detrano, M.D., Ph.D., V.A. Medical Center, Long Beach and Cleveland Clinic Foundation
2. COMPETITION-SPECIFIC RULES
1. TEAM LIMITS
a. This is an internal SPARK Academy 2026 competition. Only registered SPARK 2026 participants may enter.

b. Teams are pre-assigned by the SPARK Academy 2026 organisers. Each team competes independently.

2. SUBMISSION LIMITS
a. You may submit a maximum of three (3) Submissions per day.

b. You may select up to two (2) Final Submissions for judging.

3. COMPETITION TIMELINE
Competition Timeline dates, including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, are reflected on the competition's Overview > Timeline page. Participants are responsible for monitoring the timeline. No extensions will be granted.

4. COMPETITION DATA
a. Data Access and Use. You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any Participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.

b. Test Set. The test set is held out and will not be released to participants at any point during or after the competition. It is used exclusively for automated leaderboard scoring. Participants are expected to build and validate their models using the provided training data only.

c. Permitted Tools. Participants may use Python (any version ≥ 3.8) with standard data science libraries including pandas, numpy, matplotlib, seaborn, and scikit-learn. Jupyter Notebook, Google Colab, and Kaggle Notebooks are all permitted environments.

The following are not permitted:

AutoML frameworks (e.g., TPOT, Auto-sklearn, H2O AutoML, Google AutoML)
Deep learning frameworks (e.g., TensorFlow, PyTorch, Keras)
Large Language Models or foundation models of any kind
Any tool that automates model selection or hyperparameter tuning without explicit code written by the participant
d. Suggested Models. This competition is designed for the application of supervised machine learning. Suggested approaches include, but are not limited to, Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, Support Vector Machine, and Gradient Boosting. Participants are free to choose any supervised learning method they judge appropriate. Model choice must be justified in the one-page implementation summary.

e. Data Security. You agree not to transmit, duplicate, publish, redistribute, or otherwise provide the Competition Data to any party not participating in the Competition. You agree to notify the Competition Sponsor immediately upon learning of any possible unauthorised access to the Competition Data.

f. No Data Leakage. The test set must not be used in any way during model training, validation, or hyperparameter tuning. The id column must not be used as a predictive feature. Any submission found to have exploited the test set will be disqualified.

5. WINNER LICENSE
Under Section 2.8 (Winners Obligations) below, you hereby grant to the Competition Sponsor a worldwide, non-exclusive, sub-licensable, transferable, fully paid-up, royalty-free, perpetual, irrevocable right to use, reproduce, distribute, and create derivative works of your winning Submission and the source code used to generate the Submission, for educational and non-commercial research purposes, without further approval by or payment to you.

6. EXTERNAL DATA AND TOOLS
a. You may not use external datasets beyond the Competition Data provided (train.csv).

b. Pre-trained models of any kind are not permitted.

c. You may use publicly available educational resources, textbooks, tutorials, and documentation, to inform your approach, provided you do not directly copy another participant's code or solution.

7. ELIGIBILITY
a. This competition is open exclusively to registered SPARK Academy 2026 participants. Participation is limited to individuals who received an official SPARK 2026 invitation and completed programme registration.

b. SPARK Academy organisers, mentors, and programme staff are not eligible to submit.

c. Participants must be members of a pre-assigned SPARK Academy 2026 team. Individual submissions outside of an assigned team are not accepted.

8. WINNER'S OBLIGATIONS
As a condition of being recognised as a competition winner, the following are required:

a. Kaggle Submission. A valid .csv file submitted via Kaggle in the correct format (id, target) before the Final Submission Deadline. The submission must be generated from a reproducible notebook.

b. Jupyter Notebook. A fully executed, clean Jupyter notebook pushed to GitHub Classroom under submissions/hackathon_week1/ by the Final Submission Deadline. The notebook must:

Run top-to-bottom without errors
Include the team name and member names in the header cell
Contain markdown commentary explaining each major decision
Credit the UCI dataset authors
Fix all random seeds (random_state=42) to ensure reproducibility
c. One-Page Implementation Summary (PDF). Each team must submit a single-page PDF containing:

Team name
Names of team members who actively participated in the project, and their individual role (e.g., data cleaning, modelling, evaluation, write-up)
A concise description of the approach, model(s) used, key preprocessing decisions, and final result
The team's best F1-Score achieved on the leaderboard
The PDF must be pushed to GitHub Classroom alongside the notebook under submissions/hackathon_week1/.

d. Grant of License. Grant to the Competition Sponsor the license described in Section 2.5 above.

9. EVALUATION AND SCORING
Primary Metric: Macro-averaged F1-Score on the held-out test set.

Submissions are scored automatically via the Kaggle leaderboard. The test labels are not released at any point during or after the competition. Final rankings are determined by each team's best selected submission.

In the event of a leaderboard tie, the team whose implementation summary best demonstrates understanding of the clinical problem and modelling decisions will be ranked higher, at the discretion of the SPARK Academy panel.

10. GOVERNING LAW
This competition is administered by SPARK Academy 2026 under CAMERA. All disputes will be resolved by the Programme Manager in consultation with the SPARK Academy leadership team. Participation in this competition constitutes acceptance of the Programme Manager's decisions as final and binding.

Prepared by: SPARK Academy 2026

Start

5 days ago
Close
2 days to go
Description
About This Mini Hackathon
This mini hackathon is part of the SPARK Academy 2026 Hackathon Phase, the competitive arm of the SPARK programme. It is designed for participants to apply the knowledge and skills built across the first six weeks of the Foundation phase to a real-world medical dataset. Teams will explore, clean, and model clinical data to predict the presence of heart disease in patients.

This is not a toy problem. The data is real, the disease is real, and the methods you apply here are the same methods used in clinical decision support research across the world.

The Clinical Problem
Heart disease remains the single largest cause of death globally. In Africa, cardiovascular disease is now the leading non-communicable disease burden, yet diagnostic infrastructure in most settings is limited to basic clinical measurements: blood pressure, a blood test, a simple ECG. The question this challenge asks is straightforward:

Given a patient's routine clinical measurements, can a machine learning model reliably identify whether that patient has heart disease?

A model that answers this question accurately, and generalises across patient populations, could serve as an early-warning screening tool in resource-limited African clinics where specialist cardiologists are unavailable.

The Data
The dataset combines patient records from four institutions across three countries, giving it a multi-site diversity that makes it more representative than single-centre datasets.

Site	Country
Cleveland Clinic Foundation	USA
Hungarian Institute of Cardiology	Hungary
University Hospital Zurich	Switzerland
V.A. Medical Center Long Beach	USA
Each patient record contains 14 clinical features including age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, ECG results, maximum heart rate, exercise-induced angina, and more.

The original dataset recorded heart disease severity on a scale of 0 to 4. For this challenge, the target has been recoded to binary:

0 — No heart disease
1 — Heart disease present (any stage)
Your Approach
This is a supervised binary classification problem. You are provided with a labelled training set (train.csv) and asked to predict the target for an unlabelled test set. The test set is hidden and used exclusively for leaderboard scoring, it will not be released at any point.

Suggested supervised learning methods include, but are not limited to:

Logistic Regression
Decision Tree
Random Forest
K-Nearest Neighbors
Support Vector Machine
Gradient Boosting
You are free to choose whichever model or combination of models you judge best. Your model selection and reasoning must be documented in your notebook and one-page PDF summary.

Evaluation Metric
Submissions are evaluated using macro-averaged F1-Score:



The macro average treats both classes equally, regardless of class frequency. This matters here because the dataset is imbalanced, with approximately 68% of patients having heart disease. A model that simply predicts 1 for every patient would achieve high accuracy but a poor F1-Score. Your model must perform well on both classes to rank highly.

What to Submit
Every team submits three things:

1. Kaggle prediction file A .csv file with two columns: id and target. One row per patient in test.csv. See sample_submission.csv for the exact format.

2. Jupyter Notebook A clean, fully executed notebook pushed to GitHub Classroom under submissions/hackathon_week1/. All cells must run top-to-bottom without errors. Include markdown commentary explaining your decisions at each step.

3. One-Page PDF Summary A single-page PDF containing your team name, the names of participating members and their role in the project, a brief description of your approach, and your best leaderboard F1-Score.

Dataset Citation
Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J., Sandhu, S., Guppy, K., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. American Journal of Cardiology, 64, 304-310.

SPARK Academy 2026

Evaluation
Submissions are evaluated on the macro-averaged F1-Score between the predicted class labels and the observed targets in the hidden test set.

The macro average computes the F1-Score independently for each class and takes the unweighted mean, ensuring that both classes contribute equally to the final score regardless of class frequency.



Note that the dataset is imbalanced, with approximately 68% of patients having heart disease. A model that predicts 1 for every patient will achieve poor scores on class 0. You must build a model that performs well on both classes.

Submission File
For each id in the test set, you must predict a binary label for the target variable, where 0 indicates no heart disease and 1 indicates heart disease present.

The file should contain a header and have the following format:

id,target
587,0
702,1
310,1
etc.
Prepared by: SPARK Academy 2026

Competition Host
SPARK_2025

Prizes & Awards
Kudos

Does not award Points or Medals

Participation
23 Entrants

8 Participants

8 Teams

18 Submissions

Tags
F1 Score
Table of Contents
