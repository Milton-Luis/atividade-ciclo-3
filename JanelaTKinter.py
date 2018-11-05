# coding: utf-8

from tkinter import *

from CalcIMC import Calc


class JanelaTK:
    def __init__(self, janela):

        self.fonte = ("Times New Roman", "12")

        self.janela = janela
        self.janela.geometry("700x400+300+100")
        self.janela.title("Cálculo de IMC - Indice de massa corporal")

        self.lbNome = Label(janela, text="Nome do Paciente:")
        self.lbNome["font"] = self.fonte
        self.lbNome.place(x=10, y=10)

        self.nome = Entry(janela, width=60)
        self.nome["font"] = self.fonte
        self.nome.place(x=150, y=10)

        self.lbEnd = Label(janela, text="Endereço Completo: ")
        self.lbEnd["font"] = self.fonte
        self.lbEnd.place(x=10, y=70)

        self.end = Entry(janela, width=60)
        self.end["font"] = self.fonte
        self.end.place(x=150, y=70)

        self.lbAltura = Label(janela, text="Altura (M)")
        self.lbAltura["font"] = self.fonte
        self.lbAltura.place(x=10, y=130)

        self.altura = Entry(janela, width=20)
        self.altura["font"] = self.fonte
        self.altura.place(x=150, y=130)

        self.lbPeso = Label(janela, text="Peso (Kg)")
        self.lbPeso["font"] = self.fonte
        self.lbPeso.place(x=10, y=190)

        self.peso = Entry(janela, width=20)
        self.peso["font"] = self.fonte
        self.peso.place(x=150, y=190)

        self.txt = Text(janela, width=40, height=10)
        self.txt.place(x=330, y=130)

        self.btC = Button(janela, text="Calcular")
        self.btC["font"] = self.fonte
        self.btC["command"] = self.btCalcular
        self.btC["width"] = 15
        self.btC.place(x=150, y=325)

        self.btR = Button(janela, text="Reiniciar")
        self.btR["command"] = self.btReiniciar
        self.btR["font"] = self.fonte
        self.btR["width"] = 15
        self.btR.place(x=300, y=325)

        self.btS = Button(janela, text="Sair")
        self.btS["font"] = self.fonte
        self.btS["command"] = quit
        self.btS["width"] = 15
        self.btS.place(x=500, y=325)

    def btCalcular(self):

        nome = self.nome.get()
        endereco = self.end.get()
        altura = float(self.altura.get())
        peso = float(self.peso.get())

        j = Calc(altura, peso)
        imc = j.result

        # imc = float(peso/(altura * altura))

        self.txt.insert(INSERT, "Nome: {}\n".format(nome))
        self.txt.insert(INSERT, "Endereço: {}\n".format(endereco))
        self.txt.insert(INSERT, "Altura: {} m    Peso: {} Kg\n".format(altura, peso))
        self.txt.insert(INSERT, "Seu IMC é: %.2f\n" % imc)

        if imc < 16:
            self.txt.insert(INSERT, "Situação: Magreza grave")

        elif imc >= 16 < 17:
            self.txt.insert(INSERT, "Situação: Magreza Moderada")

        elif imc >= 17 < 18.5:
            self.txt.insert(INSERT, "Situação: Magreza Leve")

        elif imc >= 18.25 < 25:
            self.txt.insert(INSERT, "Situação: Saudável")

        elif imc > 25 < 30:
            self.txt.insert(INSERT, "Situação: Sobrepeso")

        elif imc >= 30 < 35:
            self.txt.insert(INSERT, "Situação: Obesidade - Grau I")

        elif imc >= 35 < 40:
            self.txt.insert(INSERT, "Situação: Obesidade - Grau II (Severa)")

        else:
            self.txt.insert(INSERT, "Situação: Obesidade - Grau III ( Morbida)")

    def btReiniciar(self):
        self.nome.delete(0, END)
        self.end.delete(0, END)
        self.altura.delete(0, END)
        self.peso.delete(0, END)
        self.txt.delete(1.0, END)
        return self.txt, self.nome, self.end, self.altura, self.peso


tk = Tk()
JanelaTK(tk)
tk.mainloop()
