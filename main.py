   
import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption(" Register CAT")
icone = pg.image.load("assets/mucego.ico")
pg.display.set_icon(icone)
COLOR_INACTIVE = pg.Color(162,93,155)
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 25)

start = "start"

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.Rect(100, 310, 400, 60).collidepoint(event.pos):
                self.active = not self.active
                import game
            else:
                self.active = False
            if self.rect.collidepoint(event.pos):
                self.text = ''
                self.active = not self.active
            else:
                self.active = False

            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                arq = open('lista.Vencedores', 'r')
                ler = arq.read()
                if event.key == pg.K_RETURN : 
                    arquivo = open('lista.Vencedores', 'w')
                    arquivo.write(ler + ' -- > ' + self.text)
                    print(self.text)

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(400, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

    def draw2(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def main():
    AMD = pg.image.load("assets/START.png")
    configTela = (600, 400)
    gameDisplay    = pg.display.set_mode(configTela)
    fonte = pg.font.SysFont(None, 30)
    texto = fonte.render("Insira seu Nome:", True, (255,255,0))
    texto2 = fonte.render("E-mail:", True, (255,255,0))
    texto3 = fonte.render("Pressione Enter a cada campo inserido para confirmação!", True, (255,255,0))
    gameDisplay.blit(texto, (100, 200))
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 90, 140, 40)
    input_box2 = InputBox(100, 210, 140, 40)
    input_box3 = InputBox(100, 310, 140, 60)
    input_boxes = [input_box1, input_box2]
    inputies = [input_box3]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            for inp3 in inputies:
                inp3.handle_event(event)

        for box in input_boxes:
            box.update()
        for inp3 in inputies:
            inp3.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            gameDisplay.blit(texto3, (17, 10))
            gameDisplay.blit(texto, (220, 70))
            gameDisplay.blit(texto2, (260, 190))
            gameDisplay.blit(AMD, (155, 320))
            box.draw(screen)
        for inp3 in inputies:
            inp3.draw2(screen)

        pg.display.flip()
        clock.tick(30)

if start == "start":
    main()
    pg.quit()


    
    