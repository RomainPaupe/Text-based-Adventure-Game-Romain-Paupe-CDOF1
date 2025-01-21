import random

class StudentLifeGame:
    def __init__(self):
        self.grade = 0
        self.social_life = 0
        self.motivation = 5  # Motivation is a key factor affecting decisions.
        self.time_spent_on_study = 0
        self.time_spent_on_other_activities = 0

    def display_status(self):
        print("\nCurrent Status:")
        print(f"Grade: {self.grade}")
        print(f"Social Life: {self.social_life}")
        print(f"Motivation: {self.motivation}")
        print(f"Time spent on study: {self.time_spent_on_study} hours")
        print(f"Time spent on other activities: {self.time_spent_on_other_activities} hours")

    def make_choice(self, prompt, choices):
        print(prompt)
        for idx, choice in enumerate(choices, 1):
            print(f"{idx}. {choice}")
        
        choice = input("Press Enter to accept the default (1), or type your choice number: ")
        
        if choice == "":
            return 0  # Accept the default (1st choice) if Enter is pressed
        else:
            return int(choice) - 1  # Process the chosen number (adjusted for 0-index)

    def study(self):
        print("\nYou decide to study.")
        self.time_spent_on_study += 3
        self.motivation -= 1
        grade_increase = random.randint(1, 3)
        self.grade += grade_increase
        print(f"Studying improves your grade by {grade_increase} points!")

    def hang_out(self):
        print("\nYou decide to hang out with friends.")
        self.time_spent_on_other_activities += 3
        self.social_life += 1
        self.motivation += 1
        print("Your social life improves, but you lose focus on your studies.")

    def relax(self):
        print("\nYou decide to relax and take a break.")
        self.time_spent_on_other_activities += 2
        self.motivation += 2
        print("You feel recharged and your motivation improves!")

    def procrastinate(self):
        print("\nYou decide to procrastinate and do nothing.")
        self.time_spent_on_other_activities += 2
        self.motivation -= 2
        print("You waste time and your motivation takes a hit.")

    def play(self):
        print("Welcome to the Student Life Adventure!")
        print("You are a student trying to balance academics, social life, and personal time.")
        print("Each round, you will make decisions that impact your grades, social life, and motivation.")

        for round_num in range(1, 6):
            print(f"\nRound {round_num}:")
            self.display_status()

            choices = [
                "Study for an upcoming exam",
                "Hang out with friends",
                "Relax and recharge",
                "Procrastinate and waste time"
            ]
            decision = self.make_choice("What will you do?", choices)

            if decision == 0:
                self.study()
            elif decision == 1:
                self.hang_out()
            elif decision == 2:
                self.relax()
            elif decision == 3:
                self.procrastinate()

            # Check if motivation is too low, game over if motivation drops too much
            if self.motivation <= 0:
                print("\nYour motivation is too low. You failed to balance your life and studies.")
                break

        self.end_game()

    def end_game(self):
        print("\nGame Over! Here's your summary:")
        self.display_status()

        if self.grade >= 12:
            grade_status = "You passed all your exams and have great grades!"
        elif self.grade >= 8:
            grade_status = "You passed some exams, but could have done better."
        else:
            grade_status = "You failed many exams and need to focus more on studying."

        if self.social_life >= 8:
            social_status = "You have a great social life and many friends!"
        elif self.social_life >= 4:
            social_status = "You have some friends, but could socialize more."
        else:
            social_status = "Your social life is lacking; you need to spend more time with others."

        motivation_status = "Your motivation is at a good level!" if self.motivation > 4 else "Your motivation is too low; it might affect your future decisions."

        print(f"\nGrade Status: {grade_status}")
        print(f"Social Life Status: {social_status}")
        print(f"Motivation Status: {motivation_status}")

if __name__ == "__main__":
    game = StudentLifeGame()
    game.play()
