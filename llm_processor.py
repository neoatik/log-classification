from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq = Groq()

def classify_with_llm(log_msg):
    prompt = f'''Classify the log message into one of the these catagories:
    (1)Workflow Error, (2)Deprecation Warning.
    If you can't figure out the catagory, return "Unclassified".
    Only return the catagory name. No preamble.
    log message:{log_msg} '''
    chat_completion = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],     
    )

    print(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    print(classify_with_llm("Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm("The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))