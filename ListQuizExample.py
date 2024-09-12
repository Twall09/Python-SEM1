# Student Quiz Calculator

# import libraries
import FormatValues as FV

print()
QuizTitle = input("Enter the quiz title: ")
NumQuestions = input("Enter the number of questions: ")
NumQuestions = int(NumQuestions)

# Build the answer key
AnswerKey = []
AnswerLst = ["A", "B", "C", "D"]
for Question in range(1, NumQuestions + 1):
    while True:
        Answer = input("Enter the answer for the question " + str(Question) + "(A, B, C, D): ").upper()

        if Answer == "":
            print("Error")
        elif Answer not in AnswerLst:
            print("Error")
        else:
            break

        AnswerKey.append(Answer)

# Prompt for the number of quizzes to be graded
        
NumQuiz = input("Enter the total number of quizzes to be graded: ")
NumQuiz = int(NumQuiz)

# Input the student and the answer for each question
StudNameLst = []
NumCorrectLst= []
GradeLst = []

for Quizzes in range(1, NumQuiz + 1):
    StuName = input("Enter the student name: ")

    StuAnswer = []
    for Question in range(1, NumQuestions + 1):
        while True:
            Answer = input("Enter the answer for the question " + str(Question) + "(A, B, C, D): ").upper()

            if Answer == "":
                print("Error")
            elif Answer not in AnswerLst:
                print("Error")
            else:
                break

        # Add the student answers to a second list.
        StuAnswer.append(Answer)
    
    # Grade the test by comparing the values in the AnswerKey and StuAnswer 
    
    # Keep track of the number they get correct.
    NumCorrect = 0
    for i in range(0, NumQuestions):
        if StuAnswer[i] == AnswerKey[i]:
            NumCorrect += 1

    # Calculate the grade.
    Grade = (NumCorrect / NumQuestions) * 100
        
    # Add the student name, number correct, and the gradr to the lists

    StudNameLst.append(StuName)
    NumCorrectLst.append(NumCorrect)
    GradeLst.append(Grade)
        
    # Print the results

    print(f"   Quiz: {QuizTitle}")
print()
print("    Student          # Correct         % Grade")
print("    ------------------------------------------")
for i in range(0, len(StudNameLst)):
    print(f"    {StudNameLst[i]:<15s}     {NumCorrectLst[i]:>2d}             {FV.FNumber1(GradeLst[i]):>5s}")