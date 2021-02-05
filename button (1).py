import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

class Button(pygame.sprite.Sprite):
    """Label Class (simplest version
        Atttributes :
            font: any pygame Font or SysFont object
            text:  text to display
            center:  desired positon of label center (x,y)
    """
    def __init__(self, text = "", posx = 320, posy = 240, color = (255,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill((color))
        self.font = pygame.font.SysFont("None", 30)
        self.text = text
        self.center = (posx,posy)
        self.background = (0,255,255)
        self.mouse = pygame.mouse.get_pos()

    def update(self):
        '''create an image based on the font and text'''
        self.image = self.font.render(self.text, 1, (0,0,0), self.background)
        self.rect = self.image.get_rect()       #set the rectangle to be the size of the image.
        self.rect.center = self.center          #position the button
        self.mouse = pygame.mouse.get_pos()
        self.check_hover()            #check if mouse is hovering
        self.color()                            #change color of background of label


    def check_hover(self):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.rect.collidepoint(self.mouse):
         self.is_hover = True
      else:
         self.is_hover = False

    def color(self):
      '''change color when hovering'''
      if self.is_hover  == True:
         self.background = (255,0,0)
      else:
         self.background = (0,255,255)

    def click(self):
        '''return true or false based on mouse over the button '''
        if self.rect.collidepoint(self.mouse):
            return True
        else:
            return False

def main():

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("sprite - to - sprite collision")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 0))
    screen.blit(background, (0,0))

    btn1 = Button('Button 1', 100, 100)
    btn2 = Button('Button 2', 400, 400)
    btn3 = Button('Button 3')

    allSprites = pygame.sprite.Group(btn1, btn2, btn3)

    clock = pygame.time.Clock()
    keepGoing = True
    pygame.mouse.set_visible(False)

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn1.click() == True:
                   print('button 1 clicked')
                elif btn2.click():
                   print('button 2 clicked')
                elif btn3.click():
                   print('button 3 clicked')

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
        pygame.mouse.set_visible(True)

if __name__ == "__main__":
    main()
