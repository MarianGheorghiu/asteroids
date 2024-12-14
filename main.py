# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for player_obj in updatable:
            player_obj.update(dt)
            
        for asteriod_obj in asteroids:
            if asteriod_obj.check_collisions(player):
                print("Game over!")
                sys.exit()
                
        for shot in shots:
            if asteriod_obj.check_collisions(shot):
                shot.kill()
                asteriod_obj.split()
          
        screen.fill("black")
        
        for player_obj in drawable:
            player_obj.draw(screen)
            
        pygame.display.flip()

        # limit 60 FPS max, for good performance
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()