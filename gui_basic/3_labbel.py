from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="GUI_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    # 함수 내에서 포토값을 바꾸려면 변수를 글로벌로 지정해야한다.
    global photo2
    photo2 = PhotoImage(file="GUI_basic/image2.png")
    label2.config(image=photo2)

btn2 = Button(root, text="클릭", command=change)
btn2.pack()


root.mainloop()