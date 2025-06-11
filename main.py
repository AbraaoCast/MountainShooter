import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 400))
print('Setup End')

print('Loop Start')
while True:
    # Checar todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Fecha a janela
            quit()
