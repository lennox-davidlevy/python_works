class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        if self.check_responses_empty():
            print("Survery results:")
            for response in self.responses:
                print(f"- {response}")
        else:
            print("No responses available")

    def check_responses_empty(self):
        return len(self.responses) > 0
