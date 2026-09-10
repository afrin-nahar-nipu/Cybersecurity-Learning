# 🔒 Deadlock Practice – Operating System

This repository contains my hands-on practice on **Deadlock concepts in Operating Systems** using Python.

## 📚 Topics Covered

### 1. Create Deadlock

Created a deadlock situation using two processes and two resources.

* Process P1 holds Resource A and waits for Resource B.
* Process P2 holds Resource B and waits for Resource A.
* This creates a Circular Wait condition and causes Deadlock.

### 2. Observe Deadlock

Observed the deadlock situation using Python threads and resource locks.

The program demonstrates how processes wait indefinitely when each process holds a resource required by another process.

### 3. Deadlock Prevention

Prevented deadlock by following a fixed resource ordering.

Both processes acquire resources in the same order:

`Resource A → Resource B`

This prevents the Circular Wait condition.

### 4. Timeout-Based Handling

Used Python's `acquire(timeout=...)` method to avoid indefinite waiting.

If a resource is not available within a specific time, the process releases its held resource and exits safely.

### 5. Resource Allocation Graph

Implemented a Resource Allocation Graph using Python.

Used the **Depth First Search (DFS)** algorithm to detect cycles in the graph.

A cycle may indicate a possible deadlock.

### 6. Need Matrix Calculator

Calculated the Need Matrix using:

`Need = Maximum - Allocation`

This is an important part of the Banker's Algorithm.

### 7. Banker's Algorithm

Implemented the Banker's Algorithm to check whether the system is in a:

* Safe State
* Unsafe State

The program calculates the Need Matrix and checks whether each process can safely execute.

### 8. Safe Sequence

Generated a Safe Sequence for processes using the Safety Algorithm.

Example:

`P0 → P1 → P2`

A safe sequence ensures that all processes can complete without causing deadlock.

### 9. Deadlock Detection

Implemented the Deadlock Detection Algorithm using:

* Available Vector
* Allocation Matrix
* Request Matrix

The program identifies processes that cannot complete and may be involved in a deadlock.

### 10. Deadlock Recovery

Simulated a basic Deadlock Recovery technique.

The program:

1. Detects a deadlock.
2. Selects a victim process.
3. Terminates the selected process.
4. Releases its allocated resources.
5. Allows the remaining processes to continue.

---

## 🛠️ Technologies Used

* Python
* Python Threading
* Python Locks
* DFS Algorithm

---

## 📂 Practice Files

```text
Deadlock-Practice/
│
├── 01_create_deadlock.py
├── 02_observe_deadlock.py
├── 03_deadlock_prevention.py
├── 04_timeout_handling.py
│
├── 05_rag_detector.py
├── 06_need_matrix.py
├── 07_bankers_algorithm.py
├── 08_safe_unsafe_test.py
│
├── 09_deadlock_detection.py
└── 10_deadlock_recovery.py
```

---

## 🎯 Learning Objectives

Through this practice, I learned how to:

* Create a deadlock situation.
* Observe process waiting and resource locking.
* Prevent deadlock using resource ordering.
* Handle resource waiting using timeouts.
* Detect cycles in a Resource Allocation Graph.
* Calculate the Need Matrix.
* Implement the Banker's Algorithm.
* Find a Safe Sequence.
* Detect deadlocked processes.
* Simulate basic deadlock recovery.

---

## 📖 Key Formula

```text
Need = Maximum - Allocation
```

---

## 🔑 Important Deadlock Conditions

Deadlock can occur when the following four conditions exist simultaneously:

1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait

---

## 👩‍💻 Learning Journey

This repository is part of my **Cybersecurity and Operating System Learning Journey**.

I am practicing Operating System concepts not only theoretically but also through hands-on Python programming.

**Learning → Practice → Understand → Improve**

---

## 👤 Author

**Afrin Nahar Nipu**

🎓 CSE Student
🔐 Cybersecurity Learner
💻 Interested in Penetration Testing and Cybersecurity

---

⭐ This repository documents my hands-on journey of learning and practicing Deadlock concepts in Operating Systems.
