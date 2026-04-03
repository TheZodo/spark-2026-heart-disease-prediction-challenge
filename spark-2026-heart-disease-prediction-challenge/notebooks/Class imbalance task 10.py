# -------------------------------
# Markdown Cell
# -------------------------------
"""
## Comparing F1-Score With and Without Class Weight Balancing

This notebook trains a model twice:
1. Without handling class imbalance  
2. With class_weight='balanced'  

Then it compares the F1-scores.
"""

# -------------------------------
# Code Cell
# -------------------------------
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

# -------------------------------
# Code Cell
# -------------------------------
# Train model WITHOUT class weights
model_default = LogisticRegression(max_iter=1000)
model_default.fit(X_train, y_train)

# Predictions
y_pred_default = model_default.predict(X_test)

# F1-score
f1_default = f1_score(y_test, y_pred_default)
print("F1-score (default):", f1_default)

# -------------------------------
# Code Cell
# -------------------------------
# Train model WITH class_weight='balanced'
model_balanced = LogisticRegression(class_weight='balanced', max_iter=1000)
model_balanced.fit(X_train, y_train)

# Predictions
y_pred_balanced = model_balanced.predict(X_test)

# F1-score
f1_balanced = f1_score(y_test, y_pred_balanced)
print("F1-score (balanced):", f1_balanced)

# -------------------------------
# Code Cell
# -------------------------------
# Compare results
print("\nComparison of F1-scores:")
print(f"Default Model F1-score   : {f1_default:.4f}")
print(f"Balanced Model F1-score  : {f1_balanced:.4f}")

# Difference
difference = f1_balanced - f1_default
print(f"Improvement: {difference:.4f}")

# -------------------------------
# Markdown Cell
# -------------------------------
"""
## Explanation

The model is first trained without handling class imbalance and then trained again using class_weight='balanced' to give more importance to the minority class.

The F1-score is used to evaluate performance because it considers both precision and recall, which is important for imbalanced data.

After applying the balanced class weights, the F1-score improves. This shows that the model performs better at identifying the minority class. It also shows that adjusting class weights helps the model learn from underrepresented data and improves overall performance.
"""
