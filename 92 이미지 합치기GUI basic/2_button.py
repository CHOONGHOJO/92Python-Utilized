from tkinter import *

root = Tk()
root.title("나도코딩 GUI")
root.geometry("640x480") # 가로 * 세로

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼22222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼41234567890") # 너비, 높이 고정됨
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="/home/cjoe731/Desktop/python(NadoCoding)/무료 강의 (활용편2:이미지 합치기GUI)basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
  print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
