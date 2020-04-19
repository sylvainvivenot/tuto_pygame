import pygame

from game import Game

pygame.init()

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))
game = Game()
background = pygame.image.load('assets/bg.jpg')

running = True

while running:

    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)
    for projectile in game.player.all_projectiles:
        projectile.move()

    for monster in game.all_monsters:
        monster.forward()

    game.player.all_projectiles.draw(screen)
    game.all_monsters.draw(screen)
    pygame.display.flip()

    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            else:
                game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
