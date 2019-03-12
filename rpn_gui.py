#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import operator
import readline
from Tkinter import *

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

class App:
    result = ""
    flag = False
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.add_button = Button(
            frame, text = "+", fg = "red", command = self.add_func
            )
        self.add_button.pack(side=LEFT)

        self.minus_button = Button(
            frame, text = "-", fg = "red", command = self.minus_func
            )
        self.minus_button.pack(side=LEFT)

        self.multiply_button = Button(
            frame, text = "x", fg = "red", command = self.multiply_func
            )
        self.multiply_button.pack(side=LEFT)

        self.divide_button = Button(
            frame, text = u"÷", fg = "red", command = self.divide_func
            )
        self.divide_button.pack(side=LEFT)

        self.power_button = Button(
            frame, text = "^", fg = "red", command = self.power_func
            )
        self.power_button.pack(side=LEFT)

        self.equal_button = Button(
            frame, text = "=", fg = "red", command = self.equal_func
            )
        self.equal_button.pack(side=LEFT)

        self.one_button = Button(
            frame, text = "1", command = self.one
            )
        self.one_button.pack(side=LEFT)

        self.two_button = Button(
            frame, text = "2", command = self.two
            )
        self.two_button.pack(side=LEFT)

        self.three_button = Button(
            frame, text = "3", command = self.three
            )
        self.three_button.pack(side=LEFT)

        self.four_button = Button(
            frame, text = "4", command = self.four
            )
        self.four_button.pack(side=LEFT)

        self.five_button = Button(
            frame, text = "5", command = self.five
            )
        self.five_button.pack(side=LEFT)

        self.six_button = Button(
            frame, text = "6", command = self.six
            )
        self.six_button.pack(side=LEFT)

        self.seven_button = Button(
            frame, text = "7", command = self.seven
            )
        self.seven_button.pack(side=LEFT)

        self.eight_button = Button(
            frame, text = "8", command = self.eight
            )
        self.eight_button.pack(side=LEFT)

        self.nine_button = Button(
            frame, text = "9", command = self.nine
            )
        self.nine_button.pack(side=LEFT)

        self.zero_button = Button(
            frame, text = "0", command = self.zero
            )
        self.zero_button.pack(side=LEFT)

        self.display_field = Label(
            master, text = self.result
            )
        self.display_field.pack()

        self.answer_field = Label(
            master, text = ""
        )
        self.answer_field.pack()

    def add_func(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "+"
        self.display()

    def minus_func(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "-"
        self.display()

    def multiply_func(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "*"
        self.display()

    def divide_func(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "/"
        self.display()

    def power_func(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "^"
        self.display()

    def one(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "1"
        self.display()

    def two(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "2"
        self.display()

    def three(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "3"
        self.display()

    def four(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "4"
        self.display()

    def five(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "5"
        self.display()

    def six(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "6"
        self.display()

    def seven(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "7"
        self.display()

    def eight(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "8"
        self.display()

    def nine(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "9"
        self.display()

    def zero(self):
        if self.flag == True:
            self.result += " "
        else:
            self.answer_field["text"] = ""
            self.flag = True
        self.result += "0"
        self.display()

    def equal_func(self):
        stack = list()
        for token in self.result.split():
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
            print(stack)
        if len(stack) != 1:
            raise TypeError("Too many parameters")
        self.answer_field["text"] = "ANS: " + str(stack.pop())
        self.flag = False
        self.result = ""

    def display(self):
        self.display_field["text"] = self.result

def main():
    while True:
        root = Tk()
        root.title("RPN Calculator")
        app = App(root)
        root.mainloop()

if __name__ == '__main__':
    main()
