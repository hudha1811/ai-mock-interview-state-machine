# main.py

from states import START, EASY, MEDIUM, HARD, WARNING, TERMINATED, COMPLETED
from interview_engine import evaluate_answer, get_next_state, get_final_feedback
from data.questions import QUESTIONS
import random
import time


def run_interview():
    current_state = EASY
    score = 0
    stress = 0
    question_count = 0
    max_questions = 10

    print("\n🎤 AI Mock Interview Started")
    print("----------------------------------")

    while current_state not in [TERMINATED, COMPLETED] and question_count < max_questions:

        print(f"\n📍 Current State: {current_state}")
        print(f"📊 Score: {score} | 😰 Stress: {stress}")

        # Pick a question based on state
        question = random.choice(QUESTIONS[current_state])
        print(f"\n❓ Question: {question['text']}")

        # Simulate thinking time
        time.sleep(1)

        answer_quality = question["answer_quality"]
        print(f"📝 Answer Quality: {answer_quality.upper()}")

        # Step 7 logic
        score, stress = evaluate_answer(answer_quality, score, stress)

        # State transition
        next_state = get_next_state(current_state, answer_quality, stress)

        print(f"🔁 Transition: {current_state} → {next_state}")

        current_state = next_state
        question_count += 1

        time.sleep(1)

    print("\n==================================")
    print("🛑 Interview Ended")
    print("==================================")

    category, feedback = get_final_feedback(score, stress)

    print(f"\n✅ Final Interview Readiness Score: {score}")
    print(f"📌 Category: {category}")

    print("\n📋 Feedback:")
    for f in feedback:
        print(f"- {f}")


if __name__ == "__main__":
    run_interview()

