from pygame import * 
import pyganim
from settings import Settings as Stg
from block import Spikes


class Player(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0                                   # Speed for moving - standing
        self.startX = x                                 # Start position x
        self.startY = y                                 # Start position y
        self.image = Surface((Stg.WIDTH, Stg.HEIGHT))
        self.image.fill(Color(Stg.COLOR))
        self.rect = Rect(x, y, Stg.WIDTH, Stg.HEIGHT)   # Creating rectangular object
        self.yvel = 0
        self.onGround = False
        self.image.set_colorkey(Color(Stg.COLOR))       # Making background transparent

        # Animation moving in right
        boltAnim = []
        for anim in Stg.ANIMATION_RIGHT:
           boltAnim.append((anim, Stg.ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        # Animation moving in left     
        boltAnim = []
        for anim in Stg.ANIMATION_LEFT:
           boltAnim.append((anim, Stg.ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
                
        # Animation standing
        boltAnim = []
        for anim in Stg.ANIMATION_STAY:
            boltAnim.append((anim, Stg.ANIMATION_DELAY_STAY))
        self.boltAnimStay = pyganim.PygAnimation(boltAnim)
        self.boltAnimStay.play()
                
        # Animation jump in left       
        self.boltAnimJumpLeft= pyganim.PygAnimation(Stg.ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()
                
        # Animation jump in right        
        self.boltAnimJumpRight= pyganim.PygAnimation(Stg.ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
                
        # Animation jump         
        self.boltAnimJump= pyganim.PygAnimation(Stg.ANIMATION_JUMP)
        self.boltAnimJump.play()

        # Animation death
        # boltAnim = []
        # for anim in Stg.ANIMATION_DEATH:
        #     boltAnim.append((anim, Stg.ANIMATION_DELAY))
        # self.boltAnimDeath = pyganim.PygAnimation(boltAnim)
        # self.boltAnimDeath.play()

    def update(self,  left, right, up, platforms):
        '''Moving animation and treatment'''
        if up:                                          # Arrow up
            if self.onGround:

                # jump sounds
                mixer.music.load("sounds/jump.mp3")
                mixer.music.play()

                self.yvel = -Stg.JUMP_POWER
            self.image.fill(Color(Stg.COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:                                        # Arrow left
            self.xvel = -Stg.MOVE_SPEED                 # Left = x- n
            self.image.fill(Color(Stg.COLOR))
            if up:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:                                       # Arrow right
            self.xvel = Stg.MOVE_SPEED                  # Right = x + n
            self.image.fill(Color(Stg.COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not(left or right):                          # If not moving
            self.xvel = 0
            if not up:
                self.image.fill(Color(Stg.COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:                           # If we are in the air
            self.yvel += Stg.GRAVITY

        self.onGround = False
        self.rect.y += self.yvel
        self.collide_platforms(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide_platforms(self.xvel, 0, platforms)
    
    def collide_platforms(self, xvel, yvel, platforms):
        '''Collision with platforms'''
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, Spikes):
                    self.die()

                if xvel > 0:                        # If collision right
                    self.rect.right = p.rect.left

                if xvel < 0:                        # If collison left
                    self.rect.left = p.rect.right

                if yvel > 0:                        # if collisoin up
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:                        # if collison down
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

    def die(self):
        """If we die, return to the starting place"""
        time.wait(70)
        self.teleporting(self.startX, self.startY)

    def teleporting(self, goX, goY):
        """Change the position to zero"""
        self.rect.x = goX
        self.rect.y = goY
