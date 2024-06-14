from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)   
        cursor.execute('INSERT INTO tasks VALUES (?)', (task_string,))    
        list_update()    
        task_field.delete(0, 'end')  
    
def list_update():    
    task_listbox.delete(0, 'end')  
    for task in tasks:    
        task_listbox.insert('end', task)  
  
def delete_task():  
    try:  
        text = task_listbox.get(task_listbox.curselection())    
        if text in tasks:  
            tasks.remove(text)    
            list_update()   
            cursor.execute('DELETE FROM tasks WHERE title = ?', (text,))
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
def delete_all_tasks():  
    if messagebox.askyesno('Delete All', 'Are you sure?'):  
        tasks.clear()
        cursor.execute('DELETE FROM tasks')
        list_update()
   
def close():    
    print(tasks)   
    guiWindow.destroy()  
    
def retrieve_database():    
    tasks.clear()
    for row in cursor.execute('SELECT title FROM tasks'):    
        tasks.append(row[0])  

if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("TDL")  
    guiWindow.geometry("665x400+680+50")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg="#05f739")  
   
    connection = sql.connect('listOfTasks.db')   
    cursor = connection.cursor()   
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')  
    
    tasks = []  
    
    functions_frame = Frame(guiWindow, bg="#FFDF00") 
    functions_frame.pack(side="top", expand=True, fill="both")  
    Label(functions_frame, text="TO-DO LIST", font=("Segoe UI Black", 18, "bold"), bg="#FFDF00", fg="#ff0000").place(x=260, y=10)
    Label(functions_frame, text="Enter the Task:", font=("Times New Romen", 14, "bold"), bg="#FFDF00", fg="#0d0c0c").place(x=50, y=51)  
        
    task_field = Entry(functions_frame, font=("Times New Romen", 14), width=35, fg="black", bg="white")    
    task_field.place(x=210, y=53)  
    
    Button(functions_frame, text="Add", width=10, bg='#098aed', font=("Arial", 14, "bold"), command=add_task).place(x=30, y=325)  
    Button(functions_frame, text="Remove", width=10, bg='#098aed', font=("Arial", 14, "bold"), command=delete_task).place(x=190, y=325)  
    Button(functions_frame, text="Delete All", width=10, bg='#098aed', font=("Arial", 14, "bold"), command=delete_all_tasks).place(x=350, y=325)  
    Button(functions_frame, text="Close", width=10, bg='#098aed', font=("Arial", 14, "bold"), command=close).place(x=510, y=325)  

    task_listbox = Listbox(functions_frame, width=70, height=10, font=("Times New Romen", 12), selectmode='SINGLE', bg="white", fg="black", 
                           selectbackground="#5fff57", selectforeground="black")    
    task_listbox.place(x=15, y=100)  
    
    retrieve_database()  
    list_update()    
    guiWindow.mainloop()    
    connection.commit()  
    cursor.close()
    