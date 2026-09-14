def ask_question(question_text):
    answer = input(question_text)
    return answer

def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False

def show_feedback(is_correct):
    if is_correct:
        print("The answer is correct.")
    else:
        print("The answer is wrong. Try again.")

def run_quiz():
    point = 0
    answer = ask_question("What is the capital if Norway?")
    is_correct = check_answer(answer, correct_answer= "Oslo")
    if is_correct:
        point +=1
    show_feedback(is_correct)

    answer = ask_question("Who is the king of Norway ?")
    is_correct = check_answer(answer, correct_answer="Hakoon")
    if is_correct:
        point +=1
    show_feedback(is_correct)

    answer = ask_question("What is the year we are in ?")
    is_correct = check_answer(answer, correct_answer="2026")
    if is_correct:
        point +=1
    show_feedback(is_correct)
    print(f"Your answered {point} out of 3 questions correctly.")
run_quiz()




