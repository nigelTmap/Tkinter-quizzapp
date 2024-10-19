from tkinter import *
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions
    (id INTEGER PRIMARY KEY, question TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT, answer INTEGER)
''')

# Insert sample questions
questions = [
    ("What is the capital of France?", "Paris", "London", "Berlin", "Rome", 1),
    ("Which planet is largest in our solar system?", "Earth", "Saturn", "Jupiter", "Mars", 3),
    ("Who painted the Mona Lisa?", "Michelangelo", "Leonardo da Vinci", "Raphael", "Caravaggio", 2)
]
#cursor.executemany('INSERT INTO questions VALUES (NULL, ?, ?, ?, ?, ?, ?)', questions)
#cursor.execute('DELETE FROM questions')
conn.commit()

class Quiz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Quiz App")
        self.root.geometry("800x600")
        self.question_number = 0
        self.score = 0

        # Get questions from database
        cursor.execute('SELECT * FROM questions')
        self.questions = cursor.fetchall()

        # Display first question
        self.display_question()

        # Start quiz
        self.root.mainloop()

    def display_question(self):
        # Clear previous question
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display current question

        Label(self.root, text="TMAP'S REVISION QUIZ",font=("Arial",24,"bold")).grid(row=0,column=0,pady=20)

        frame = LabelFrame(self.root,padx=100,pady=50,text="QUESTION "+str(self.question_number+1),font=("Arial",12))
        frame.grid(row=2,column=0,padx=20,pady=10)

        question = self.questions[self.question_number]
        Label(frame, text=question[1],font=("Arial",18),wraplength=600).grid(row=3,column=0)

        # Display options
        self.options = [
            Radiobutton(frame, text=question[2],font=("Arial",16)),
            Radiobutton(frame, text=question[3],font=("Arial",16)),
            Radiobutton(frame, text=question[4],font=("Arial",16)),
            Radiobutton(frame, text=question[5],font=("Arial",16))
        ]

        self.selected_option = IntVar()
        for i, option in enumerate(self.options):
            option.grid(column=0)
            option.config(variable=self.selected_option, value=i+1)

        # Display submit button
        Button(frame, text="Submit", command=self.check_answer,font=("Arial",16),bg="#4CAF50",fg="#fff").grid(row=9,column=0,pady=20)

    def check_answer(self):
        selected_option = self.selected_option.get()
             
        # Check answer
        question = self.questions[self.question_number]
        if selected_option == question[6]:
            self.score += 1
            messagebox.showinfo("Correct!", "You answered correctly!")
        else:
            if(question[6]== 1):
             messagebox.showinfo("Incorrect", f"Sorry, the correct answer was {question[2]}")
            elif(question[6]== 2):
             messagebox.showinfo("Incorrect", f"Sorry, the correct answer was {question[3]}")
            elif(question[6]== 3):
             messagebox.showinfo("Incorrect", f"Sorry, the correct answer was {question[4]}")
            elif(question[6]== 4):
             messagebox.showinfo("Incorrect", f"Sorry, the correct answer was {question[5]}")
            else:
             messagebox.showinfo("incorrect","You did not answer the question!!")
            
         # Move to next question
        self.question_number += 1
       # if self.question_number > 2:
        if self.question_number >= len(self.questions):
            self.display_results()
        else:
            self.display_question()

    def display_results(self):
        # Clear previous question
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display results
        Label(self.root, text=f"Quiz finished! Your score is {self.score}/{len(self.questions)}",font=("Arial",20)).pack(pady=80)

if __name__ == "__main__":
    quiz = Quiz()



'''1. Insert new questions into the `questions` table in the SQLite database.
// 2. Update the `questions` list in the code with the new questions.'''
