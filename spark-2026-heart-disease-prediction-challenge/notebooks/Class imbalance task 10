# Import libraries
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

# -----------------------------
# 1. Train model WITHOUT class weights
# -----------------------------
model_default = LogisticRegression(max_iter=1000)
model_default.fit(X_train, y_train)

# Predictions
y_pred_default = model_default.predict(X_test)

# F1-score
f1_default = f1_score(y_test, y_pred_default)
print("F1-score (default):", f1_default)


# -----------------------------
# 2. Train model WITH class_weight='balanced'
# -----------------------------
model_balanced = LogisticRegression(class_weight='balanced', max_iter=1000)
model_balanced.fit(X_train, y_train)

# Predictions
y_pred_balanced = model_balanced.predict(X_test)

# F1-score
f1_balanced = f1_score(y_test, y_pred_balanced)
print("F1-score (balanced):", f1_balanced)


# -----------------------------
# 3. Compare results
# -----------------------------
print("\nComparison of F1-scores:")
print(f"Default Model F1-score   : {f1_default:.4f}")
print(f"Balanced Model F1-score  : {f1_balanced:.4f}")

