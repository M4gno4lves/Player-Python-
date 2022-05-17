from cgitb import text
from email.mime import image
from multiprocessing import managers
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import os
import pygame
class Player:
    def __init__(self):
        pygame.mixer.init()

        self.w = ThemedTk(theme='equilux')
        self.w.title("Músicas")
        self.w.geometry('300x400')
        self.w.resizable(0,0)
        self.w.config(bg='#333333')
        self.img_add = PhotoImage(file='img/add.png')
        self.img_next = PhotoImage(file='img/next.png')
        self.img_pause = PhotoImage(file='img/pause.png')
        self.img_play = PhotoImage(file='img/play.png')
        self.img_previus = PhotoImage(file='img/previus.png')
        self.img_remove = PhotoImage(file='img/remove.png')
        self.local=''
        self.status = 0
        self.list = Listbox(self.w, bg='#444444',height=10, bd=0, fg='white', font='arial 12 bold', selectbackground='#6868e6')
        self.list.pack(fill='x', pady=10,padx=10)

        self.frame = ttk.Frame(self.w)
        self.frame.pack(pady=10)

        self.remover = ttk.Button(self.frame,image=self.img_remove, command=self.DeletarMusica)
        self.remover.grid(row=0,column=0)
        self.add = ttk.Button(self.frame, image=self.img_add, command=self.SelecionarMusica)
        self.add.grid(row=0,column=1)

        self.frame2 = ttk.Frame(self.w)
        self.frame2.pack(pady=10)

        self.anterior = ttk.Button(self.frame2,image=self.img_previus, command=self.MusicaAnterior)
        self.anterior.grid(row=0,column=0)
        self.iniciar = ttk.Button(self.frame2,image=self.img_play, command=self.PlayMusica)
        self.iniciar.grid(row=0,column=1)
        self.proximo = ttk.Button(self.frame2,image=self.img_next,command=self.ProximaMusica)
        self.proximo.grid(row=0,column=3)

        self.vol = ttk.Scale(self.w,from_= 0, to = 1, command=self.Volume)
        self.vol.pack(fill='x', padx=10)


        self.w.mainloop()
    def SelecionarMusica(self):
        self.local = filedialog.askdirectory()   
        files = os.listdir(self.local)

        for arquivo in files:
            self.list.insert(END, str (arquivo))
    def DeletarMusica(self):
        self.list.delete(ANCHOR)

    def ProximaMusica(self):
        try:
            index = self.list.curselection()[0] + 1 
            self.list.select_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
                self.Error('Não há músicas para passar')

    def MusicaAnterior(self):
        try:
            index = self.list.curselection()[0] - 1
            self.list.select_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
            self.Error('Não há músicas para passar')


    def PlayMusica(self):
        try:
            if self.status == 0:
                pygame.mixer.music.load(str(self.local) + '/' + str(self.list.get(ANCHOR)))
                pygame.mixer.music.play()
                self.iniciar.config(image=self.img_pause)
                self.status=1
            else:
                pygame.mixer.music.pause()
                self.iniciar.config(image=self.img_play)
                self.status=0
        except:    
            self.Error('Não tem músicas para tocar')
  
    def Error(self, menssage):
        win=Toplevel()
        win.title("ERROR")
        win.geometry('300x300+300+300')
        win.resizable(0,0)
        win.config(bg='#444444')

        text = ttk.Label(win, text=str(menssage), font='arial 12')
        text.pack(expand=YES)
        btn = ttk.Button(win,text='OK', command=win.destroy)
        btn.pack()

    def Volume(self, var):
        pygame.mixer.music.set_volume(self.vol.get())
Player()        