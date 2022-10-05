from question_model import Question
from data import question_data


question_bank = []

for q in question_data:
    # q_text = q["text"]
    # q_answer = q["answer"]
    # new_question = Question(q_text, q_answer)
    # question_bank.append(new_question)
    new_question = Question(q["text"], q["answer"])
    question_bank.append(new_question)


print(question_bank)
