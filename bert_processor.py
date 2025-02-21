from sentence_transformers import SentenceTransformer
import joblib
import numpy as np

# Load models 
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')
classifier_model = joblib.load('models/log_message_classifier_01.joblib')  

def classify_with_bert(log_message):
    message_embedding = transformer_model.encode(log_message)
    message_embedding = np.array(message_embedding).reshape(1, -1)
    probabilities = classifier_model.predict_proba(message_embedding)[0]

    # If max probability is less than 0.5, classify as "Unclassified"
    if max(probabilities) < 0.23:
        return "Unclassified"
    else:
        predicted_label = classifier_model.predict(message_embedding)[0]
        return predicted_label

if __name__ == "__main__":
    logs = [
        "Multiple bad login attempts detected on user 8538 account",
        "RAID array experienced multiple disk crashes",
        "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE  200 len: 1893 time: 0.2738080",
        "olaala le o",
        "Systemic configuration inconsistencies detected"
    ]
    
    for log in logs:  
        label = classify_with_bert(log)
        print(log, "->", label)
