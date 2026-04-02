# MedAI-Zambia Team Task Plan

This file breaks the challenge work into five practical sub-tasks so the team can move from data exploration to final submission.

## Task Summary Table

| Task | Focus | Short Deliverables |
| --- | --- | --- |
| 1. Data Audit And Preprocessing Setup | Clean and prepare the training data | Missing-value review, feature handling plan, reusable preprocessing pipeline, `id` removed from features |
| 2. Baseline Modeling And Validation | Compare permitted baseline models | Baseline experiments, validation approach, macro F1 comparison table, shortlisted models |
| 3. Final Model Selection And Submission File | Produce the best Kaggle-ready predictions | Final tuned model, full-train fit, `test.csv` predictions, valid `id,target` submission file |
| 4. Notebook Finalization And Reproducibility | Prepare the required notebook deliverable | Fully executed notebook, team header, markdown explanations, citations, fixed seeds |
| 5. One-Page Summary And Final Submission Check | Package and verify all final outputs | One-page PDF, folder placement check, Kaggle submission check, final compliance review |

## Shared Rules To Respect

- Use only the provided competition data.
- Do not use `id` as a predictive feature.
- Do not use the test set for training, validation, or tuning.
- Use reproducible code with `random_state=42` where applicable.
- Stay within permitted tools: standard Python data science stack and explicit code-written models only.
- Optimize for macro F1-score, not accuracy.
- Keep in mind the Kaggle limit of 3 submissions per day.

## Sub-Tasks

### 1. Data Audit And Preprocessing Setup

**Suggested owner:** Team Member 1
**Goal:** Build a clean, reproducible preprocessing pipeline from `train.csv`.

**Deliverables**

- Review feature types, missing values, class balance, and obvious outliers.
- Document how categorical and numeric columns will be handled.
- Create a preprocessing workflow that can be applied consistently to train and test data.
- Confirm that `id` is excluded from modeling.

**Definition of done**

- Clear summary of data quality findings.
- Final list of features used for modeling.
- Reusable preprocessing code ready for the notebook.

### 2. Baseline Modeling And Validation

**Suggested owner:** Team Member 2
**Goal:** Establish strong baseline models using only the training data.

**Deliverables**

- Train baseline models such as Logistic Regression, Decision Tree, KNN, SVM, Random Forest, or Gradient Boosting.
- Use a defensible validation strategy on the training set only.
- Compare models using macro F1-score.
- Record the strengths and weaknesses of each approach.

**Definition of done**

- A short comparison table of model performance.
- One or two leading candidate models selected for final tuning.

### 3. Final Model Selection And Submission File

**Suggested owner:** Team Member 3
**Goal:** Produce the best submission-ready predictions for Kaggle.

**Deliverables**

- Tune the final shortlisted model(s) with explicit code.
- Retrain the chosen model on the full training data.
- Generate predictions for `test.csv`.
- Export a valid submission file in the required format: `id,target`.

**Definition of done**

- Submission file matches `sample_submission.csv` structure.
- Final local pipeline can regenerate the exact file.
- Kaggle submission order is planned to stay within the daily limit.

### 4. Notebook Finalization And Reproducibility

**Suggested owner:** Team Member 4
**Goal:** Prepare the required notebook for GitHub Classroom submission.

**Deliverables**

- Build a clean Jupyter notebook that runs top-to-bottom without errors.
- Add a header cell with team name and member names.
- Add markdown explanations for major decisions, preprocessing, model choice, and evaluation.
- Credit the UCI heart disease dataset authors.
- Ensure all seeds and model settings needed for reproducibility are fixed.

**Definition of done**

- Notebook is fully executed and clean.
- Another team member can rerun it successfully.
- The final submission file can be reproduced from the notebook.

### 5. One-Page Summary And Final Submission Check

**Lead:** Team Captain
**Goal:** Package the final materials and complete submission without avoidable mistakes.

**Deliverables**

- Prepare the one-page PDF summary with team name, members, roles, approach, preprocessing choices, model used, and best leaderboard macro F1-score.
- Verify the notebook and PDF are placed under `submissions/hackathon_week1/`.
- Confirm the Kaggle `.csv` submission is valid and submitted before the deadline.
- Check that the final materials comply with all challenge rules.

**Definition of done**

- PDF is complete and concise.
- Notebook, PDF, and Kaggle submission are all aligned.
- Final review confirms no data leakage, no banned tools, and no missing deliverables.

## Working Sequence

1. Finish Task 1 before locking in model experiments.
2. Run Task 2 and Task 4 in parallel once preprocessing is stable.
3. Use Task 3 to generate the best final Kaggle file.
4. Close with Task 5 as a submission checklist.
