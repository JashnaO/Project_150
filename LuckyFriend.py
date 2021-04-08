from tkinter import *
#from tkmacosx import
import random
root=Tk()
root.title("Lucky Family Member Wheel")
root.geometry("500x500")
list1=["Hridaan", "Mom", "Dad", "Dadi", "Dada"]
print(list1)
def random_number():
    random_no=random.randint(0,4)
    print(random_no)
    random_lucky=list1[random_no]
    print("Your lucky member is:" + random_lucky)
    btn=Button(root)
    btn=Button(root, text="Who is your Lucky Member?",command=random_number)
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()