from book.survey import AnnoymousSurvey

question = 'what language did you first learn to speak?'
my_survey=AnnoymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response =='q':
        break
    my_survey.store_response(response)

print("\nThanks you to everyone who participated in the survey!")
my_survey.show_results()
