# interview_engine.py

from states import EASY, MEDIUM, HARD, WARNING, TERMINATED, COMPLETED

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


# ==============================
# EVALUATE ANSWER 
# ==============================

def evaluate_answer(answer_quality, score, stress):
    """
    Updates score and stress based on answer quality
    """
    if answer_quality == "good":
        score += GOOD_SCORE
        stress += GOOD_STRESS
    elif answer_quality == "average":
        score += AVERAGE_SCORE
        stress += AVERAGE_STRESS
    else:  # bad
        score += BAD_SCORE
        stress += BAD_STRESS

    # Clamp stress between 0 and 100
    stress = max(0, min(100, stress))

    return score, stress


# ==============================
# STATE TRANSITION LOGIC
# ==============================

def get_next_state(current_state, answer_quality, stress):
    """
    Determines next interview state based on current state,
    answer quality, and stress level
    """

    # Immediate termination due to extreme stress
    if current_state == WARNING and stress >= TERMINATION_STRESS_THRESHOLD:
        return TERMINATED

    # Stress-based warning
    if stress >= WARNING_STRESS_THRESHOLD:
        return WARNING

    if current_state == EASY:
        if answer_quality == "good":
            return MEDIUM
        else:
            return EASY

    if current_state == MEDIUM:
        if answer_quality == "good":
            return HARD
        elif answer_quality == "bad":
            return EASY
        else:
            return MEDIUM

    if current_state == HARD:
        if answer_quality == "good" and stress < 40:
            return COMPLETED
        else:
            return MEDIUM

    if current_state == WARNING:
        if answer_quality == "good":
            return MEDIUM
        else:
            return TERMINATED

    return current_state


# ==============================
# FINAL RESULT EVALUATION
# ==============================

def get_final_feedback(score, stress):
    """
    Generates final interview result and feedback
    """
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


