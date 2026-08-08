# ###############################################
# Visualiza pontos e retangulos usando PyGlet   #
# ###############################################

import sys
import random
from datetime       import datetime

import objetosGeometricos as cObjetos       # importa o modulo com os objetos geometricos

import pyglet
from pyglet         import shapes
from pyglet.window  import Window
from pyglet.window  import key
from pyglet.window  import mouse

# dimensoes da janela

WIN_X       = 800       
WIN_Y       = 800

# para guardar o ponto inicial do retangulo quando for clicado com o botao direito
pto_atual   = None

# *******************************************************
# ***                                                 ***
# *******************************************************
def gameLoop():

    global window, batch

    window = pyglet.window.Window(WIN_X, WIN_Y)
    window.set_caption('Visualiza Pontos e Retangulos')

    batch   = pyglet.graphics.Batch()
    formas = []

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):

        global pto_atual

        if button == mouse.LEFT:    # se for o botao esquerdo cria um ponto

            corPto = cObjetos.cCor( random.randint(0, 255), 
                                    random.randint(0, 255), 
                                    random.randint(0, 255)  )
            
            formas.append(shapes.Circle(    x, y, 3, 
                                            color=(corPto.getR(), corPto.getG(), corPto.getB()), 
                                            batch=batch)) 
            
        elif button == pyglet.window.mouse.RIGHT:  # se for o botao esquerdo cria um ponto

            if pto_atual == None:       # se nao tem ponto inicial registra o primeiro ponto do retangulo sem "desenhar"
                corPto = cObjetos.cCor( random.randint(0, 255), 
                                        random.randint(0, 255), 
                                        random.randint(0, 255)  )
                pto_atual = cObjetos.cPonto( x, y, corPto)
            else:                       # se for o segundo ponto do calcula as dimensões do retangulo e "desenha"
                corPto = cObjetos.cCor( random.randint(0, 255), 
                                        random.randint(0, 255), 
                                        random.randint(0, 255)  )
                xmin = min(pto_atual.getX(), x)
                ymin = min(pto_atual.getY(), y)
                xmax = max(pto_atual.getX(), x)
                ymax = max(pto_atual.getY(), y)
                w = xmax - xmin
                h = ymax - ymin
                formas.append(shapes.Rectangle( xmin, ymin, w, h,
                                                color=(corPto.getR(), corPto.getG(), corPto.getB()), 
                                                batch=batch)) 
                
                pto_atual = None        # reseta o ponto inicial

    pyglet.app.run()


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    gameLoop()
