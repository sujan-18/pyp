print('+-'*12 + "WELCOME TO OUR PYTHON PROJECT" + '+-'*12)
print('+-'*12 + "Customer feedback" + '+-'*12)

def view_feedback():
    with open("Data/feedback.txt","r") as feedback_file:
        for i in feedback_file:
            print(i.strip())