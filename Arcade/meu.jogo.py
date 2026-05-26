import arcade

ALTURA=600
LARGURA=800
TITULO="Meu jogo"

#personagem
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("direita.png", scale=0.5)

        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")
    
    #atualizar personagem
    def update(self, delta_time):
       pass

class JanelaJogo(arcade.Window):
    def __init__(self):
         super().__init__(LARGURA, ALTURA, TITULO)
         arcade.set_background_color(  arcade.color.AMAZON  )

         self.personagem = Player()

         self.personagem.center_x = 400
         self.personagem.center_y = 300

    def on_draw(self):
        self.clear()

        arcade.draw_sprite(self.personagem)

    def on_update(self, delta_time):
        pass
    
def main():
    jogo = JanelaJogo()
    arcade.run()


if __name__== "__main__":
    main()

