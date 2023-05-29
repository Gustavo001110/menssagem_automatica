from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib


def enviar():
    telefone = entry0.get()
    msg = entry1.get('1.0', END)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://web.whatsapp.com/')
    sleep(30)
    texto = urllib.parse.quote(msg)
    navegador.get(f'https://web.whatsapp.com/send?phone={telefone}&text={texto}')
    sleep(30)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    sleep(30)


window = Tk()
window.title('Menssagem automatica')

window.geometry("659x468")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=468,
    width=659,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"imagens/background.png")
background = canvas.create_image(
    375.0, 234.0,
    image=background_img)

entry0_img = PhotoImage(file=f"imagens/img_textBox0.png")
entry0_bg = canvas.create_image(
    536.5, 195.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry0.place(
    x=441, y=175,
    width=191,
    height=38)

entry1_img = PhotoImage(file=f"imagens/img_textBox1.png")
entry1_bg = canvas.create_image(
    537.0, 325.0,
    image=entry1_img)

entry1 = Text(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry1.place(
    x=430, y=249,
    width=214,
    height=150)

img0 = PhotoImage(file=f"imagens/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=enviar,
    relief="flat")

b0.place(
    x=493, y=426,
    width=103,
    height=33)

window.resizable(False, False)
window.mainloop()
