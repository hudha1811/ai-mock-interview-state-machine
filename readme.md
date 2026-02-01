# 🧠 AI-Powered Mock Interview Platform  
### A Stateful & Stress-Aware Interview Simulation Engine

---

## 📌 Overview

This project implements an **AI-powered mock interview platform** that simulates how real technical interviews are conducted in modern hiring systems.

Instead of relying on machine learning or black-box AI models, the system uses a **rule-driven, stateful evaluation engine** that adapts interview difficulty, scoring, and termination decisions based on candidate performance and stress — closely mirroring how real interviewers think and react.

The goal is to objectively measure **interview readiness**, not just correctness of answers.

---

## 🎯 Problem Alignment (Hack2Hire)

This solution directly satisfies all core expectations of the Hack2Hire challenge:

| Hackathon Requirement | Implementation |
|----------------------|----------------|
| Stateful simulation | ✅ Explicit finite state machine |
| Adaptive behavior | ✅ Difficulty adapts dynamically |
| Performance under pressure | ✅ Stress-aware evaluation |
| Time & pressure modeling | ✅ Stress-based penalties |
| Early interview termination | ✅ WARNING & TERMINATED states |
| Objective scoring | ✅ Rule-based scoring engine |
| Real-world interview realism | ✅ Product-style evaluation logic |

---

## 🧩 Design Philosophy

> **Interviews are adaptive decision systems, not linear questionnaires.**

This project models an interview as a **finite state machine**, where:
- Each answer affects the **next interview state**
- Stress accumulates under pressure
- Poor performance triggers early termination
- Strong performance accelerates completion

This mirrors how interviewers dynamically adjust difficulty and expectations in real time.

---

## 🔁 Interview State Machine

### 📍 States Defined

START → EASY → MEDIUM → HARD
↓
WARNING
↓
TERMINATED / COMPLETED


### 🧠 State Descriptions

| State | Purpose |
|------|--------|
| EASY | Warm-up, low-pressure questions |
| MEDIUM | Standard evaluation round |
| HARD | High-pressure technical probing |
| WARNING | Performance degradation detected |
| TERMINATED | Early interview rejection |
| COMPLETED | Interview successfully completed |

---

## 😰 Stress-Aware Evaluation (Key Innovation)

A **Stress Level (0–100)** is tracked throughout the interview.

### Stress increases when:
- Answers are incorrect
- Performance drops in harder rounds
- Candidate struggles under pressure

### Stress decreases when:
- Answers are strong
- Candidate regains consistency

### Why stress matters:
- High stress prevents difficulty escalation
- High stress reduces score gains
- Extreme stress triggers early termination

This models **performance under pressure**, a critical real-world interview factor.

---

## 📊 Scoring Rules

| Answer Quality | Score Change | Stress Change |
|---------------|-------------|---------------|
| Good | +10 | −10 |
| Average | +5 | +5 |
| Bad | −5 | +15 |

Stress is always clamped between **0 and 100** to maintain system stability.

---

## 🛑 Early Termination Logic

The interview ends early if:
- Stress exceeds a critical threshold in WARNING state
- Candidate shows continuous performance degradation
- Maximum number of questions is reached

This reflects real-world interviewer cut-off behavior.

---

## 🏁 Final Evaluation Output

At the end of the interview, the system generates:

- ✅ Final Interview Readiness Score (0–100)
- ✅ Performance Category  
  - **Strong**  
  - **Average**  
  - **Needs Improvement**
- ✅ Pressure-handling feedback
- ✅ Actionable improvement suggestions

---

## 🛠️ Tech Stack

- **Language:** Python
- **Architecture:** Rule-based finite state machine
- **Interface:** Command Line Interface (CLI)
- **Dependencies:** None (lightweight & portable)

---

## ▶️ How to Run

Run the interview simulation using the command below.

Command to execute:
    python main.py

---

## 👩‍💻 Author

**Hudha Ashraf**  
Computer Science & Engineering Student  
Participant – Hack2Hire: AI-Powered Interview Hackathon 
