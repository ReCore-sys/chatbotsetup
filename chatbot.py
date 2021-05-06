from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import sys
import threading
import time
start = time.time()

bot = ChatBot('Gideon')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    'chatterbot.corpus.english'
)
end = time.time()

print(f"Training: {end - start}")
start = time.time()

main = Tk()

main.geometry("500x650")

main.title("Gideon")

img = PhotoImage(file="bot.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)
end = time.time()

print(f"Frame render: {end - start}")


def ask_from_bot():
    start = time.time()
    query = textF.get()
    msgs.insert(END, "You : " + query)

    textF.delete(0, END)
    msgs.yview(END)

    answer_from_bot = bot.get_response(query)

    print(answer_from_bot)
    msgs.insert(END, "Gideon : " + str(answer_from_bot))
    end = time.time()

    print(f"Anwser: {end - start}")


def takeQuery():
    query = textF.get()
    print(query)
    textF.delete(0, END)
    textF.insert(0, query)
    ask_from_bot()


frame = Frame(main)

# main.attributes('-fullscreen', True)

sc = Scrollbar(frame)

width = frame.winfo_width()

msgs = Listbox(frame, width=400, height=35, yscrollcommand=sc.set)

print(width)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(fill=X, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Courier", 10))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask Gideon", font=(
    "Courier", 10), bg='red', command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    ask_from_bot()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)

"""
def repeatL():
    takeQuery()


t = threading.Thread(target=repeatL)

t.start()"""

main.mainloop()
