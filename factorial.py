import tkinter as tk
def fun():
    label.config(text="good bye")
root=tk.Tk()
root.title("saii")
label=tk.Label(root,text="Hello")
label.pack()
button=tk.Button(root,text="change message",command=fun)
button.pack()
root.mainloop()

n=int(input("enter number:"))
fact=1
for i in (1,n+1):
    fact=fact*i
print("factorial of",n,fact)

