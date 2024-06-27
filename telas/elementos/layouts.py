from flet import *


def main(page:Page):
    page.title="Estudando Cards"
    produto=Card(
        content=Container(
            content=Column(
                controls=[
                    Image(src="lanche.jpg"),
                    Text("Lanche Vegano"),
                    Text("Lanche feito de proteina Vegetal"),
                    Row(controls=[
                        Icon(cupertino_icons.HEART),
                        Icon(icons.PAYMENT)
                    ])

                ]
            )
        )
    )

    page.add(produto)


if __name__ == '__main__':
    app(target=main)