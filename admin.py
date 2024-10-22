from tkinter import *
from tkinter import messagebox
import sqlite3

# Connect to database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions
    (id INTEGER PRIMARY KEY, question TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT, answer INTEGER)
''')


# Function to add data to database
def add_question():
    question = question_entry.get()
    option1 = option1_entry.get()
    option2 = option2_entry.get()
    option3 = option3_entry.get()
    option4 = option4_entry.get()
    answer = answer_var.get()
        
       
    question_entry.delete(0,END)
    option1_entry.delete(0,END)
    option2_entry.delete(0,END)
    option3_entry.delete(0,END)
    option4_entry.delete(0,END)
    answer_var.set(None)
    
   
    
    
    cursor.execute('''
        INSERT INTO questions (question, option1, option2, option3, option4, answer)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option1, option2, option3, option4, answer))

    conn.commit()
    messagebox.showinfo("Success", "Question added successfully")

    

    
    
# Create UI
root = Tk()
root.title("Quiz App")
root.geometry("650x550")


def manage_records():
    global manage
    manage = Tk()
    manage.title("Manage Records")
    manage.geometry("400x300")

    show_label = Label(manage, text="Show all questions",font=("Arial",16,"bold"))
    show_label.grid(row=0,column=0,padx=20,pady=10)

    show_button = Button(manage, text="SHOW", command=querry,font=("Arial",16),bg="#4CAF50",fg="#fff")
    show_button.grid(row=1,column=0,pady=10)

    update_label = Label(manage, text="Update/delete question",font=("Arial",16,"bold"))
    update_label.grid(row=4,column=0,padx=20,pady=10)

    find_label = Label(manage, text="Search question by number",font=(14))
    find_label.grid(row=5,column=0,padx=20,pady=10)
     
    global find_entry 
    find_entry = Entry(manage,width=5,font=("Arial",12))
    find_entry.grid(row=5,column=1,)

    
    delete_button = Button(manage, text="DELETE", command=delete,font=("Arial",16),bg="#4CAF50",fg="#fff")
    delete_button.grid(row=7,column=0,pady=10)


    update_button = Button(manage, text="UPDATE", command=edit,font=("Arial",16),bg="#4CAF50",fg="#fff")
    update_button.grid(row=7,column=1,pady=10)

    manage.mainloop()

def querry():
    show = Tk()
    show.title("Show Records")
    show.geometry("900x600")
    
        # Connect to database
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT *,oid FROM questions")
    records = cursor.fetchall()

    conn.commit()
    
    
    print_records =''
    for record in records:
        print_records += str(record[0])+". "+str(record[1])+"\n"

    qtitle_label = Label(show,text="ALL QUESTIONS",justify="left",font=("Ariel",20,"bold"))
    qtitle_label.grid(row=0,column=0,padx=20)

    querry_label = Label(show,text=print_records,anchor="w",font=("Ariel",16))
    querry_label.grid(row=2,column=0,padx=20)
   
    show.mainloop()

def delete():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("DELETE from questions WHERE oid = "+ find_entry.get())
    find_entry.delete(0,END)
    conn.commit()
    messagebox.showinfo("successful","Question has been deleted")
    
    manage.destroy()

def edit():
    global editor
    editor = Tk()
    editor.title("update Records")
    editor.geometry("650x550")

    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    record_id = find_entry.get()
    cursor.execute("SELECT * FROM questions WHERE oid="+ record_id)
    records = cursor.fetchall()

    conn.commit()



    Label(editor, text="Update a question",font=("Arial",24,"bold")).grid(row=0,column=0,pady=20,padx=20,columnspan=2)
    
    global question_entr
    global option1_entr
    global option2_entr
    global option3_entr
    global option4_entr
    global answe_var

    question_label = Label(editor, text="Question",font=("Arial",16,"bold"))
    question_label.grid(row=2,column=0,padx=20,pady=10)
    question_entr = Entry(editor,width=30,font=("Arial",12))
    question_entr.grid(row=2,column=1,)

    option1_label = Label(editor, text="Option 1:",font=("Arial",14))
    option1_label.grid(row=5,column=0,padx=20)
    option1_entr = Entry(editor,width=30,font=("Arial",12))
    option1_entr.grid(row=5,column=1,)

    option2_label = Label(editor, text="Option 2:",font=("Arial",14))
    option2_label.grid(row=6,column=0,padx=20)
    option2_entr = Entry(editor,width=30,font=("Arial",12))
    option2_entr.grid(row=6,column=1,)

    option3_label = Label(editor, text="Option 3:",font=("Arial",14))
    option3_label.grid(row=7,column=0,padx=20)
    option3_entr =Entry(editor,width=30,font=("Arial",12))
    option3_entr.grid(row=7,column=1,)

    option4_label = Label(editor, text="Option 4:",font=("Arial",14))
    option4_label.grid(row=8,column=0,padx=20)
    option4_entr = Entry(editor,width=30,font=("Arial",12))
    option4_entr.grid(row=8,column=1,)

   # answer_label = Label(editor, text="Correct Answer",font=("Arial",16,"bold"))
   # answer_label.grid(row=10,column=0,pady=10,padx=20)
    answe_var = IntVar()
   #answe_option1 = Radiobutton(editor, text="Option 1", variable=answe_var, value=1,font=(12))
    #answe_option1.grid(row=11,column=0,padx=20)
    #answe_option2 = Radiobutton(editor, text="Option 2", variable=answe_var, value=2,font=(12))
    #answe_option2.grid(row=11,column=1,padx=20)
    #answe_option3 = Radiobutton(editor, text="Option 3", variable=answe_var, value=3,font=(12))
    #answe_option3.grid(row=12,column=0,padx=20)
    #answe_option4 = Radiobutton(editor, text="Option 4", variable=answe_var, value=4,font=(12))
    #answe_option4.grid(row=12,column=1,padx=20)


    for record in records:
        question_entr.insert(0,record[1])
        option1_entr.insert(0,record[2])
        option2_entr.insert(0,record[3])
        option3_entr.insert(0,record[4])
        option4_entr.insert(0,record[5])
    
    
    

    edit_button = Button(editor, text="Save Changes", command=update,font=("Arial",16),bg="#4CAF50",fg="#fff")
    edit_button.grid(row=13,column=1,pady=10)
    
    editor.mainloop()

def update():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
     
    record_id = find_entry.get()
    cursor.execute('''UPDATE questions SET
              question= :question, 
              option1=  :option1,
              option2=  :option2,
              option3=  :option3,
              option4=  :option4,
              answer =  :answer

              WHERE oid =:oid  ''',
              {
              'question': question_entr.get(),
              'option1': option1_entr.get(),
              'option2':option2_entr.get(),  
              'option3':option3_entr.get(), 
              'option4':option4_entr.get(),
              'answer' : answe_var.get(),
         
              'oid': record_id }
    )

    conn.commit()


    editor.destroy()
    



Label(root, text="TMAP'S REVISION QUIZ ADMIN PANEL",font=("Arial",24,"bold")).grid(row=0,column=0,pady=20,padx=20,columnspan=2)

question_label = Label(root, text="Question",font=("Arial",16,"bold"))
question_label.grid(row=2,column=0,padx=20,pady=10)
question_entry = Entry(root,width=30,font=("Arial",12))
question_entry.grid(row=2,column=1,)

option1_label = Label(root, text="Option 1:",font=("Arial",14))
option1_label.grid(row=5,column=0,padx=20)
option1_entry = Entry(root,width=30,font=("Arial",12))
option1_entry.grid(row=5,column=1,)

option2_label = Label(root, text="Option 2:",font=("Arial",14))
option2_label.grid(row=6,column=0,padx=20)
option2_entry = Entry(root,width=30,font=("Arial",12))
option2_entry.grid(row=6,column=1,)

option3_label = Label(root, text="Option 3:",font=("Arial",14))
option3_label.grid(row=7,column=0,padx=20)
option3_entry =Entry(root,width=30,font=("Arial",12))
option3_entry.grid(row=7,column=1,)

option4_label = Label(root, text="Option 4:",font=("Arial",14))
option4_label.grid(row=8,column=0,padx=20)
option4_entry = Entry(root,width=30,font=("Arial",12))
option4_entry.grid(row=8,column=1,)

answer_label = Label(root, text="Correct Answer",font=("Arial",16,"bold"))
answer_label.grid(row=10,column=0,pady=10,padx=20)
answer_var = IntVar()
answer_option1 = Radiobutton(root, text="Option 1", variable=answer_var, value=1,font=(12))
answer_option1.grid(row=11,column=0,padx=20)
answer_option2 = Radiobutton(root, text="Option 2", variable=answer_var, value=2,font=(12))
answer_option2.grid(row=11,column=1,padx=20)
answer_option3 = Radiobutton(root, text="Option 3", variable=answer_var, value=3,font=(12))
answer_option3.grid(row=12,column=0,padx=20)
answer_option4 = Radiobutton(root, text="Option 4", variable=answer_var, value=4,font=(12))
answer_option4.grid(row=12,column=1,padx=20)


add_button = Button(root, text="Add Question", command=add_question,font=("Arial",16),bg="#4CAF50",fg="#fff")
add_button.grid(row=13,column=1,pady=10)

manage_button = Button(root, text="Manage Existing Records", command=manage_records,font=("Arial",16),bg="#4CAF50",fg="#fff")
manage_button.grid(row=14,column=0,pady=10,columnspan=2,ipadx=82)

root.mainloop()


