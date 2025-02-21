from regex_processor import classify_with_regex
from llm_processor import classify_with_llm
from bert_processor import classify_with_bert
import pandas as pd
def classify(logs):
    labels = []
    for source, log_message in logs:
        label = classify_log(source, log_message)
        labels.append(label)
    return labels

def classify_log(source, log_msg):
    if source == "LegacyCRM":
        label = classify_with_llm(log_msg)
    else:
        label = classify_with_regex(log_msg)
        if not label:
            label = classify_with_bert(log_msg)
    return label
    
def classify_csv(input_file):
    import pandas as pd
    df = pd.read_csv(input_file)

    # Perform classification
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    # Save the modified file
    output_file = "resources/output.csv"
    df.to_csv(output_file, index=False)
    

if __name__ == "__main__":
    classify_csv("resources/test.csv")
#     logs = [
#         ("ModerCRM", "Warning: IP 192.168.191.32 may be compromised"),
#         ("BillingSystem", "User User522 logged in."),
#         ("AnalyticsEngine", "Backup completed successfully."),
#         ("AnalyticsEngine", "File data_5435.csv uploaded successfully by user User563."),
#         ("ModerHR", "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE 200 len: 1583 time: 0.1878400"),
#         ("ModerHR", "Admin privilege elevation warning for user 8383"),
#         ("LegacyCRM", "Escalation rule execution failed for ticket ID 9807 - undefined escalation level."),
#         ("LegacyCRM", "Lead conversion failed for prospect ID 7842 due to missing contact information."),
#         ("LegacyCRM", "Task assignment for TeamID 3425 could not complete due to invalid priority level."),
#         ("LegacyCRM", "The 'ExportToCSV' feature is outdated. Please migrate to 'ExportToXLSX' by the end of Q3.")
#     ]  

 
# classified_logs = classify(logs)
# print(classified_logs)