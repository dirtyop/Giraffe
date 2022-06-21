from question import Questions

question_prompts = [
    "What color are apples?\n(a) Red/green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")
]


def run_test(a):
    score = 0
    for question in a:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("your score is " + str(score) + "/ " + str(len(a)))


run_test(questions)
