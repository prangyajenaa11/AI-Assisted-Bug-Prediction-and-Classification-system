from flask import Flask, render_template, request
import classification_model
import prediction_model

app = Flask(__name__)

# Load trained models
clf = classification_model.train_classification_model()
pred_model = prediction_model.train_prediction_model()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get code metrics from the form
    code_metrics = ...  # Replace with your logic to extract data

    # Predict bug type and likelihood
    predicted_bug_type = clf.predict(code_metrics)[0]
    predicted_likelihood = pred_model.predict_proba(code_metrics)[0][1]

    return render_template("result.html",
                           predicted_bug_type=predicted_bug_type,
                           predicted_likelihood=predicted_likelihood)

if __name__ == "__main__":
    app.run(debug=True)