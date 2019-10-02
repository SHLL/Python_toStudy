from tkinter import *
import random
import string
from datetime import datetime

root = Tk()
root.title("Python打字练习")
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
e1 = Entry(root, text=v1,state='disabled',width=38, font=('宋体',14))
e2 = Entry(root, textvariable=v2, width=40, font=('宋体',14))
e3 = Label(root, textvariable=v3, width=40, font=('宋体', 10),foreground='red')
e1.grid(row=0, column=0,padx=12,pady=20)
e2.grid(row=1, column=0,padx=12,pady=20)
e3.grid(row=2, column=0,padx=12,pady=20)
text = Text(root, width=57, height=7)

text.grid(row=4, column=0, sticky=W, columnspan=2, padx=12, pady=20)

class TypingTest:
    def __init__(self):
        self.time_list = []
        self.letterNum = 20
        self.letterStr = ''.join(random.sample(string.printable.split(' ')[0], self.letterNum))
        self.examination_paper = ''
        self.create_exam()

    def time_calc(self):
        self.time_list.append(datetime.now())
        yield

    def create_exam(self):
        text.delete(0.0,END)
        v1.set(self.letterStr)
        self.time_calc().__next__()
        text.insert(END, "开始：%s \n" % str(self.time_list[-1]))

    def score(self):
        wrong_index = []
        self.time_calc().__next__()
        text.insert(END,"结束：%s \n" % str(self.time_list[-1]))
        use_time = (self.time_list[-1] - self.time_list[-2]).seconds
        self.examination_paper = v2.get()
        if len(self.examination_paper) > self.letterNum:
            v3.set("输入数据有误，作答数大于考题数")
        else:
            right_num = 0
            for z in range(len(self.examination_paper)):
                if self.examination_paper[z] == self.letterStr[z]:
                    right_num += 1
                else:
                    wrong_index.append(z)
            if right_num == self.letterNum:
                v3.set("完全正确，正确率%.2f%%用时: %s秒" % ((right_num * 1.0) / self.letterNum * 100, use_time))
            else:
                v3.set("正确率%.2f%%用时：%s 秒" % ((right_num * 1.0) / self.letterNum * 100, use_time))
                text.insert(END,"题目：%s\n" % self.letterStr)
                tag_info = list(map(lambda x: '4.' + str(x + 3), wrong_index))
                text.insert(END,"作答：%s\n" % self.examination_paper)
                for i in range(len(tag_info)):
                    text.tag_add("tag1", tag_info[i])
                    text.tag_config("tag1", background='red')
TypingTest = TypingTest()
btn_submit = Button(root, text="交卷",width=10, command=TypingTest.score, state='active')
btn_submit.grid(row=3, column=0, sticky=E ,padx=12, pady=5)
root.geometry("430x358")
mainloop()