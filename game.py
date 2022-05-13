import pygame

def checkWalls(direction):
    bool = True

    if direction == 'haut':
        wall = perso_pos.top - moy_y
        wall2 = perso_pos.left
        print(len(walls))
        for case in walls:
            if case[1] == wall and case[0] == wall2:
                bool = False

    if direction == 'bas':
        wall = perso_pos.top + moy_y
        wall2 = perso_pos.left
        for case in walls:
            if case[1] == wall and case[0] == wall2:
                bool = False

    if direction == 'gauche':
        wall2 = perso_pos.top
        wall = perso_pos.left - moy_X
        for case in walls:
            if case[0] == wall and case[1] == wall2:
                bool = False

    if direction == 'droite':
        # position = perso_pos.left
        wall = perso_pos.left + moy_X
        wall2 = perso_pos.top
        for case in walls:
            if case[0] == wall and case[1] == wall2:
                bool = False

    print("bool", bool)
    return bool

def pushCrate(direction):
    if direction == 'haut': #-y
        ...
        
    if direction == 'bas': #+y
        ...
    
    if direction == 'gauche': #+x
        ...
    
    if direction == 'droite': #-x
        ...


level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 9, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

walls = []
crates = []

height = 1024
width = 1024

i = 0
for row in level:
    for case in row:
        i += 1
    break

moy_y = height/len(level)
moy_X = width/i

pygame.init()
fenetre = pygame.display.set_mode((height, width))

espace_vide = pygame.image.load("images/ground.png").convert()
espace_vide = pygame.transform.scale(espace_vide, (moy_X, moy_y))

mur = pygame.image.load("images/wall.png").convert()
mur = pygame.transform.scale(mur, (moy_X, moy_y))

perso = pygame.image.load("images/perso.png").convert_alpha()
perso = pygame.transform.scale(perso, (moy_X, moy_y))

perso_l = pygame.image.load("images/perso_left.png").convert_alpha()
perso_l = pygame.transform.scale(perso_l, (moy_X, moy_y))

crate = pygame.image.load("images/crate.png").convert()
crate = pygame.transform.scale(crate, (moy_X, moy_y))


# image sans transparence rendre la couleur de fond transparente,
# méthode Surface set_colorkey(),

x = 0
y = 0
for ligne in level:
    for case in ligne:
        if(case == 0):
            fenetre.blit(espace_vide, (x, y))

        elif(case == 1):
            fenetre.blit(mur, (x, y))
            walls.append([int(x), int(y), int(moy_X), int(moy_y)])
            
        elif(case == 9):
            fenetre.blit(perso, (x, y))
            perso_pos = perso.get_rect()
            perso_pos.top = y
            perso_pos.left = x

        elif(case == 2):
            fenetre.blit(crate, (x, y))
            crates.append([int(x), int(y), int(moy_X), int(moy_y)])


        x += moy_X
    x = 0
    y += moy_y
    pygame.display.flip()

pygame.display.flip()

pygame.font.init()
continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.type)

            if event.type == pygame.K_ESCAPE:
                print("K_ESCAPE" + pygame.K_ESCAPE)
                continuer = 0

            elif event.key == pygame.K_DOWN:
                couscous = checkWalls('bas')
                print(couscous)
                if couscous:
                    print('passé dedans')
                    perso_pos = perso_pos.move(0, moy_y)
                    fenetre.blit(espace_vide, (perso_pos.left,
                                               perso_pos.top - moy_y))

            elif event.key == pygame.K_UP:
                couscous = checkWalls('haut')
                if couscous:
                    print('passé dedans')
                    perso_pos  = perso_pos.move(0, -moy_y)
                    fenetre.blit(espace_vide, (perso_pos.left,
                                               perso_pos.top + moy_y))

            elif event.key == pygame.K_LEFT:
                couscous = checkWalls('gauche')
                if couscous:
                    print('passé dedans')
                    perso_pos = perso_pos.move(-moy_X, 0)
                    fenetre.blit(espace_vide, (perso_pos.left +
                                               moy_X, perso_pos.top))

            elif event.key == pygame.K_RIGHT:
                couscous = checkWalls('droite')
                if couscous:
                    print('passé dedans')
                    perso_pos = perso_pos.move(moy_X, 0)
                    fenetre.blit(espace_vide, (perso_pos.left - moy_X, 
                                               perso_pos.top))

        fenetre.blit(perso, perso_pos)
        print(perso_pos)

        pygame.display.update()
        pygame.display.flip()