import pygame,simpleGE,random
"""
Help Charlie The Cardinal save earth!
Asteriods will fall. Destory them before
they hit earth. You will
lose a life if it does. Use
the left arrow to move left, 
and the right arrow to move right.
Click Space Bar to shoot! Lose
three lifes you lose. Score 100
and you win. Have fun!

Asteriod Image: https://opengameart.org/content/brown-asteroid
Galaxy Background Image: https://opengameart.org/content/space-bg-planets
Explosion Image: https://opengameart.org/content/pixel-explosion-12-frames
Laser Bullets Image: https://opengameart.org/content/bullet-collection-1-m484
Game Over Image: https://pngimg.com/image/83334
Heart: https://opengameart.org/content/life-icon-health-shield
Trophy: https://www.vecteezy.com/png/9315016-winner-trophy-in-flat-style
Explosion Sound: https://opengameart.org/content/explosion-0
Game over Sound: https://opengameart.org/content/lose-game-short-music-clip
Laser Sound: https://opengameart.org/content/shots
Win and lose life Sound: https://opengameart.org/content/oldschool-win-and-die-jump-and-run-sounds

Nolan Meyer

October 30, 2023
"""
#Class that stores all the game data
class Game(simpleGE.Scene):

    def __init__(self):
        super().__init__()
        
        self.setCaption("Asteroid Game")
        self.background = pygame.image.load("spaceBackground.png")
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background,((self.screen.get_size())))

        self.charlie = UserCharacter(self)

        self.asteriod = Asteriod(self)
        self.bullet = Bullet(self)

        self.heart1 = simpleGE.BasicSprite(self)
        self.heart1.setImage("heart.png")
        self.heart1.setSize(30,30)
        self.heart1.x = 550
        self.heart1.y = 20

        self.heart2 = simpleGE.BasicSprite(self)
        self.heart2.setImage("heart.png")
        self.heart2.setSize(30,30)
        self.heart2.x = 585
        self.heart2.y = 20

        self.heart3 = simpleGE.BasicSprite(self)
        self.heart3.setImage("heart.png")
        self.heart3.setSize(30,30)
        self.heart3.x = 620
        self.heart3.y = 20

        self.explosion = simpleGE.BasicSprite(self)
        self.explosion.setImage("explosion.png")
        self.explosion.setSize(50,50)
        self.explosion.x = -150
        self.explosion.y = -150

        self.gameOver = simpleGE.BasicSprite(self)
        self.gameOver.setImage("gameOver.png")
        self.gameOver.x = -150
        self.gameOver.y = -150
        self.gameOver.setSize(30,30)

        self.win = simpleGE.BasicSprite(self)
        self.win.setImage("win.png")
        self.win.setSize(30,30)
        self.win.x = -150
        self.win.y = -150

        self.score = 0
        self.scoreLabel = simpleGE.Label()
        self.scoreLabel.text = "Score: 0"
        self.scoreLabel.center = (50,15)

        self.winSound = simpleGE.Sound("round_end.wav")
        self.gameOverSound = simpleGE.Sound("gameOverSoud.wav")
        self.playSoundTimes = 1
        
        self.sprites = [self.charlie,self.asteriod,self.bullet,self.explosion,self.scoreLabel,self.heart1,self.heart2,
                        self.heart3,self.gameOver,self.win]


#User characters class for the cardinal

class UserCharacter(simpleGE.BasicSprite):

    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("Ball_State_Logo.png")
        self.setSize(50,50)
        self.x = 300
        self.y = 400
        self.health = 3
        self.canMove = True
        self.sound = simpleGE.Sound("death.wav")


    def checkEvents(self):

        if self.scene.isKeyPressed(pygame.K_RIGHT):

            if self.canMove:
                self.x += 5 

        if self.scene.isKeyPressed(pygame.K_LEFT):

            if self.canMove:
                self.x -= 5
        
        if self.scene.isKeyPressed(pygame.K_SPACE):

            if self.scene.bullet.fire == False:
                self.scene.bullet.x = self.scene.charlie.x
                self.scene.bullet.y = self.scene.charlie.y
                self.scene.bullet.fire = True
                self.scene.bullet.sound.play()
        
        self.scene.bullet.shoot()
        self.checkScore()
    

    def checkScore(self):

        if self.scene.score == 100:
            
            self.scene.win.setSize(200,200)
            self.scene.win.x = 320
            self.scene.win.y = 240
            self.scene.asteriod.fall = False
            self.scene.bullet.fire = True
            self.scene.charlie.canMove = False

            if self.scene.playSoundTimes == 1:
                self.scene.winSound.play()
                self.scene.playSoundTimes += 1
                
    
    def checkHealth(self):
         
        if self.scene.charlie.health == 2:
            self.scene.heart1.setImage("noheart.png")
            self.scene.heart1.setSize(30,30)
            self.scene.charlie.sound.play()
            
        elif self.scene.charlie.health == 1:
            self.scene.heart2.setImage("noheart.png")
            self.scene.heart2.setSize(30,30)
            self.scene.charlie.sound.play()
            
        elif self.scene.charlie.health == 0:
            self.scene.heart3.setImage("noheart.png")
            self.scene.heart3.setSize(30,30)
            self.scene.charlie.sound.play()

            self.scene.gameOver.x = 320
            self.scene.gameOver.y = 240
            self.scene.gameOver.setSize(200,200)

            self.scene.charlie.canMove = False
            self.scene.asteriod.fall = False
            self.scene.bullet.fire = True

            self.scene.gameOverSound.play()
 

#Class for the asteriod that will be falling

class Asteriod(simpleGE.BasicSprite):

    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("asteroid.png")
        self.setSize(30,30)
        self.fall = True
        self.reset()
        self.sound = simpleGE.Sound("explosion.wav")
    
    def reset(self):

        self.x = random.randint(0,640)
        self.y = 20
        self.fallSpeed = 5
        
    
    def checkEvents(self):

        if self.fall == True:
            self.y += self.fallSpeed
        
        self.checkCollision()
    
    
    def checkBounds(self):
        
        if self.rect.bottom > self.scene.background.get_height():
            self.reset()
            self.scene.charlie.health -= 1
            self.scene.charlie.checkHealth()
    

    def checkCollision(self):

        if self.collidesWith(self.scene.bullet):

            self.scene.bullet.x = 1000
            self.scene.bullet.y = 1000

            self.scene.explosion.x = self.x
            self.scene.explosion.y = self.y
            
            self.scene.bullet.fire = False

            self.sound.play()

            self.scene.score += 10
            self.scene.scoreLabel.text = f"Score: {self.scene.score}"

            self.reset()
        
        
#This is the bullet class that will be shot from charlie

class Bullet(simpleGE.BasicSprite):

    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("bullet.png")
        self.setSize(15,30)
        self.x = 1000
        self.y = 1000
        self.speed = 7
        self.fire = False
        self.sound = simpleGE.Sound("laserSound.wav")

    def shoot(self):
        
        if self.fire == True:
             
             self.y -= self.speed
            
    
    def checkBounds(self):
        
        if self.rect.bottom < 0:
            self.fire = False
            self.x = 1000
            self.y = 1000


#Main function that creates an instant of game and starts the game
def main():
    
   game = Game()
   game.start()

#Calling of main
if __name__ == "__main__":
    main()