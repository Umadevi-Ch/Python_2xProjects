print("Exam results")
marks = 100
if marks == 35:
    print("you are promoted! marks: ", marks)
elif marks > 35:
    print("you passed the exam! marks:", marks)
    if marks >= 75 and marks <= 85:
        print("you got good marks! marks: ", marks)
    elif marks > 85 and marks <=95:
        print("you got great marks! marks: ", marks)
    elif marks > 95:
        print("you got the best marks! marks: ", marks)
    else:
        print("you got in between 35 and 75 range marks marks: ", marks)
else:
        print("You failed the exam marks: ", marks)
