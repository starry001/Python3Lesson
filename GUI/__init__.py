from tkinter import *
from tkinter import messagebox

'''
第一步是导入Tkinter包的所有内容
第二步是从Frame派生一个Application类，这是所有Widget的父容器
在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，
所有的Widget组合起来就是一棵树。
pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出
'''
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.helloLabel = Label(self, text='hello')#文字
        self.helloLabel.pack()
        self.nameInput = Entry(self)#输入框
        self.nameInput.pack()
        self.quitButton = Button(self, text='quit', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello %s' %name)

'''
第三步，实例化Application，并启动消息循环：
'''
app = Application()
app.master.title = 'hello app'
app.mainloop()
