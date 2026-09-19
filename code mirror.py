# ==========================================
# 🪞 CODEMIRROR
# Personal Coding Mistake Tracker
# ==========================================

problems = []


# ------------------------------------------
# 1. ADD A PROBLEM
# ------------------------------------------

def add_problem():
    print("\n--- Add Problem ---")

    name = input("Problem name: ")
    topic = input("Topic: ")
    mistake = input("What mistake did you make? ")

    problem = {
        "name": name,
        "topic": topic,
        "mistake": mistake
    }

    problems.append(problem)

    print("\n✅ Problem added successfully!")


# ------------------------------------------
# 2. VIEW ALL PROBLEMS
# ------------------------------------------

def view_problems():
    print("\n--- Your Problems ---")

    if not problems:
        print("No problems added yet.")
        return

    for i, problem in enumerate(problems, 1):
        print("\nProblem", i)
        print("Name   :", problem["name"])
        print("Topic  :", problem["topic"])
        print("Mistake:", problem["mistake"])


# ------------------------------------------
# 3. FIND WEAKEST TOPIC
# ------------------------------------------

def find_weak_topic():

    if not problems:
        print("\nNo problems added yet.")
        return

    topic_count = {}

    for problem in problems:

        topic = problem["topic"]

        if topic in topic_count:
            topic_count[topic] = topic_count[topic] + 1
        else:
            topic_count[topic] = 1

    print("\n--- 📊 Topic Report ---")

    for topic in topic_count:
        print(topic, ":", topic_count[topic], "mistakes")

    weak_topic = max(topic_count, key=topic_count.get)

    print("\n⚠️ Weakest Topic:", weak_topic)


# ------------------------------------------
# 4. MAIN MENU
# ------------------------------------------

while True:

    print("\n==============================")
    print("        🪞 CODEMIRROR")
    print("==============================")

    print("1. Add Problem")
    print("2. View Problems")
    print("3. Find Weak Topic")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_problem()

    elif choice == "2":
        view_problems()

    elif choice == "3":
        find_weak_topic()

    elif choice == "4":
        print("\n👋 Thank you for using CodeMirror!")
        break

    else:
        print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")