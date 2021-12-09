def check_answer(user_answer, correct_answer):
  if user_answer.lower() == correct_answer.lower():
    print("Correct!")
  else:
    print(f"Wrong. The correct answer is {correct_answer}.")

print()

answer = input("What is the largest ocean in the world? ")
check_answer(answer, "Pacific")

answer = input("\nWhich country has the biggest population? ")
check_answer(answer, "China")

answer = input("\nHow many planets are in the solar system? ")
check_answer(answer, "8")
