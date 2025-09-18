import os
import flet as ft
pasta = ""

def main(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"
    
    # Função para criar pastas
    def criar_pasta(e):
        global pasta
        pasta = texto_recebido.value
        try:
            os.mkdir(pasta)
            informativo.value = f"Pasta criada: '{pasta}'"
        except FileExistsError:
            informativo.value = f"A pasta '{pasta}' foi criada."
        page.update()
   
    def renomear(e):   
        texto_novo = texto_recebido.value
        os.rename(f"{texto}", "{texto_novo}")
        
        
         # Função para criar arquivos
    def criar_arquivo(e):
        global texto
        if pasta == "":
            texto = texto_recebido.value
            open(texto, "w").close()
            informativo.value = f"Arquivo criado: '{texto}.txt'"
        else:
            texto = texto_recebido.value
            open(f"(pasta)/(texto)", "w").close()
            page.update()

    # Campos e botões
    texto_recebido = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="WHITE", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="CYAN", color="BLACK", width=200, on_click=criar_arquivo)
    botao_renomear = ft.ElevatedButton("RENOMEAR ARQUIVO", bgcolor="WHITE", color="BLACK", width=200, on_click=texto_novo)
    informativo = ft.Text("", size=20, color="white")

    # Layout
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo], alignment="center"),
        ft.Row([ botao_renomear], alignment="center"),
        ft.Row([informativo], alignment="center"))
    

ft.app(target=main)

