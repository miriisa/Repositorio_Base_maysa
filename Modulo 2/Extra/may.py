import pyautogui as aut
import flet as ft 

def man(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"        
 
    def automacao(e):
        email = texto_recebido.value
        # aut.mouseInfo()
        aut.sleep(1)
        aut.press("win")
        aut.sleep(2)
        aut.write("https://mail.google.com/mail/u/0/#inbox")
        aut.press("enter")
        aut.moveTo(145,182)
        aut.sleep(2)
        aut.doubleClick()
        aut.sleep(5)
        aut.write(email)
        aut.sleep(2)
        aut.press("tab")
        aut.press("tab")
        aut.sleep(3)
        aut.write("ooi fessor!")
        aut.moveTo(1299,992)
        aut.sleep(2)
        aut.doubleClick()
        # aut.moveTo(347,889)
        # aut.sleep(2)
        # aut.click()

    texto_recebido = ft.TextField (label="email")
    botoes = ft.ElevatedButton ("ENVIAR EMAIL",bgcolor= "blue", color= "white", width=200, on_click= automacao)
    page.add(ft.Row([texto_recebido],alignment= "center"),
             ft.Row ([botoes],alignment= "center"))
ft.app(target=man)
