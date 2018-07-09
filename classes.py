import sys, pygame, random

class Bird:
     pass

class Pipes:
     def __init__(self, n, birdRect, screen):
          self.image = pygame.image.load("pipe.bmp")
          self.pairs = []
          self.windowHeight = screen.get_height()
          self.windowWidth = screen.get_width()
          self.offset = self.windowWidth / 2
          self.gap = 2.5 * birdRect.height
          for i in range(n):
               self.pairs.insert(i, {
                    "upperRect": self.image.get_rect(),
                    "lowerRect": self.image.get_rect()
               })
          self.place()

     def place(self):
          for i in range(len(self.pairs)):
               end = self.windowHeight - (4/5) * self.pairs[i]['upperRect'].height
               self.pairs[i]['upperRect'].bottom = random.randrange(30, self.windowHeight - int(end))
               self.pairs[i]['lowerRect'].top = self.pairs[i]['upperRect'].bottom + self.gap
               self.pairs[i]['upperRect'].left = self.windowWidth + i * self.offset
               self.pairs[i]['lowerRect'].left = self.pairs[i]['upperRect'].left

     def move(self, speed):
          for i in range(len(self.pairs)):
               end = self.windowHeight - (4/5) * self.pairs[i]['upperRect'].height
               if self.pairs[i]['upperRect'].left <= -self.offset:
                    self.pairs[i]['upperRect'].left = self.windowWidth
                    self.pairs[i]['upperRect'].bottom = random.randrange(30, self.windowHeight - int(end))
                    self.pairs[i]['lowerRect'].top = self.pairs[i]['upperRect'].bottom + self.gap
               else:
                    self.pairs[i]['upperRect'].left -= speed
               self.pairs[i]['lowerRect'].left = self.pairs[i]['upperRect'].left

     def blit(self, screen):
          for i in range(len(self.pairs)):
               screen.blit(self.image, self.pairs[i]['upperRect'])
               screen.blit(self.image, self.pairs[i]['lowerRect'])