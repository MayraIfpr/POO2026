import arcade
import random

ALTURA=600
LARGURA=800
TITULO="Meu jogo"

class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.10)

    def update(self, delta_time):
       self.center_x += self.change_x
       self.center_y += self.change_y
 
       if(self.right > LARGURA):
           self.change_x *= -1

       elif(self.left < 0):
            self.change_x *= -1
        
       if(self.top > ALTURA):
            self.change_y *= -1

       elif(self.bottom < 0):
            self.change_y *= -1 



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
            self.texture = self.textura_esquerda

       if(self.right > 800):
           self.change_x = 0

       elif(self.left < 0):
         self.change_x = 0
         self.left = 0
        
       if(self.top > ALTURA):
            self.change_y = 0
            self.top = ALTURA

       elif(self.bottom < 0):
            self.change_y = 0
            self.bottom = 0

        
           
        
       
           

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

         self.moeda.change_x = self.movimento
         self.moeda.change_y = self.movimento

         self.sprite_personagem = arcade.SpriteList()
         self.sprite_personagem.append(self.personagem)

         self.sprite_moedas = arcade.SpriteList()
         self.sprite_moedas.append(self.moeda)

         self.sprite_moedas = arcade.SpriteList()

         for i in range(25):  # quantidade de moedas
             moeda = Moeda()

             moeda.center_x = random.randint(50, LARGURA - 50)
             moeda.center_y = random.randint(50, ALTURA - 50)

             moeda.change_x = random.choice([-2, 2])
             moeda.change_y = random.choice([-2, 2])

             self.sprite_moedas.append(moeda)

    def on_draw(self):
        self.clear()
        self.sprite_personagem.draw()
        self.sprite_moedas.draw()



    def on_update(self, delta_time):
        self.sprite_personagem.update(delta_time)
        self.sprite_moedas.update(delta_time)
    
    #Gerenciamento do teclado
    def on_key_press(self, key, modifiers):
        def on_key_press(self, key, modifiers):
         if key == arcade.key.ESCAPE:
            self.close()
        if (key == arcade.key.RIGHT): 
            self.personagem.change_x += self.movimento
        if(key  == arcade.key.LEFT):
            self.personagem.change_x -= self.movimento
        if(key == arcade.key.UP):
            self.personagem.change_y += self.movimento
        if(key == arcade.key.DOWN):
            self.personagem.change_y -= self.movimento

        #Evento ao soltar a tecla
    def on_key_release(self, key, modifiers):
        if (key == arcade.key.RIGHT or key  == arcade.key.LEFT): 
                self.personagem.change_x = 0
        if(key == arcade.key.UP or key == arcade.key.DOWN):
                 self.personagem.change_y = 0


def main():
    jogo = JanelaJogo()
    arcade.run()


if __name__== "__main__":
    main()

