from sklearn.linear_model import LogisticRegression

def train_prediction_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Evaluate
    # ... (use appropriate metrics for prediction)

    return model

if __name__ == "__main__":
    X, y = preprocess_data()
    model = train_prediction_model(X, y)