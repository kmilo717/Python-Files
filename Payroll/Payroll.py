from tkinter import ttk
from tkinter import *

import sqlite3

class Payroll:

    db_name='Payroll/Payroll.db'
        
    #Enter data
    def __init__(self, window):
        self.wind=window
        self.wind.title('Payroll SYSTEM.exe')
        
        #Creating a frame container
        frame=LabelFrame(self.wind, text='Query a new payroll')
        frame.grid(row=0, column=0, columnspan=5, pady=5)
    
        #Identification Number Input
        Label(frame, text='Enter your Identification Number (only numbers, without special characters such as points): ').grid(row=1, column=0)
        self.PayIdentification=Entry(frame)
        self.PayIdentification.focus()
        
    
        #Lastnames Input
        Label(frame,  text='Enter your last names: ').grid(row=2, column=0)
        self.PayLastname=Entry(frame)
        self.PayLastname.grid(row=2, column=1)
        
        #Firstname Input
        Label(frame,  text='Enter your first names: ').grid(row=3, column=0)
        self.PayFirstname=Entry(frame)
        self.PayFirstname.grid(row=3, column=1)
        '''
        #Salary Input
        Label(frame,  text='Enter the value of your monthly salary: $').grid(row=4, column=0)
        self.PaySalary=Entry(frame)
        self.PaySalary.grid(row=4, column=1)
        
        #Worked days Input
        Label(frame,  text='Enter the number of days worked in the month: ').grid(row=4, column=0)
        self.PayDays=Entry(frame)
        self.PayDays.grid(row=4, column=1)
        '''
        #Query payroll Button
        ttk.Button(frame, text='Query payroll', command=self.add_payroll).grid(row=6, columnspan=2, sticky=W+E)

        #Output messages
        self.message=Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)

        #Table
        self.tree=ttk.Treeview(height=10, columns=5)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Identification', anchor=CENTER)
        self.tree.heading('#1', text='Name', anchor=CENTER)

        #Buttons
        ttk.Button(text='Delete', command=self.delete_PayQuery).grid(row=5, column=0, sticky=W+E)
        ttk.Button(text='Update', command=self.edit_PayQuery).grid(row=5, column=1, sticky=W+E)

        #Filling rows
        self.get_Payroll()

    def run_Payroll(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor=conn.cursor()
            result=cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_Payroll(self):
        #Cleaning table
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #Quering data
        query='SELECT * FROM Payroll ORDER BY PayFirstname DESC'
        db_rows=self.run_Payroll(query)
        print(db_rows)
        #Filling data
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])
            
    def validation(self):
        return len(self.PayIdentification.get())!=0 and len(self.PayLastname.get())!=0 #and len(self.PayFirstname.get())!=0 and len(self.Salary.get())!=0 and len(self.PayDays.get())!=0

    def add_payroll(self):
        if self.validation():
            query='INSERT INTO Payroll VALUES (NULL, ?, ?)'
            parameters=(self.PayLastname.get(), self.PayLastname.get())
            self.run_Payroll(query, parameters)
            self.message['text']='Mr(s). {}, your data were entered succesfully'.format(self.PayFirstname.get)
            self.PayFirstname.delete(0, END)
            self.PayFirstname.delete(0, END)
            self.PayFirstname.delete(0, END)
            self.PayFirstname.delete(0, END)
            self.PayFirstname.delete(0, END)
        else:
            self.message['text']='It is necessary to enter all the data'
        self.get_Payroll()

    def delete_PayQuery(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text']='Select a register'
            return
        self.message['text']=''
        PayIdentification=self.tree.item(self.tree.selection())['text']
        query='DELETE FROM Payroll WHERE PayIdentification=?'
        self.run_Payroll(query, (PayIdentification, ))
        self.message['text']='Register with Identification Number {} was deleted succesfully'.format(PayIdentification)
        self.get_Payroll

    def edit_PayQuery(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text']='Select a register'
            return
        PayLastname=self.tree.item(self.tree.selection())['text']
        previousPayLastname=self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind=Toplevel()
        self.edit_wind.title='Edit Register'

        #Previous Lastname
        Label(self.edit_wind, text='Previous Lastname: ').grid(row=0, column=1)
        Entry(self.edit_PayQuery, textvariable=StringVar(self.edit_wind, value=PayLastname), state='readonly').grid(row=0, column=2)
        

        #New Lastname
        Label

if __name__=='__main__':
    window=Tk()
    application=Payroll(window)
    window.mainloop()