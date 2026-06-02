import arcade

ALTURA=600
LARGURA=800
TITULO="Meu jogo"

class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.10)

    def update(self, delta_time):
       self.center_x += self.change_x
       self.center_y += self.change_y
 
       if self.center_x > 800:
           self.change_x 

       elif self.center_x < 0:
            self.change_x = 0

       if self.center_y > 600:
            self.change_y = 0 

       elif self.center_y < 0:
            self.change_y = 0    



#personagem
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("direita.png", scale=0.5)

        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")
    
    #atualizar personagem
    def update(self, delta_time):
       self.center_x += self.change_x
       self.center_y += self.change_y

       if self.change_x > 0:
           self.texture = self.textura_direita

       elif self.change_x <0:
            self.exture = self.textura_esquerda
        
       
           

class JanelaJogo(arcade.Window):
    def __init__(self):
         super().__init__(LARGURA, ALTURA, TITULO)
         arcade.set_background_color(  arcade.color.AMAZON  )

         self.movimento = 2

         self.personagem = Player()
         self.moeda = Moeda()

         self.personagem.center_x = 400
         self.personagem.center_y = 300

         self.moeda.center_x = 500
         self.moeda.center_y = 300

         self.moeda.center_x += self.movimento
         self.moeda.center_y += self.movimento


         
         self.sprite_personagem = arcade.SpriteList()
         self.sprite_personagem.append(self.personagem)

         self.sprite_moedas = arcade.SpriteList()
         self.sprite_moedas.append(self.moeda)

    def on_draw(self):
        self.clear()
        self.sprite_personagem.draw()
        self.sprite_moedas.draw()



    def on_update(self, delta_time):
        self.sprite_personagem.update(delta_time)
        self.sprite_moedas.update(delta_time)
    
def main():
    jogo = JanelaJogo()
    arcade.run()


if __name__== "__main__":
    main()

