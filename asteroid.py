import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        print(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = self.velocity * 1.2
        a2.velocity = self.velocity * 1.2

        a1.velocity = a1.velocity.rotate(angle)
        a2.velocity = a2.velocity.rotate(-angle)   
        print(a1.velocity)
        print(a2.velocity)
        print()