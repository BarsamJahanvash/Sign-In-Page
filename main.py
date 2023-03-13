from flet import *



Color1 = "#191414"
Color2 = "#1DB954"

def main(page : Page):
    # Page Controls
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = "Login Page"
    page.window_width,page.window_height = 1000,800
    page.fonts = {
        "Font1":"/fonts/TiltNeon.ttf",
        "Font2":"/fonts/Quicksand.ttf",
        "Font2Bold":"/fonts/Quicksand-Bold.ttf"
    }
    page.bgcolor = Color1 
    # "#292A2A"
    MainCont = Container(
        width=495,
        height=500,
        border_radius=5,
        alignment=alignment.center,
        bgcolor=Color1,
        content=(
            Column(
                controls=[
                    Divider(height=45,color="transparent"),
                    Text("Sign In",size=40,weight="bold",font_family="Font2"),
                    Divider(height=30,color="transparent"),
                    Container(width=300,height=40,border=border.only(bottom = border.BorderSide(0.9,"white")),content=(
                        Row(
                            controls=[
                                Icon(name=icons.PERSON_ROUNDED,color=Color2),
                                TextField(width=300,height=50,hint_text="Email",hint_style=TextStyle(font_family="Font2",size=20),text_style=TextStyle(font_family="Font2",size=18),content_padding=5,border_color="transparent")
                            ]
                        )
                        )),
                    Divider(height=20,color="transparent"),
                    Container(width=300,height=40,border=border.only(bottom = border.BorderSide(0.9,"white")),content=(
                        Row(
                            controls=[
                                Icon(name=icons.LOCK,color=Color2),
                                TextField(width=300,height=50,hint_text="Password",password=True,hint_style=TextStyle(font_family="Font2",size=20),text_style=TextStyle(font_family="Font2",size=18),content_padding=5,border_color="transparent")
                            ]
                        )
                        )),
                    Row(width=300,alignment=MainAxisAlignment.END,controls=[TextButton(content=(Text("Forgot Password?",font_family="Font2",weight="bold")),style=ButtonStyle(color="white",shape={"":RoundedRectangleBorder(radius=0)}))]),
                    Divider(height=40,color="transparent"),
                    TextButton(content=(Text("Sign In",font_family="Font2",weight="bold")),width=300,style=ButtonStyle(bgcolor=Color2,color="white",shape={"":RoundedRectangleBorder(radius=20)},)),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )
    )
    # 
    # (
    #             TextField(width=300,height=50,hint_text="Email",hint_style=TextStyle(font_family="Font2",size=20),text_style=TextStyle(font_family="Font2",size=18),content_padding=5,border_color="transparent",icon=icons.PERSON_ROUNDED))        
    #                 )
    
    page.add(MainCont)
    page.update()


app(target=main,assets_dir="assest",view=WEB_BROWSER,port=8080)


