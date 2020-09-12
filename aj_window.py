
from tkinter import *
import random
from win32com.client import Dispatch
from ques1 import *
from ans1 import *


def quegen():
    global list1
    root.destroy()
    while (len(list1)<100):
        x=random.randint(0,99)
        if x in list1:
            continue
        else:
            list1.append(x)
    print(list1)
def quegen_1():
    root.destroy()
    global list1
    for i in range(0,10):
        list1.append(i)
        print(list1)
def quegen_2():
    root.destroy()
    global list1
    for i in range(10,20):
        list1.append(i)
        print(list1)

def quegen_3():
    root.destroy()
    global list1
    for i in range(20,30):
        list1.append(i)
        print(list1)

def quegen_4():
    root.destroy()
    global list1
    for i in range(30,40):
        list1.append(i)
        print(list1)

def quegen_5():
    root.destroy()
    global list1
    for i in range(40,50):
        list1.append(i)
        print(list1)

def quegen_6():
    root.destroy()
    global list1
    for i in range(50,60):
        list1.append(i)
        print(list1)

def quegen_7():
    root.destroy()
    global list1
    for i in range(60,70):
        list1.append(i)
        print(list1)

def quegen_8():
    root.destroy()
    global list1
    for i in range(70,80):
        list1.append(i)
        print(list1)

def quegen_9():
    root.destroy()
    global list1
    for i in range(80,90):
        list1.append(i)
        print(list1)

def quegen_10():
    root.destroy()
    global list1
    for i in range(90,100):
        list1.append(i)
        print(list1)

def speak(Str):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.speak(Str)


user_ans=[]
list1=[]
ques=1
y=[]
i=1
a=1


def showresult():
    global userinteract
    global name_input, list1
    questionframe.destroy()
    topansframe.destroy()
    bottomansframe.destroy()
    userinteract.destroy()

    def calculate():
        global list1, correct_ans, user_ans
        x = 0
        score = 0

        for i in list1:
            if user_ans[x] == correct_ans[i]:
                score = score + 5
            x += 1

        def exitwindow():
            exit()

        if len(list1) == 100:
            photoframe = Frame(mainwindow2, bg="black")
            photoframe.pack(fill=X)

            img = PhotoImage(file="python3.png")
            imglabel = Label(photoframe, image=img)
            imglabel.image = img
            imglabel.pack()

            mainframe = Frame(mainwindow2, bg="black")
            mainframe.pack(fill=BOTH)

            if score >= 450:
                label1 = Label(mainframe,
                    text=" W E L L     P L A Y E D  ,   Y O U    H A V E    G O O D    E X P E R I E N C E.",
                    padx=200, fg="red", font="cascade 20 bold", bg="black")
                label1.pack(pady=30, )

            elif score >= 300:
                label2 = Label(mainframe,
                    text="H A V E    G O O D   E X P E R I E N C E    A N D    N E E D    I M P R O V E M E N T.",
                    padx=200, fg="red", font="cascade 20 bold", bg="black", )
                label2.pack(pady=30)
            elif score <= 295:
                label1 = Label(mainframe, text=" Y O U   N E E D   M O R E   H A R D   W O R K . ",
                    padx=200, fg="red", font="cascade 20 bold", bg="black", )
                label1.pack(pady=30, )

            score_display = Frame(mainwindow2, bg="black")
            score_display.pack(fill=BOTH)

            title_name = Label(score_display, text=" N A M E ", fg="blue",
                bg="black",font="cascade 30 bold ", padx=5)
            title_name.grid(row=0, column=0, pady=15)

            title_score = Label(score_display, text=" S C O R E ", fg="blue",
                bg="black",font="cascade 30 bold ")
            title_score.grid(row=0, column=1, padx=170, pady=20, )

            player_name = Label(score_display, text=name_input, bg="black",
                fg="green", width=30,font="cascade 25 bold ", padx=10)
            player_name.grid(row=1, column=0, pady=(30, 50))

            label2 = Label(score_display, text=f"{score} / 500", fg="green",
                bg="black",font="cascade 20 bold",width=10, )
            label2.grid(row=1, column=1, padx=170, pady=(30, 50))

            exit_frame = Frame(mainwindow2, bg="black")
            exit_frame.pack(fill=BOTH, expand=TRUE)

            exit_button = Button(exit_frame, text=" E X I T ", fg="red",
                bg="black",font="cascade 20 bold", width=10, command=exitwindow)
            exit_button.grid(row=0, column=0, padx=(600, 0))

        if score <= 35:
            photoframe = Frame(mainwindow2, bg="black")
            photoframe.pack(fill=X)

            img = PhotoImage(file="python1.png")
            imglabel = Label(photoframe, image=img)
            imglabel.image = img
            imglabel.pack()

            mainframe = Frame(mainwindow2, bg="black")
            mainframe.pack(fill=BOTH)

            score_display = Frame(mainwindow2, bg="black")
            score_display.pack(fill=BOTH)

            exit_frame = Frame(mainwindow2, bg="black")
            exit_frame.pack(fill=BOTH, expand=TRUE)

            label1 = Label(mainframe, text=" Y O U   N E E D   M O R E   H A R D   W O R K . ",
                padx=200,fg="red", font="cascade 20 bold", bg="black", )
            label1.grid(row=0, column=0, pady=30)

            title_name = Label(score_display, text=" N A M E ", fg="blue", bg="black",
                               font="cascade 30 bold ", padx=5)
            title_name.grid(row=0, column=0, pady=15)

            title_score = Label(score_display, text=" S C O R E ", fg="blue", bg="black",
                                font="cascade 30 bold ")
            title_score.grid(row=0, column=1, padx=(300, 0), pady=20, )

            player_name = Label(score_display, text=name_input, bg="black", fg="green",
                width=30,font="cascade 25 bold ", padx=10)
            player_name.grid(row=1, column=0, pady=(30, 50))

            label2 = Label(score_display, text=f"{score} / 50", fg="green", bg="black",
                font="cascade 20 bold",width=10, )
            label2.grid(row=1, column=1, padx=(300, 0), pady=(30, 0))

            exit_button = Button(exit_frame, text=" E X I T ", fg="red",
                    bg="black",font="cascade 20 bold", width=10, command=exitwindow)
            exit_button.grid(row=0, column=0, padx=(600, 0))
        elif score <= 45:
            photoframe = Frame(mainwindow2, bg="black")
            photoframe.pack(fill=X)

            img = PhotoImage(file="python2.png")
            imglabel = Label(photoframe, image=img)
            imglabel.image = img
            imglabel.pack()

            mainframe = Frame(mainwindow2, bg="black")
            mainframe.pack(fill=BOTH)

            label2 = Label(mainframe,
                text="H A V E    G O O D   E X P E R I E N C E    A N D    N E E D    I M P R O V E M E N T.",
                padx=200, fg="red", font="cascade 20 bold", bg="black", )
            label2.grid(row=0, column=0, pady=30)

            score_display = Frame(mainwindow2, bg="black")
            score_display.pack(fill=BOTH)

            title_name = Label(score_display, text=" N A M E ", fg="blue", bg="black",
                font="cascade 30 bold ", padx=5)
            title_name.grid(row=0, column=0, pady=15)

            title_score = Label(score_display, text=" S C O R E ", fg="blue", bg="black",
                                font="cascade 30 bold ")
            title_score.grid(row=0, column=1, padx=200, pady=20, )

            player_name = Label(score_display, text=name_input, bg="black",
                    fg="green", width=30,font="cascade 25 bold ", padx=10)
            player_name.grid(row=1, column=0, pady=(30, 50))

            label2 = Label(score_display, text=f"{score} / 50", fg="green",
                    bg="black", font="cascade 20 bold",width=10, )
            label2.grid(row=1, column=1, padx=200, pady=(30, 50))

            exit_frame = Frame(mainwindow2, bg="black")
            exit_frame.pack(fill=BOTH, expand=TRUE)

            exit_button = Button(exit_frame, text=" E X I T ", fg="red", bg="black",
                                 font="cascade 20 bold", width=10, command=exitwindow)
            exit_button.grid(row=0, column=0, padx=(600, 0))
        elif score == 50:
            photoframe = Frame(mainwindow2, bg="black")
            photoframe.pack(fill=X)

            img = PhotoImage(file="python3.png")
            imglabel = Label(photoframe, image=img)
            imglabel.image = img
            imglabel.pack()

            mainframe = Frame(mainwindow2, bg="black")
            mainframe.pack(fill=BOTH)

            label3 = Label(mainframe,
                   text=" W E L L     P L A Y E D  ,   Y O U    H A V E    G O O D    E X P E R I E N C E.",
                   padx=200, fg="red", font="cascade 20 bold", bg="black")
            label3.grid(row=0, column=0, pady=30, )

            score_display = Frame(mainwindow2, bg="black")
            score_display.pack(fill=BOTH)

            title_name = Label(score_display, text=" N A M E ", fg="blue",
                    bg="black",font="cascade 30 bold ", padx=5)
            title_name.grid(row=0, column=0, pady=15)

            title_score = Label(score_display, text=" S C O R E ", fg="blue",
                    bg="black",font="cascade 30 bold ")
            title_score.grid(row=0, column=1, padx=200, pady=20, )

            player_name = Label(score_display, text=name_input, bg="black",
                    fg="green", width=30,font="cascade 25 bold ", padx=10)
            player_name.grid(row=1, column=0, pady=(30, 50))

            label2 = Label(score_display, text=f"{score} / 50", fg="green",
                    bg="black", font="cascade 20 bold",width=10, )
            label2.grid(row=1, column=1, padx=200, pady=(30, 50))

            exit_frame = Frame(mainwindow2, bg="black")
            exit_frame.pack(fill=BOTH, expand=TRUE)
            exit_button = Button(exit_frame, text=" E X I T ", fg="red", bg="black",
                                 font="cascade 20 bold", width=10, command=exitwindow)
            exit_button.grid(row=0, column=0, padx=(600, 0))

    calculate()
# def speak(Str):
#     speak=Dispatch(("SAPI.SpVoice"))
#     speak.speak(Str)

def imagedisplay(list1):
    global label, l1, l2, l3, l4, python,var,name_input
    global  topframe , topansframe,bottomansframe,questionframe,userinteract
    global mainwindow2,f1,f2,f3,f4
    mainwindow2 = Tk()
    mainwindow2.minsize(1550,850)

    questionframe=Frame(mainwindow2,pady=(20),bg="black",)
    questionframe.pack(fill="x")

    #  1.Top ans frame
    topansframe = Frame(mainwindow2, bg="black",pady=(20))
    topansframe.pack( fill="x")

    # 2. bottom ans frame
    bottomansframe = Frame(mainwindow2,bg="black")
    bottomansframe.pack(expand=TRUE, fill=BOTH,)

    # 1.a left frame
    topleftframe=Frame(topansframe,bg="blue")
    topleftframe.pack(side=LEFT,anchor="nw",padx=(30,70))

    sizelabel=Label(topleftframe,text="                                                                                                      "
      "                                                                                                 "
                    ,bg="black",height=0)
    sizelabel.pack()

    # 1.b Right frame
    toprightframe=Frame(topansframe,bg="blue")
    toprightframe.pack(side=RIGHT,expand=TRUE,anchor="nw")

    sizelabel = Label(toprightframe,
                      text="                                                                                                                        "
                           "                                                        "
                      , bg="black", height=0)
    sizelabel.pack()

    # 2.a left frame
    bottomleftframe=Frame(bottomansframe,bg="blue")
    bottomleftframe.pack(side=LEFT,anchor="nw",padx=(30,70))

    sizelabel = Label(bottomleftframe,
        text="                                                                                                                             "
             "                                                                          "
                      , bg="black", height=0)
    sizelabel.pack()

    # 2.b Right frame
    bottomrightframe=Frame(bottomansframe,bg="blue")
    bottomrightframe.pack(side=RIGHT,expand=TRUE,anchor="nw")

    sizelabel = Label(bottomrightframe,
                      text="                                                                                                      "
 "                                                                          "
                      , bg="black", height=0)
    sizelabel.pack()

    # Questions packing in  the Question frames
    label = Label(questionframe,text=Questions[list1[0]][0], command=speak(Questions[list1[0]][0]),bg="blue", font="cascade 20 bold", fg="white")
    label.pack()


    # for   l1 packing inside the f1
    f1=Frame(topleftframe,)
    f1.pack(side=LEFT)

    # for l2 packing inside the f2
    f2=Frame(toprightframe,)
    f2.pack(side=LEFT,anchor="nw")

    # for l3 packing inside the f3
    f3=Frame(bottomleftframe,)
    f3.pack(side=LEFT)

    # for l4 packing inside the f4
    f4=Frame(bottomrightframe,)
    f4.pack(side=LEFT)


    userinteract = Frame(mainwindow2,bg="black" )
    userinteract.pack(side=BOTTOM, anchor="nw",pady=(0,2),fill=X)

    def select():
        global y,i,name_input,list1
        global var,ques,user_ans
        x = var.get()
        if ques == i:
            user_ans.append(x)
            print("this is user_ans",user_ans)
            i+=1
            if len(list1)==10:
                if len(user_ans)==10:
                    button4 = Button(userinteract, text=" R  E  S  U  L  T ", bg="black",
                        font=" cascase 20 bold ",fg="green",command=showresult)
                    button4.grid(row=0, column=2, pady=(0, 30), padx=(100, 50))

            if len(list1)==100:
                if len(user_ans)==100:
                    button4 = Button(userinteract, text=" R  E  S  U  L  T ", bg="black",
                            font=" cascase 20 bold ",fg="green",command=showresult)
                    button4.grid(row=0, column=2, pady=(0, 30), padx=(100, 50))

        # def speak(Str):
        #     speak = Dispatch(("SAPI.SpVoice"))
        #     speak.speak(Str)
        def next():
            global var, user_ans,name_input
            global label, l1, l2, l3, l4
            global ques,i,ques1,y
            global y,i,a,list1

            if ques < len(list1):
                print("This is checked",list1[ques])
                label.config(text=Questions[list1[ques]][0],command=speak(Questions[list1[ques]][0]))
                l1['text'] = answers[list1[ques]][0]
                l2['text'] = answers[list1[ques]][1]
                l3['text'] = answers[list1[ques]][2]
                l4['text'] = answers[list1[ques]][3]
                a=ques

                def previous():
                    global var, user_ans,i,ques
                    global label, l1, l2, l3, l4
                    global a,list1,y,i

                    label.config(text=Questions[list1[a]][0], command=speak(Questions[list1[a]][0]))
                    l1['text'] = answers[list1[a]][0]
                    l2['text'] = answers[list1[a]][1]
                    l3['text'] = answers[list1[a]][2]
                    l4['text'] = answers[list1[a]][3]
                    if a > 0:
                        a -= 1

                ques += 1
                button2 = Button(userinteract, text=" P  R  E  V  I  O  U  S",bg="black",
                        font="cascade 20 bold ", fg="blue",command=previous)
                button2.grid(row=0, column=0,pady=(0,30),padx=(130,50))

                def closewindow():
                    quit()
                button3 = Button(userinteract, text=" Q U I T ", bg="black",
                    font=" cascase 20 bold ", fg="red",command=closewindow)
                button3.grid(row=0, column=3, pady=(0, 30), padx=(100,170))

        button1 = Button(userinteract, text="N  E  X  T ", bg="black",
                font=" cascase 20 bold ", fg="yellow",command=next)
        button1.grid(row=0, column=1, pady=(0, 30), padx=(100, 50))


    var = IntVar()
    var.set(-1)
    l1_a=Label(f1,text=" A ",font="cascade 20 bold",fg="white",bg="black")
    l1_a.grid(row=0,column=0)

    l1 = Radiobutton(f1, text=answers[list1[0]][0],bg="blue",fg="white", font="cascade 20 bold", variable=var, value=0,
        command=select)
    l1.grid(row=0,column=1)

    l1_B = Label(f2, text=" B ",font="cascade 20 bold",bg="black",fg="white")
    l1_B.grid(row=0, column=0)

    l2 = Radiobutton(f2, text=answers[list1[0]][1],bg="blue",fg="white", font="cascade 20 bold", variable=var, value=1,
        command=select,)
    l2.grid(row=0,column=1,)

    l1_C = Label(f3, text=" C ",font="cascade 20 bold",fg="white",bg="black")
    l1_C.grid(row=0, column=0)

    l3 = Radiobutton(f3, text=answers[list1[0]][2], bg="blue",fg="white",font="cascade 20 bold", variable=var, value=2,
        command=select)
    l3.grid(row=0,column=1,)

    l1_D = Label(f4, text=" D ",font="cascade 20 bold",fg="white",bg="black")
    l1_D.grid(row=0, column=0)

    l4 = Radiobutton(f4, text=answers[list1[0]][3],bg="blue",fg="white", font="cascade 20 bold", variable=var, value=3,
        command=select)
    l4.grid(row=0,column=1,)


    mainwindow2.mainloop()

def name():
    global name_input
    speak("Before starting  the game we need to know some of its rules "
          "which will help you to play this game. This python quiz has "
          "hundres of questions and you will get four options from "
          "which you have to choose the correct answer. please write "
          "your name which must be more than two alphabets.")
    name_root = Tk()
    name_root.minsize(700,400)
    title_frame=Frame(name_root,bg="black")
    title_frame.pack(fill=BOTH)

    name_frame = Frame(name_root, bg="black")
    name_frame.pack(fill=BOTH)
    submit_frame = Frame(name_root,bg="black")
    submit_frame.pack(fill=BOTH,expand=TRUE)


    title = Label(title_frame,text = " W R I T E     Y O U R     N A M E ",
        fg="red",bg="black",font="cascade 30 bold",)
    title.pack(padx=30,pady=30)

    name_label =  Label(name_frame,text = " N A M E ",padx=60,
        font = "Arial 30 bold",fg="blue",bg="black")
    name_label.grid(row = 0,column = 0,pady=60,padx=250)

    name_var =  StringVar()

    name_entry =  Entry(name_frame,textvariable = name_var,width=40)
    name_entry.grid(row = 0 , column = 1,padx=80)

    def get1():
        global name_input
        name_root.destroy()
        name_input=name_var.get()

    sub_button = Button(submit_frame,text = " S T A R T ",
        font ="cascade 30 bold",command=get1,fg="green",bg="black")
    sub_button.pack(pady=40)

    name_root.mainloop()

if __name__ == '__main__':
        global name_input,userinteract
        name()
        speak("while playing you will be given the choice to choose only once for each question,"
              "after which you cannot make your selection. you can only see the previous question"
              " but can not make sine changes. please adapt questions continuously or else your "
              "score will be canceled. you will get 5 marks for each question. After attending "
              "all the questions please press the Result button. ")
        if len(name_input)>2:
            root=Tk()
            root.minsize(1550,850)
            root.title(" P Y T H O N      Q U I Z " ,)

            sideframe = Frame(root, borderwidth=2, bg="blue", relief=SUNKEN, )     # mainwindow  frame for create a LEVELS
            sideframe.pack(side=TOP,anchor="sw", fill=X)

            select_level1 = Label(sideframe, text="S   E   L   E   C   T            L   E   V   E   L"
                "                   - ",fg="yellow",bg="blue",font="cascade 20 bold ",)
            select_level1.grid(row=0, column=0,pady=(5,30))

            Button(sideframe, text=" S E L E C T   AL L   L E V E L ", font="ALGERIAN 18 bold",
                fg="white", bg="red",command=quegen, ).grid(row=0, column=3, padx=(40, 0))

            Button(sideframe, text=" L    E    V    E    L     -  1 ", font="ALGERIAN 20 bold",
                command=quegen_1,fg="white",bg="green",padx=150).grid(row=1,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  2 ", font="ALGERIAN 20 bold", fg="white",
                command=quegen_2,bg="green",padx=150).grid(row=2,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  3 ", font="ALGERIAN 20 bold", fg="white",
                command=quegen_3,bg="green",padx=150).grid(row=3,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  4 ", font="ALGERIAN 20 bold",
                command=quegen_4,fg="white",bg="green",padx=150).grid(row=4,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  5 ", font="ALGERIAN 20 bold",
                command=quegen_5,fg="white",bg="green",padx=150).grid(row=5,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  6 ", font="ALGERIAN 20 bold",
                command=quegen_6,fg="white",bg="green",padx=150).grid(row=6,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  7 ", font="ALGERIAN 20 bold",
                command=quegen_7,fg="white",bg="green",padx=150).grid(row=7,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  8 ", font="ALGERIAN 20 bold",
                command=quegen_8,fg="white",bg="green",padx=150).grid(row=8,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  9",  font="ALGERIAN 20 bold",
                command=quegen_9,fg="white",bg="green",padx=150).grid(row=9,column=0, pady=10,padx=(450,0))


            Button(sideframe, text=" L    E    V    E    L     -  10", font="ALGERIAN 18 bold",
                command=quegen_10,fg="white",bg="green",padx=160).grid(row=10,column=0,pady=10,padx=(450,0))

            root.mainloop()
            imagedisplay(list1)




