Dataset Description
The dataset is derived from the UCI Heart Disease Dataset, combining patient records from four medical institutions across three countries. Your task is to predict whether a patient has heart disease based on their clinical measurements.

Files
train.csv - the training set. Contains 690 patient records with clinical features and the target label. Use this to build and validate your model.
test.csv - the test set. Contains 230 patient records with clinical features only. No target label is provided. Generate predictions for these patients and submit via Kaggle.
sample_submission.csv - a sample submission file in the correct format. Contains the id of every patient in test.csv with a placeholder target of 0. Replace the target column with your predictions before submitting.
Columns
id - unique identifier for each patient record
age - age of the patient in years
sex - biological sex of the patient (Male, Female)
cp - chest pain type (typical angina, atypical angina, non-anginal, asymptomatic)
trestbps - resting blood pressure on hospital admission, in mmHg
chol - serum cholesterol in mg/dl
fbs - whether fasting blood sugar is greater than 120 mg/dl (True, False)
restecg - resting electrocardiographic results (normal, stt abnormality, lv hypertrophy)
thalach - maximum heart rate achieved during exercise
exang - exercise-induced angina (True, False)
oldpeak - ST depression induced by exercise relative to rest
slope - slope of the peak exercise ST segment (upsloping, flat, downsloping)
ca - number of major vessels coloured by fluoroscopy (0, 1, 2, 3); may contain missing values
thal - thalassemia type (normal, fixed defect, reversible defect); may contain missing values
origin - study site where the patient record was collected (Cleveland, Hungary, Switzerland, VA Long Beach)
target - the variable you are predicting. 0 indicates no heart disease; 1 indicates heart disease present (train.csv only)
Acronyms and Clinical Terms
ECG / restecg - electrocardiogram, a recording of the electrical activity of the heart
ST depression / oldpeak - a change in the ECG waveform during exercise, associated with reduced blood flow to the heart
ST segment / slope - a segment of the ECG waveform; its slope during peak exercise is a marker of cardiac stress
Angina / exang - chest pain or discomfort caused by reduced blood flow to the heart muscle
Thalassemia / thal - a blood disorder; a reversible defect on a nuclear scan suggests ischaemia (reduced blood supply)
Fluoroscopy / ca - an imaging technique used to visualise blood vessels; the number of major vessels coloured indicates the extent of blockage
fbs - fasting blood sugar; elevated levels are associated with diabetes, a major cardiovascular risk factor
Notes
ca and thal contain a small number of missing values (NaN). You must decide how to handle them as part of your preprocessing. Median imputation, mode imputation, and row removal are all valid strategies. Document your choice in your notebook.
The id column is a unique identifier only and must not be used as a predictive feature.
The origin column indicates the study site and may be used as a feature if you judge it clinically relevant.
