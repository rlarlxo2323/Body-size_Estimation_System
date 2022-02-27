import PIL
import Read_HData
import Regression
from tkinter import *
import tkinter.filedialog
import tkinter.font
from PIL import ImageTk, Image
from tkinter import messagebox

window = Tk()
window.title("Benefit")
window.geometry("950x570")#"930x590"
window.resizable(False, False)

Sex = IntVar()
men_W = StringVar()
men_A = StringVar()
women_W = StringVar()
women_A = StringVar()
global Height

font = tkinter.font.Font(family="Arial", size=13, weight="bold", slant="italic")
font2 = tkinter.font.Font(family="Arial", size=12, weight="bold", slant="italic")


w0 = Canvas(window, width=3000, height=3000)
w0.pack()
w0.create_rectangle(0, 0, 1000, 1100, fill='sky blue')

img = PhotoImage(file="real.png")
w = Label(window, image=img)
w.place(x=0, y=0)

frame = Canvas(window, width=414, height=441)
frame.place(x=0, y=123) #(x=0, y=140)
image = Image.open("bene2.png")
image = image.resize((414, 450), PIL.Image.ANTIALIAS) #414, 441
photo = ImageTk.PhotoImage(image)
frame.create_image(0, 0, anchor=NW, image=photo)


def off():
    global window
    global button_5

    try:
        if 'normal' == window.state():
            window.destroy()
    finally:
        window.mainloop()


def tall():
    window.file = tkinter.filedialog.askopenfile(
        initialdir='path',
        title='select file',
        filetypes=(('png files', '*.png'), ('all files', '*.*')))
    file_name = window.file.name
    H_data = str(Read_HData.HData(file_name))
    global Height
    Height = H_data
    t1 = Label(window, text=H_data+"cm", font=font, fg="white", bg="sky blue")
    t1.place(x=780, y=24)
    newim = Image.open(file_name)
    newimage = newim.resize((430, 450), PIL.Image.ANTIALIAS)#414, 441
    newphoto = ImageTk.PhotoImage(newimage)
    frame.config(frame.create_image(0, 0, anchor=NW, image=newphoto))


def im():
    global Data
    if Sex.get() == 1:
        if ('Height' not in globals()) or (men_W.get()=='') or (men_A.get()==''):
            messagebox.showwarning("Warning", "입력정보를 확인 해주세요.")
        else:
            Data = Regression.Model(float(Sex.get()), float(Height), float(men_W.get()), float(men_A.get()))
            shoulder = Data[0]
            chest = Data[1]
            waist = Data[2]
            arm = Data[3]
            hip = Data[4]
            leg = Data[5]
            
            t8 = Label(window, text="                   Result[cm]".format(shoulder), font=font2, fg="white", bg="sky blue")
            t8.place(x=600, y=180)
            t9 = Label(window, text="_________________", font=font, fg="white", bg="sky blue")
            t9.place(x=600, y=198)
            t2 = Label(window, text="shoulder         {}".format(shoulder), font=font, fg="white", bg="sky blue")
            t2.place(x=600, y=228)
            t3 = Label(window, text="chest              {}".format(chest), font=font, fg="white", bg="sky blue")
            t3.place(x=600, y=278)
            t4 = Label(window, text="waist              {}".format(waist), font=font, fg="white", bg="sky blue")
            t4.place(x=600, y=328)
            t5 = Label(window, text="arm                {}".format(arm), font=font, fg="white", bg="sky blue")
            t5.place(x=600, y=378)
            t6 = Label(window, text="hip                 {}".format(hip), font=font, fg="white", bg="sky blue")
            t6.place(x=600, y=428)
            t7 = Label(window, text="leg                 {}".format(leg), font=font, fg="white", bg="sky blue")
            t7.place(x=600, y=478)
            
            #t8 = Label(window, text="고객님의 추천 옷사이즈는 L 사이즈 입니다.", font=font, fg="white", bg="sky blue")
            #t8.place(x=500, y=478)
    else:
        if ('Height' not in globals()) or (women_W.get()=='') or (women_A.get()==''):
            messagebox.showwarning("Warning", "입력정보를 확인 해주세요.")
        else:
            Data = Regression.Model(float(Sex.get()), float(Height), float(women_W.get()), float(women_A.get()))
            shoulder = Data[0]
            chest = Data[1]
            waist = Data[2]
            arm = Data[3]
            hip = Data[4]
            leg = Data[5]
            
            t8 = Label(window, text="                   Result[cm]".format(shoulder), font=font2, fg="white", bg="sky blue")
            t8.place(x=600, y=180)
            t9 = Label(window, text="_________________", font=font, fg="white", bg="sky blue")
            t9.place(x=600, y=198)
            t2 = Label(window, text="shoulder         {}".format(shoulder), font=font, fg="white", bg="sky blue")
            t2.place(x=600, y=228)
            t3 = Label(window, text="chest              {}".format(chest), font=font, fg="white", bg="sky blue")
            t3.place(x=600, y=278)
            t4 = Label(window, text="waist              {}".format(waist), font=font, fg="white", bg="sky blue")
            t4.place(x=600, y=328)
            t5 = Label(window, text="arm                {}".format(arm), font=font, fg="white", bg="sky blue")
            t5.place(x=600, y=378)
            t6 = Label(window, text="hip                 {}".format(hip), font=font, fg="white", bg="sky blue")
            t6.place(x=600, y=428)
            t7 = Label(window, text="leg                 {}".format(leg), font=font, fg="white", bg="sky blue")
            t7.place(x=600, y=478)

# =============================================================================
#             t2 = Label(window, text="shoulder         {}".format(shoulder), font=font, fg="white", bg="sky blue")
#             t2.place(x=600, y=178)
#             t3 = Label(window, text="chest              {}".format(chest), font=font, fg="white", bg="sky blue")
#             t3.place(x=600, y=228)
#             t4 = Label(window, text="waist              {}".format(waist), font=font, fg="white", bg="sky blue")
#             t4.place(x=600, y=278)
#             t5 = Label(window, text="arm                {}".format(arm), font=font, fg="white", bg="sky blue")
#             t5.place(x=600, y=328)
#             t6 = Label(window, text="hip                 {}".format(hip), font=font, fg="white", bg="sky blue")
#             t6.place(x=600, y=378)
#             t7 = Label(window, text="leg                 {}".format(leg), font=font, fg="white", bg="sky blue")
#             t7.place(x=600, y=428)
#             t8 = Label(window, text="고객님의 추천 옷사이즈는 L 사이즈 입니다.", font=font, fg="white", bg="sky blue")
#             t8.place(x=500, y=478)
# =============================================================================


def men():
    we = Label(window, text="몸무게를 입력하세요", font=font, fg="white", bg="sky blue", width=20)
    we.place(x=600, y=72)
    ww = Label(window, text="kg", font=font, fg="white", bg="sky blue", width=20)
    ww.place(x=805, y=72)

    we1 = Entry(window, width=10, textvariable=men_W)
    we1.place(x=816, y=76)

    we2 = Label(window, text="나이를 입력하세요", font=font, fg="white", bg="sky blue", width=20)
    we2.place(x=600, y=100)
    ww2 = Label(window, text="세", font=font, fg="white", bg="sky blue", width=20)
    ww2.place(x=805, y=100)

    we3 = Entry(window, width=10, textvariable=men_A)
    we3.place(x=816, y=104)


def women():
    we4 = Label(window, text="몸무게를 입력하세요", font=font, fg="white", bg="sky blue", width=20)
    we4.place(x=600, y=72)
    ww = Label(window, text="kg", font=font, fg="white", bg="sky blue", width=20)
    ww.place(x=805, y=72)

    we5 = Entry(window, width=10, textvariable=women_W)
    we5.place(x=816, y=76)

    we6 = Label(window, text="나이를 입력하세요", font=font, fg="white", bg="sky blue", width=20)
    we6.place(x=600, y=100)
    ww2 = Label(window, text="세", font=font, fg="white", bg="sky blue", width=20)
    ww2.place(x=805, y=100)

    we7 = Entry(window, width=10, textvariable=women_A)
    we7.place(x=816, y=104)


button_1 = Button(window, text="키 정보 가져오기", command=tall, font=font, fg="white", bg="sky blue", width=20)
button_1.place(x=465, y=18)#x=480, y=18
button_3 = Button(window, text="내 신체 지수 정보확인", command=im, font=font, fg="white", bg="sky blue", width=20, )
button_3.place(x=576, y=137)#x=570, y=137)
button_5 = Button(window, text="종료", command=off, font=font, fg="white", bg="sky blue", width=15)
button_5.place(x=598, y=525)#x=595, y=525

btn_men = Radiobutton(window, text="남", value=1, variable=Sex, command=men, font=font, fg="black", bg="sky blue",
                      width=5)
btn_men.place(x=450, y=67)

btn_women = Radiobutton(window, text="여", value=2, variable=Sex, command=women, font=font, fg="black",
                        bg="sky blue", width=5)
btn_women.place(x=520, y=67)

window.mainloop()