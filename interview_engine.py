# interview_engine.py

from states import EASY, MEDIUM, HARD, WARNING, TERMINATED, COMPLETED
from questions import QUESTIONS

# ==============================
# SCORING & STRESS CONSTANTS
# ==============================

GOOD_SCORE = 10
AVERAGE_SCORE = 5
BAD_SCORE = -5

GOOD_STRESS = -10
AVERAGE_STRESS = 5
BAD_STRESS = 15

WARNING_STRESS_THRESHOLD = 65
TERMINATION_STRESS_THRESHOLD = 85


def evaluate_answer(answer_quality, score, stress):
    if answer_quality == "good":
        score += GOOD_SCORE
        stress += GOOD_STRESS
    elif answer_quality == "average":
        score += AVERAGE_SCORE
        stress += AVERAGE_STRESS
    else:
        score += BAD_SCORE
        stress += BAD_STRESS

    stress = max(0, min(100, stress))
    return score, stress


def get_next_state(current_state, answer_quality, stress):

    if current_state == WARNING and stress >= TERMINATION_STRESS_THRESHOLD:
        return TERMINATED

    if stress >= WARNING_STRESS_THRESHOLD:
        return WARNING

    if current_state == EASY:
        return MEDIUM if answer_quality == "good" else EASY

    if current_state == MEDIUM:
        if answer_quality == "good":
            return HARD
        elif answer_quality == "bad":
            return EASY
        return MEDIUM

    if current_state == HARD:
        if answer_quality == "good" and stress < 40:
            return COMPLETED
        return MEDIUM

    if current_state == WARNING:
        return MEDIUM if answer_quality == "good" else TERMINATED

    return current_state


def get_final_feedback(score, stress):
    if score >= 70:
        category = "Strong"
    elif score >= 40:
        category = "Average"
    else:
        category = "Needs Improvement"

    feedback = []

    if stress > 60:
        feedback.append("Performance dropped under pressure.")
    else:
        feedback.append("Handled interview pressure well.")

    if score < 40:
        feedback.append("Needs stronger fundamentals and practice.")
    elif score < 70:
        feedback.append("Decent performance, but consistency can improve.")
    else:
        feedback.append("Interview-ready for the given role.")

    return category, feedback


def run_interview(return_logs=False):

    current_state = EASY
    score = 0
    stress = 0
    logs = []

    print("\n🎤 AI Mock Interview Started")
    print("----------------------------------")

    while current_state not in [TERMINATED, COMPLETED]:

        question = QUESTIONS[current_state][0]
        answer_quality = question["answer_quality"]

        print(f"\n📍 Current State: {current_state}")
        print(f"📊 Score: {score} | 😰 Stress: {stress}")
        print(f"\n❓ Question: {question['text']}")
        print(f"📝 Answer Quality: {answer_quality.upper()}")

        score, stress = evaluate_answer(answer_quality, score, stress)
        next_state = get_next_state(current_state, answer_quality, stress)

        print(f"🔁 Transition: {current_state} → {next_state}")

        logs.append({
            "state": current_state,
            "score": score,
            "stress": stress,
            "question": question["text"],
            "answer": answer_quality.upper()
        })

        current_state = next_state

        if current_state == TERMINATED:
            print("\n⚠️ Interview terminated due to high stress.")
            break

    category, feedback = get_final_feedback(score, stress)

    print("\n==================================")
    print("🛑 Interview Ended")
    print("==================================")
    print(f"\n✅ Final Interview Readiness Score: {score}")
    print(f"📌 Category: {category}")
    print("\n📋 Feedback:")
    for f in feedback:
        print(f"- {f}")

    if return_logs:
        return {
            "final_score": score,
            "category": category,
            "feedback": feedback,
            "logs": logs
        }
