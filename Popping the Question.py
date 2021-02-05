"""
Popping the Question: Trivia Game
Popping the Question.py
Lexi Iocca
Date: January 17, 2018
"""
# Import and Initialize

import pygame
import random

pygame.init()

pygame.init()  # allows sound to be added to the game
pygame.mixer.init()

pop = pygame.mixer.Sound("pop.ogg")  # these are the lines that attach the sound to a variable
strike = pygame.mixer.Sound("strike.ogg")
lose = pygame.mixer.Sound("lose.ogg")
yay = pygame.mixer.Sound("yay.ogg")
correct = pygame.mixer.Sound("correct.ogg")
backtrack = pygame.mixer.Sound("backtrack.ogg")

screen = pygame.display.set_mode((1000, 800))  # sets the size of the screen
score = 0  # set the score to 0

class Pin(pygame.sprite.Sprite):  # making the sprite - assigning an image to it
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pin.fw.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cloud.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(15, 980))
        self.dx = 0  # sets how the cloud moves
        self.dy = -1

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom > screen.get_width():
            self.rect.top = 0

class Balloon1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon1.50.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(0, 800))
        self.dx = 0
        self.dy = +3.5

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom < 0:  # sets the boundaries - if the balloon goes off the top of the screen it will show
            # up at the bottom again
            self.rect.top = 800

class Balloon2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon2.100.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(0, 800))
        self.dx = 0
        self.dy = +2.5

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom < 0:
            self.rect.top = 800

class Balloon3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon3.75.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(0, 800))
        self.dx = 0
        self.dy = +3.5

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom < 0:
            self.rect.top = 800

class Balloon4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon4.125.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(0, 800))
        self.dx = 0
        self.dy = +3

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom < 0:
            self.rect.top = 800

class Balloon5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon5.150.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(0, 800))
        self.dx = 0
        self.dy = +3

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom < 0:
            self.rect.top = 800

class Plainballoon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("plainballoon.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(0, 800))
        self.dx = 0
        self.dy = +3

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom < 0:
            self.rect.top = 800

class finBalloon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("finballoon.fw.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = (random.randrange(15, 980))
        self.rect.centery = (random.randrange(0, 800))
        self.dx = 0
        self.dy = +3

    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx
        if self.rect.bottom < 0:
            self.rect.top = 800

class Strike1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("X.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = 980
        self.rect.centery = 780

class Strike2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("X.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = 935
        self.rect.centery = 780

class Strike3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("X.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = 890
        self.rect.centery = 780

class Button(pygame.sprite.Sprite):
    """Label Class (simplest version
        Atttributes :
            font: any pygame Font or SysFont object
            text:  text to display
            center:  desired positon of label center (x,y)
    """

    def __init__(self, text="", posx=320, posy=240, color=(255, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((color))
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.text = text
        self.center = (posx, posy)
        self.background = (255, 245, 175)
        self.mouse = pygame.mouse.get_pos()

    def update(self):
        '''create an image based on the font and text'''
        self.image = self.font.render(self.text, 1, (0, 0, 0), self.background)
        self.rect = self.image.get_rect()  # set the rectangle to be the size of the image.
        self.rect.center = self.center  # position the button
        self.mouse = pygame.mouse.get_pos()
        self.check_hover()  # check if mouse is hovering
        self.color()  # change color of background of label

    def check_hover(self):
        '''adjust is_hover value based on mouse over button - to change hover color'''
        if self.rect.collidepoint(self.mouse):
            self.is_hover = True
        else:
            self.is_hover = False

    def color(self):
        '''change color when hovering'''
        if self.is_hover == True:
            self.background = (255, 0, 0)
        else:
            self.background = (212, 170, 255)

    def click(self):
        '''return true or false based on mouse over the button '''
        if self.rect.collidepoint(self.mouse):
            return True
        else:
            return False

class Label(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.text = ""
        self.center = (500, 200)
        self.colour = (0, 0, 0)
        self.backcolour = (175, 255, 193)

    def update(self):
        self.image = self.font.render(self.text, 1, self.colour, self.backcolour)
        self.rect = self.image.get_rect()
        self.rect.center = self.center


# Display configuration


def main():
    global score
    pygame.display.set_caption("Popping the Question")

    background = pygame.Surface(screen.get_size())
    background.fill((141, 233, 252))
    screen.blit(background, (0, 0))

    balloon1 = Balloon1()
    balloon2 = Balloon2()
    balloon3 = Balloon3()
    balloon4 = Balloon4()
    balloon5 = Balloon5()
    cloud1 = Cloud()
    clouds = []
    balloons = []

    strike1 = Strike1()
    strike2 = Strike2()
    strike3 = Strike3()

    for i in range(1, 2):
        cloud = Cloud()
        clouds.append(cloud)

    for r in range(2):
        balloon11 = Balloon1()
        balloon22 = Balloon2()
        balloon33 = Balloon3()
        balloon44 = Balloon4()
        balloon55 = Balloon5()
        balloons.append(balloon11)
        balloons.append(balloon22)
        balloons.append(balloon33)
        balloons.append(balloon44)
        balloons.append(balloon55)

    pin = Pin()
    counter = 0  # strike counter
    balloonGroup = pygame.sprite.Group(balloons, balloon1, balloon2, balloon3, balloon4, balloon5, strike1, strike2,
                                       strike3)
    allSprites = pygame.sprite.Group(cloud1, clouds, pin)

    # hide the mouse
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(pin, balloonGroup,
                                               True):  # if the mouse clicks a sprite, it goes to the new screen
                    pop.play()  # sound
                    success = newScreen()  # if they get the correct answer
                    if success == True:
                        print("That is the correct answer")
                        correct.play()
                        score = (score + 100)  # adds 100 points to the score if they answer correctly
                        print("Score:", score)
                        if score == 800:  # once the player gets 800 points they go to the finish screen
                            yay.play()
                            keepGoing = False
                            finishScreen()

                    if success == False:  # if they get the answer wrong
                        counter = (counter + 1)
                        if counter == 1:
                            strike.play()  # counts the strikes - if they get 3 strikes the game is over - they go to the finish screen
                            strike1.kill()
                        elif counter == 2:
                            strike.play()
                            strike2.kill()
                        elif counter == 3:
                            lose.play()
                            strike3.kill()
                            keepGoing = False
                            finishScreen()

                    screen.blit(background, (0, 0))

        allSprites.clear(screen, background)
        balloonGroup.clear(screen, background)

        allSprites.update()
        balloonGroup.update()

        allSprites.draw(screen)
        balloonGroup.draw(screen)

        # return mouse
        pygame.mouse.set_visible(True)
        pygame.display.flip()


def newScreen():
    global score
    pygame.display.set_caption("Popping the Question")

    background = pygame.Surface(screen.get_size())
    background.fill((141, 233, 252))
    screen.blit(background, (0, 0))

    pin = Pin()
    allSprites = pygame.sprite.Group(pin)

    questionList = [

        ["What planet is the closest to Earth", "Venus", "Jupiter", "Pluto", "Neptune", "Venus", "one"],
        ["Which is the tallest mammal?", "Giraffe", "Elephant", "Brown Bear", "Bison", "Giraffe", "one"],
        ["What mountain range is Mount Everest found in?", "Himalayas", "Rockies", "Alps", "Andes", "Himalayas", "one"],
        ["How many strings does a violin have?", "four", "five", "six", "seven", "four", "one"],
        ["Which one of these is not a blood type for humans?", "   C   ", "   A   ", "   O   ", "   AB   ", "   C   ",
         "one"],
        ["Which one of these is NOT a secondary colour?", "yellow", "green", "orange", "purple", "yellow", "one"],

        ["How many chambers are in the human heart?", "three", "four", "five", "six", "four", "two"],
        ["What is the name of the fairy in Peter Pan", "Silvermist", "Tinkerbell", "Iridessa", "Fawn", "Tinkerbell",
         "two"],
        ["What is the longest river in the world?", "Nile", "Amazon", "Mississippi", "Danube", "Amazon", "two"],
        ["What is the most popular drink in the world that doesn't contain alcohol?", "Coca Cola", "Coffee", "Water",
         "Juice", "Coffee", "two"],
        ["A word which is the opposite of another word is called a _______?", "synonym", "antonym", "adverb",
         "adjective", "antonym", "two"],
        ["Where did the 2010 winter olympics take place?", "Sochi", "Vancouver", "Beijing", "Salt Lake City",
         "Vancouver", "two"],

        ["What is the world's largest ocean?", "Atlantic", "Indian", "Pacific", "Arctic", "Pacific", "three"],
        # the last item of the list corresponds to the correct answer which is checked later
        ["Babe Ruth is associated with which sport?", "Basketball", "Hockey", "Baseball", "Football", "Baseball",
         "three"],  # to see if they get the right answer or not
        ["Who directed the movie 'Jaws'?", "James Cameron", "Tim Burton", "Steven Spielberg", "Woody Allen",
         "Steven Spielberg", "three"],
        ["What is the largest fish in the ocean", "Salmon", "Blue Whale", "Whale Shark", "Salmon", "Whale Shark",
         "three"],
        ["What is the name of the currency used in Mexico", "Euros", "Pounds", "Pesos", "Yens", "Pesos", "three"],
        ["Ageusia is the loss of which sense?", "Sight", "Touch", "Taste", "Smell", "Taste", "three"],

        ["What is measured in Kelvins?", "Sound", "Pressure", "Volume", "Temperature", "Temperature", "four"],
        # the second last thing in the list is for if they get the question wrong, it prints
        ["Which mineral is spinach high in?", "Calcium", "Potassium", "Magnesium", "Iron", "Iron", "four"],
        # that item which is the same as the correct answer
        ["What is the most spoken language in the world?", "English", "French", "German", "Chinese", "Chinese", "four"],
        ["Which fictional city is the home of Batman?", "Azarath", "Silver City", "Metropolis", "Gotham City",
         "Gotham City", "four"],
        ["The Dewey Decimal system is used to categorise what?", "Music", "Movies", "TV shows", "Books", "Books",
         "four"],
        ["What is the world's biggest island?", "Japan", "Finland", "Greece", "Greenland", "Greenland", "four"]

    ]

    qChoice = (random.randrange(0, len(questionList)))  # generates a random question from the list

    question1 = Label()  # turns the question into a label
    question1.text = questionList[qChoice][0]  # sets the question as the first item in the list

    btn1a = Button(questionList[qChoice][1], 400, 400)
    btn1b = Button(questionList[qChoice][2], 400, 450)  # setting the multiple choice buttons for a-d
    btn1c = Button(questionList[qChoice][3], 600, 400)
    btn1d = Button(questionList[qChoice][4], 600, 450)

    labelGroup = pygame.sprite.Group(question1)

    buttonGroup = pygame.sprite.Group(btn1a, btn1b, btn1c, btn1d)

    # hide the mouse
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            elif event.type == pygame.MOUSEBUTTONDOWN:  # if the button choice and correct answer match they get 100 points
                if questionList[qChoice][6] == "one" and btn1a.click() == True:
                    # questionList.remove([qChoice])
                    # supposed to remove a question but would require lots of thinking because the questionList gets regenerated for every question
                    # and the questions would need to be added back in if the player decides to play again
                    keepGoing = False
                    return True
                elif questionList[qChoice][6] == "two" and btn1b.click() == True:
                    keepGoing = False
                    return True
                elif questionList[qChoice][6] == "three" and btn1c.click() == True:
                    return True
                elif questionList[qChoice][6] == "four" and btn1d.click() == True:
                    return True
                else:
                    print('The correct answer was: ', questionList[qChoice][
                        5])  # the 6th thing in the list is the correct answer for all questions (not used with buttons - just to print correct answer)
                    keepGoing = False
                    return False

        allSprites.clear(screen, background)
        labelGroup.clear(screen, background)
        buttonGroup.clear(screen, background)

        labelGroup.update()
        allSprites.update()
        buttonGroup.update()

        allSprites.draw(screen)
        labelGroup.draw(screen)
        buttonGroup.draw(screen)

        # return mouse
        pygame.mouse.set_visible(True)
        pygame.display.flip()


def introScreen():
    backtrack.play(-1)  # loops the background sound

    pygame.display.set_caption("Popping the Question")

    background = pygame.Surface(screen.get_size())
    background.fill((141, 233, 252))
    screen.blit(background, (0, 0))

    startballoon = []
    for r in range(5):  # to create more balloons at once through an inventory
        balloons = Plainballoon()
        startballoon.append(balloons)

    strike1 = Strike1()
    strike2 = Strike2()
    strike3 = Strike3()

    title = Label()
    title.text = ("POPPING THE QUESTION: TRIVIA GAME")
    title.font = pygame.font.SysFont("Comic Sans MS", 35)
    title.center = (500, 26)
    title.colour = (252, 0, 0)
    title.backcolour = (70, 167, 252)

    explain1 = Label()
    explain1.text = ("In this game there will be balloons like the ones you see in the background- they will bring")
    explain1.center = (500, 100)

    explain2 = Label()
    explain2.text = (
        "up a trivia question when clicked on. They are multiple choice questions, and if you answer correctly,")
    explain2.center = (500, 135)

    explain3 = Label()
    explain3.text = (
        "100 points will be added to your score which is displayed at the bottom. If you get a question")  # explains how the game works
    explain3.center = (500, 170)

    explain4 = Label()
    explain4.text = ("incorrect, you will lose one of your three strikes on the bottom right corner of the screen, ")
    explain4.center = (500, 205)

    explain5 = Label()
    explain5.text = (
        "if you lose all 3 strikes, the game is over! To win you must get 800 points (8 questions correct).")
    explain5.center = (500, 240)

    explain6 = Label()
    explain6.text = ("Good Luck!")
    explain6.center = (500, 275)

    nextPage = Label()
    nextPage.text = "Press the space bar when you are ready!"
    nextPage.center = (500, 325)
    nextPage.backcolour = (255, 204, 237)

    introText = pygame.sprite.Group(startballoon, title, explain1, explain2, explain3, explain4, explain5, explain6,
                                    nextPage, strike1, strike2, strike3)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # if they press the space bar they get forwarded to the main page
                    keepGoing = False
                    correct.play()
                    main()

        introText.clear(screen, background)
        introText.update()
        introText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def finishScreen():
    global score

    pygame.display.set_caption("Popping the Question")

    background = pygame.Surface(screen.get_size())
    background.fill((141, 233, 252))
    screen.blit(background, (0, 0))

    playAgain = Label()
    playAgain.text = ("Would you like to play again?")
    playAgain.center = (500, 335)
    playAgain.backcolour = (165, 255, 180)

    ask = Label()
    ask.text = ("Yes - Press space           No - Press x")
    ask.center = (500, 375)
    ask.backcolour = (210, 171, 242)

    finalScore = Label()
    finalScore.text = (
                "Your final score is: " + str(score))  # turns the score into a string so it can be used in the label
    finalScore.center = (500, 295)
    finalScore.backcolour = (248, 255, 130)

    intro = Label()
    intro.text = ("Or press tab to view the instruction screen again")
    intro.center = (500, 420)
    intro.backcolour = (252, 159, 239)

    finballoon = []
    for r in range(5):
        balloonf = finBalloon()
        finballoon.append(balloonf)

    clouds = []
    for i in range(2):
        cloud = Cloud()
        clouds.append(cloud)

    finalText = pygame.sprite.Group(clouds, finballoon, playAgain, ask, finalScore, intro)

    # hide the mouse
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # if they press x the game exits
                    exit()
                elif event.key == pygame.K_SPACE:  # if they press space the game restarts with a score of 0
                    keepGoing = False
                    score = 0
                    correct.play()
                    main()
                elif event.key == pygame.K_TAB:
                    keepGoing = False
                    correct.play()
                    introScreen()

        finalText.clear(screen, background)
        finalText.update()
        finalText.draw(screen)

        # return mouse
        pygame.mouse.set_visible(True)
        pygame.display.flip()


if __name__ == "__main__":
    introScreen()
