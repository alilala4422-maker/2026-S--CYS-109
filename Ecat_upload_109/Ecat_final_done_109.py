# ---------- Ali Ahmad Khan ------- Roll No.109 ----------- Cys(s)_2026

# Credentials
ADMIN_USER   = "ecat_admin"
ADMIN_PASS   = "ecat@2024"
STUDENT_USER = "student"
STUDENT_PASS = "student123"

all_results = []

# ---- Question Class ----
class Question:
    def __init__(self, subject, question_text, opt_a, opt_b, opt_c, opt_d, correct):
        self.subject  = subject
        self.question = question_text
        self.opt_a    = opt_a
        self.opt_b    = opt_b
        self.opt_c    = opt_c
        self.opt_d    = opt_d
        self.answer   = correct.upper()

    def display(self, number):
        print("\nQuestion", number, "[" + self.subject + "]")
        print(self.question)
        print("A.", self.opt_a)
        print("B.", self.opt_b)
        print("C.", self.opt_c)
        print("D.", self.opt_d)

# ---- Default Questions by myself ----
questions = [
    Question("Math",      "Solve for x: x^2 - 5x + 6 = 0",       "x=1,2",      "x=2,3",    "x=3,4",              "x=1,6",           "B"),
    Question("Physics",   "A body moving with uniform velocity, its acceleration is?", "Increasing", "Decreasing", "Zero",  "Constant but non-zero", "C"),
    Question("English",   "Synonym of Frost?",                     "Warm",       "Cold",     "Fire",               "Ice",             "B"),
    Question("Chemistry", "Formula of Hydrochloric Acid?",         "CO2",        "H2O",      "HCl",                "NaCl",            "C"),
    Question("Math",      "Find the derivative of y = x^2",        "2x",         "x",        "0",                  "x^2",             "A"),
    Question("Physics",   "The Sun revolves around?",              "Moon",       "Galaxy",   "Mars",               "Black Hole",      "D"),
    Question("English",   "Synonym of Abundant?",                  "Scarce",     "Plenty",   "Rare",               "Empty",           "B"),
    Question("Chemistry", "Symbol of Oxygen?",                     "O",          "Ox",       "Og",                 "X",               "A"),
    Question("Math",      "2^8 = ?",                               "128",        "64",       "256",                "520",             "C"),
    Question("Physics",   "Speed formula?",                        "VxT",        "D/T",      "T/D",                "V+D",             "B"),
]
# ---- Grade Function ----
def grade(percent):
    if percent >= 80:
        return "EXCELLENT"
    elif percent >= 65:
        return "GOOD"
    elif percent >= 50:
        return "AVERAGE"
    else:
        return "BELOW AVERAGE"


# ---- Admin: Add Questions ----
def add_questions():
    print("\nADD QUESTIONS")
    print("Type DONE as subject to stop\n")
    added = 0
    while True:
        subject = input("Subject (or DONE to stop): ")
        if subject.upper() == "DONE":
            break
        question_text = input("Question Text: ")
        opt_a = input("Option A: ")
        opt_b = input("Option B: ")
        opt_c = input("Option C: ")
        opt_d = input("Option D: ")
        correct = input("Correct Answer (A/B/C/D): ").upper()
        q = Question(subject, question_text, opt_a, opt_b, opt_c, opt_d, correct)
        questions.append(q)
        added += 1
        print("Question Added! Total so far:", len(questions))
    print("Done. Total questions in exam:", len(questions))

# ---- Admin: View and Delete Questions ----
def manage_questions():
    while True:
        print("\nQUESTION BANK")
        if len(questions) == 0:
            print("No questions available.")
        else:
            for i in range(len(questions)):
                print(i + 1, ".", questions[i].subject, "-", questions[i].question)

        print("\n1. Delete a Question")
        print("2. Back")
        choice = input("Choice: ")
        if choice == "2":
            break
        elif choice == "1":
            num = int(input("Enter question number to delete: "))
            if num >= 1 and num <= len(questions):
                questions.pop(num - 1)
                print("Question deleted.")
            else:
                print("Invalid number.")

# ---- Admin: View All Results ----
def view_all_results():
    print("\nALL RESULTS")
    if len(all_results) == 0:
        print("No results yet.")
        return
    for r in all_results:
        print("\nName      :", r["name"])        # go inside dictionary r and get the value stored at key "name"
        print("Roll No   :", r["roll"])
        print("Score     :", r["score"])
        print("Percentage:", r["percentage"], "%")
        print("Grade     :", r["grade"])

# ---- Admin: View Individual Result ----
def view_individual_result():
    print("\nSEARCH RESULT")
    if len(all_results) == 0:
        print("No results yet.")
        return
    search = input("Enter Name or Roll No: ")
    found = False
    for r in all_results:
        if search == r["name"] or search == r["roll"]:
            print("\nName      :", r["name"])
            print("Roll No   :", r["roll"])
            print("Score     :", r["score"])
            print("Percentage:", r["percentage"], "%")
            print("Grade     :", r["grade"])
            found = True
    if found == False:
        print("No candidate found.")

# ---- Admin Menu ----
def admin_menu():
    while True:
        print("\nADMIN MENU")
        print("1. Add Questions")
        print("2. View / Delete Questions")
        print("3. View All Results")
        print("4. View Individual Result")
        print("5. Total Question Count")
        print("6. Logout")
        choice = input("Choice: ")
        if choice == "1":
            add_questions()
        elif choice == "2":
            manage_questions()
        elif choice == "3":
            view_all_results()
        elif choice == "4":
            view_individual_result()
        elif choice == "5":
            print("Total Questions:", len(questions))
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

# ---- Admin Login ----
def admin_login():
    attempts = 3
    while attempts > 0:
        user     = input("Admin Username: ")
        password = input("Admin Password: ")
        if user == ADMIN_USER and password == ADMIN_PASS:
            print("Login Successful!")
            admin_menu()
            return
        attempts -= 1
        print("Wrong credentials.", attempts, "attempt(s) left.")
    print("Account locked.")

# ---- Exam ----
def exam():
    if len(questions) == 0:
        print("No questions available. Contact admin.")
        return
    name = input("Enter Your Name: ")
    roll = input("Enter Your Roll No: ")
    score = 0
    skipped_idx = []
    answers_given = {}
    print("\nS = Skip  |  A/B/C/D = Answer  |  SUBMIT = End exam")
    for i in range(len(questions)):          #here questions is global list of questions
        questions[i].display(i + 1)
        ans = input("  Your Answer: ").upper()
        if ans == "SUBMIT":
            break
        elif ans == "S":
            skipped_idx.append(i)
            continue
        elif ans in ("A", "B", "C", "D"):
            answers_given[i] = ans
        else:
            print("  Invalid input — treated as skipped.")
            skipped_idx.append(i)
            continue
    if skipped_idx:
        print(f"\n  You have {len(skipped_idx)} skipped question(s). Attempt them now? (Y/N): ", end="")
        if input().upper() == "Y":
            for i in skipped_idx:
                questions[i].display(i + 1)
                ans = input("  Your Answer: ").upper()
                if ans in ("A", "B", "C", "D"):
                    answers_given[i] = ans
                else:
                    print("  Skipped again.")
    # ---- Calculate score ----
    for i, ans in answers_given.items():
        if ans == questions[i].answer:
            score += 4
        else:
            score -= 1

    total      = len(questions) * 4
    percent    = (score / total) * 100
    percent    = round(percent, 2)
    result = {
        "name"       : name,
        "roll"       : roll,
        "score"      : score,
        "percentage" : percent,
        "grade"      : grade(percent)
    }
    all_results.append(result)
    print("\nYOUR RESULT")
    print("Name      :", result["name"])
    print("Roll No   :", result["roll"])
    print("Score     :", result["score"], "/", total)
    print("Percentage:", result["percentage"], "%")
    print("Grade     :", result["grade"])

# ---- Student Login ----
def student_login():
    attempts = 3
    while attempts > 0:
        user     = input("Username: ")
        password = input("Password: ")
        if user == STUDENT_USER and password == STUDENT_PASS:
            print("Login Successful!")
            exam()
            return
        attempts -= 1
        print("Wrong credentials.", attempts, "attempt(s) left.")
    print("Account locked.")

# ---- Rules ----
def show_rules():
    print("\nEXAM RULES")
    print("+4 for correct answer")
    print("-1 for wrong answer")
    print(" 0 for skipped question")
    print("Type SUBMIT to end exam early")

# ---- Main Menu ----
def main():
    while True:
        print("\nECAT EXAM SYSTEM")
        print("1. Student Portal")
        print("2. Admin Portal")
        print("3. Rules")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_login()
        elif choice == "2":
            admin_login()
        elif choice == "3":
            show_rules()
        elif choice == "4":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice.")

main()