import requests
from prefect import flow

@flow(log_prints=True)
def extract_questions(amount: int = 10, type: str = "boolean"):
    response = requests.get("https://opentdb.com/api.php", params = { "amount" : amount, "type" : type })
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]

extract_questions(10, "boolean")

if __name__ == "__main__":
    extract_questions.serve(name="my-second-deployment",
                      tags=["onboarding"],
                      interval=3600)

# parameters = { 
#     "amount" : 10,
#     "type" : "boolean"
# }

# response = requests.get("https://opentdb.com/api.php", params = parameters)
# response.raise_for_status()
# data = response.json()
# question_data = data["results"]


