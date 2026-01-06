import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Mock data reflecting FedEx account profiles
data = {
    'debt_amount': [1000, 5000, 200, 15000],
    'days_overdue': [45, 120, 30, 200],
    'past_recovery_success': [1, 0, 1, 0], # 1 for yes, 0 for no
    'recovered': [1, 0, 1, 0] # Target variable
}

df = pd.DataFrame(data)

# Features: Amount, Age, and History 
X = df[['debt_amount', 'days_overdue', 'past_recovery_success']]
y = df['recovered']

# Train a model to predict recovery probability [cite: 27]
model = RandomForestClassifier()
model.fit(X, y)

def predict_priority(new_case):
    # Returns a probability score to rank cases in the DCA portal [cite: 24]
    probability = model.predict_proba(new_case)[0][1]
    return "High Priority" if probability > 0.7 else "Standard"
