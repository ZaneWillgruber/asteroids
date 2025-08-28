import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # groups
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # bullets
    Shot.containers = (shots, updatable, drawable)

    # asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    # asteroid field
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    # player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        for item in updatable:
            item.update(dt)

        # asteroids
        for a in asteroids:
            for s in shots:
                if a.check_collide(s):
                    s.kill()
                    a.split()
                    break

            if a.check_collide(player):
                print("Game over!")
                return

        screen.fill("black")

        # draw
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
