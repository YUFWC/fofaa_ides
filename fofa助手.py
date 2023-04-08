import re
import requests
import base64
from concurrent.futures import ThreadPoolExecutor
import threading
import os, sys
import win32api, win32gui
try:
    from tkinter import *
except ImportError:
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    from tkMessageBox import *
else:
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *

ct = win32api.GetConsoleTitle()
hd = win32gui.FindWindow(0, ct)
win32gui.ShowWindow(hd, 0)

class Application_ui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('FOFA助手')
        self.master.geometry('640x426')
        # self.master.iconbitmap('C:\\Users\lenovo\Desktop\ico\二要素\kfc.ico')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text1Var = StringVar(value='请输入语法命令(例：domain="qq.com" )')
        self.Text1 = Entry(self.top, text='请输入语法命令(例：domain="qq.com" )', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0., rely=0., relwidth=0.602, relheight=0.077)

        self.style.configure('Command1.TButton',font=('宋体', 9))
        self.Command1 = Button(self.top, text='点击查询', command=lambda: self.thread_it(self.ext), style='Command1.TButton')
        self.Command1.place(relx=0.75, rely=0., relwidth=0.202, relheight=0.077)

        self.Text2Var = StringVar(value='key')
        self.Text2 = Entry(self.top, text='key', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0., rely=0.113, relwidth=0.602, relheight=0.077)

        self.Text3Var = StringVar(value='起始页')
        self.Text3 = Entry(self.top, text='起始页', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.625, rely=0., relwidth=0.102, relheight=0.077)

        self.style.configure('Command2.TButton',font=('宋体',9))
        self.Command2 = Button(self.top, text='导出文件', command=self.write, style='Command2.TButton')
        self.Command2.place(relx=0.75, rely=0.113, relwidth=0.202, relheight=0.077)

        self.ListVar = StringVar(value=f'版权：@crazy')
        self.ListFont = Font(font=('宋体', 9))
        self.List = Listbox(self.top, listvariable=self.ListVar, font=self.ListFont)
        self.List.place(relx=0., rely=0.244, relwidth=1.002, relheight=0.742)

        self.Text4Var = StringVar(value='结束页')
        self.Text4 = Entry(self.top, text='结束页', textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.place(relx=0.625, rely=0.113, relwidth=0.102, relheight=0.077)

class Application(Application_ui):

    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def thread_it(self, func, *args):
        self.myThread = threading.Thread(target=func, args=args)
        self.myThread.setDaemon(True)
        self.myThread.start()

    def exit(self):
        b = self.Text1Var.get()
        base = base64.encodebytes(b.encode('utf-8'))
        # print(base)
        base_1 = str(base)
        # print(base_1)
        obj = re.compile(r"b'(?P<bas>.*?)\\n'", re.S)
        for i in obj.finditer(base_1):
            ii = (i.group('bas'))
            url = f"https://fofa.info/result?qbase64={ii}"
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            }
            resp = requests.get(url, headers=header)
            # print(resp.text)
            obj = re.compile(r'<p class="hsxa-nav-font-size"><span class="hsxa-highlight-color">(?P<number>.*?)</span>',
                             re.S)
            for it in obj.finditer(resp.text):
                print(it.group('number') + "条匹配结果")
                iii = it.group('number') + "条匹配结果"
                self.List.insert('1', iii)

    def ext(self):
        b = self.Text1Var.get()
        base = base64.encodebytes(b.encode('utf-8'))
        base_1 = str(base)
        de = self.Text3Var.get()
        df = self.Text4Var.get()
        obj = re.compile(r"b'(?P<bas>.*?)\\n'", re.S)
        for iis in obj.finditer(base_1):
            ifs = iis.group('bas')

        def fn(url):
            header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
                    "Cookie": f"{self.Text2Var.get()}"
            }
            resp = requests.get(url, headers=header)
            obj_1 = re.compile(r'<span class="hsxa-host"><a href="(?P<web>.*?)" target="_blank">', re.S)
            for it in obj_1.finditer(resp.text):
                print(it.group('web'))
                ibs = it.group('web')
                self.List.insert('1', ibs)
        with ThreadPoolExecutor(2) as f:
            for iss in range(int(de), int(df)):
                f.submit(fn, f"https://fofa.info/result?qbase64={ifs}&page={iss}&page_size=20")
        self.List.insert("1", "查询完毕")

    def write(self):
        with open('web.txt', 'a') as file:
            for ib in range(1, int(self.Text3.get())*20):
                print(self.List.get(first=ib), file=file)

if __name__ == "__main__":
    top = Tk()
    # top.attributes("-topmost", 1)
    Application(top).mainloop()
    try: top.destroy()
    except: pass
