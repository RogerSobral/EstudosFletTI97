import flet as ft


#vou usar essa função para criar o layout da pagina
def main(page:ft.Page):
    page.title="Primeira pagina"

    #Toda vez que eu alterar a minha pagina eu devo dar um update
    page.update()



ft.app(target=main)

