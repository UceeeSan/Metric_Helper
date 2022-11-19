import tkinter
from tkinter import StringVar,ttk #ttk for more modern looking widgets

root=tkinter.Tk()
root.title("Metric Helper")
#Not defining geometry to let tkinter handle it itself
root.iconbitmap("scale.ico")
root.resizable(0,0)
root.config(bg="#45afe3")

#Define fonts and style
entry_font=('Arial',10,"bold")

#Define Functions
def click(events):
    '''To clear input box with mouse click'''
    input_box.config(state='normal')
    input_box.delete(0,tkinter.END)
    input_box.unbind('<Button-1>',clicked)

def convert():
    metric_values={
        'femto':10**-15,
        'pico':10**-12,
        'nano':10**-9,
        'micro':10**-6,
        'mili':10**-3,
        'centi':10**-2,
        'deci':10**-1,
        'base value':10**0,
        'deca':10**1,
        'hecto':10**2,
        'kilo':10**3,
        'mega':10**6,
        'giga':10**9,
        'tera':10**12,
        'peta':10**15
    }
    #Getting user info
    val=float(input_box.get())
    output_box.delete(0,tkinter.END)
    start_prefix=input_dropdown.get()
    end_prefix=output_dropdown.get()

    #Converting
    base_value=val*metric_values[start_prefix]
    converted_value=base_value/metric_values[end_prefix]

    #update output field with answer
    output_box.configure(state="normal")
    output_box.insert(0,str(converted_value))


#Define layout
input_box=tkinter.Entry(root,width=22,font=entry_font,relief="sunken",borderwidth=3)
output_box=tkinter.Entry(root,width=22,state='disable',font=entry_font,relief="sunken",borderwidth=3)
equals_labels=tkinter.Label(root,text="=",bg="#45afe3")

input_box.grid(row=0,column=0,padx=20,pady=10)
equals_labels.grid(row=0,column=1,pady=10)
output_box.grid(row=0,column=2,padx=20,pady=10)

input_box.insert(0,"Enter your quantity here") #This gives a predefined text in input box so that the user may Know where to enter the value
#Click function to clear entrybox
clicked=input_box.bind('<Button-1>',click)
#Create Dropdown box
metric_list=["femto","pico","nano","micro","mili","centi","deci",'base value',"deca","hecto","kilo","mega","giga","tera","peta"]

input_dropdown=ttk.Combobox(root,state="readonly",values=metric_list,font=entry_font,justify='center')        #state readonly prevents from typing in combobox        
output_dropdown=ttk.Combobox(root,state="readonly",values=metric_list,font=entry_font,justify="center")
to_label=tkinter.Label(root,text="to",font=entry_font,bg="#45afe3",fg='white')

input_dropdown.grid(row=1,column=0,padx=20)
to_label.grid(row=1,column=1)
output_dropdown.grid(row=1,column=2,padx=20)


#Conversion button
converter=tkinter.Button(root,text="Convert!",width=20,font=entry_font,bg="#54bcf4",fg="white",borderwidth=5,relief="raised",command=convert) #relief-->button style
#converter=ttk.Button(root,text="Converter",command=convert) ttk style button (optional)
converter.grid(row=2,column=0,columnspan=3,pady=(10,20))

root.mainloop()