# -- coding: utf-8 --
"""game"""
import pygame
from pygame import *
from player import *
from block import *
#Объявляем переменные
WIN_WIDTH = 1570 #Ширина создаваемого окна
WIN_HEIGHT = 810 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную

DARTGREEN = (0,100,0)
WHITE = "#FFFFFF"
coins = []
teleport = []
ices = []


background = pygame.image.load('forgame/background.jpg')
level1BG = pygame.image.load('forgame/level1.png')
level2BG = pygame.image.load('forgame/level2.png')
level3BG = pygame.image.load('forgame/level3.jpg')
level4BG = pygame.image.load('forgame/level4.jpg')
level5BG = pygame.image.load('forgame/level5.jpg')
level6BG = pygame.image.load('forgame/level6.png')

flag1 = pygame.image.load('forgame/flag.png')
town = pygame.image.load("forgame/Skyscraper_Buildings _pack_OldNinjaCat_v1.png")
town = pygame.transform.scale(town,(8700, 8700//3.18))

town2 = pygame.image.load("forgame/Skyscraper_Buildings _pack_OldNinjaCat_v1.png")
town2 = pygame.transform.scale(town,(8700, 8700//3.18))

town3 = pygame.image.load("forgame/Skyscraper_Buildings _pack_OldNinjaCat_v1.png")
town3 = pygame.transform.scale(town,(8700, 8700//3.18))

pygame.init() # Инициация PyGame, обязательная строчка 
screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
pygame.display.set_caption("I wanna be the Cat") # Пишем в шапку
bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
bg.blit(background,(0,0))    # Заливаем поверхность сплошным цветом

level = [
        "9999999999999999999999999999999999999999999999999",
        "9       9                9                      9",
        "9       9                9                      9",
        "9       9                9                      9",
        "9       9       999999   9         9999999999   9",
        "999999  999999  9        99999999  9            9",
        "9       9       9        9         9            9",
        "9       9       9   999999         9   9999999999",
        "9  999999   99999        9   9999999            9",
        "9       9       9        9         9            9",
        "9       9       999999   9         9999999999   9",
        "999999  999999  9        99999999  9            9",
        "9       9       9        9         9            9",
        "9       9       9   999999         9   9999999999",
        "9  999999   99999        9   9999999            9",
        "9       9       9        9         9            9",
        "9       9       999999   9         9999999999   9",
        "999999  999999  9        99999999  9            9",
        "9       9       9        9         9            9",
        "9       9       9   999999         9   9999999999",
        "9  999999   99999        9   9999999            9",
        "9               9                  9            9",
        "9               9                  9            9", 
        "9999999999999999999999999999999999999999999999999",
        "-********///////**-******-/////////*--------****-"]

        #T - Техтура земли
        #s - stoune
        #- - zemlya
        #F-FAKE PLATFORMS/SHIP
        #L- LOVUSKA
        #M - MONETKA
        #N - NEXT
        #W-WATER
        #B - BUTTON
        #P - TELEPORT
        #A - ART KILL
        #LOCK-OPEN O
        #l - liana
        #t - zemlya s travoi
        #U - up platf
        #R - x platf
level2 = [
"----------------------------------------------------------------------------------------------",
"-                                                                                            -",
"-                                                                                     SSSSSSS-",
"-                                                        M                            SSSSSSS-",
"-                 ttttttttttttttFttttttttttttttttttttwttttttttttttttttttttttttl              -",
"-                 t                                 twt                      Tl              -",
"-            M    t                                 twt                      Tl           B  -",
"-                 l             M                   twt                      Tl       WSSSSSSS-",
"-         ttttttttl              tt                                          Tl       WSSSSSSS-",
"-                 l             L                                            T        WSSSSSSS-",
"-                                                                        TTTTTFTTTTTTT       -",
"-                                                                M   TTTT             SSSSSSS-",
"-TTTTTTTTTTTTTTTTTTTTTTl     L     L    M      L                TTTTT                 SSSSSSS-",
"-TTTTTTTTTTTTTTTTTTTTTTl           lTTTTTTTTTTTTT          lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTTTTTTl            FFFFFFFFFFFFF   -      lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTTTTTTl           lTTTTTFTTTTTTT          lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTTTTTT                  M      T    U     lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTFFFFF                         l          lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTFTTTT                         l          lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTFTTTT                         l          lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTFTTTTTTTTTT                   l          lTTTTT                     SSSSSSS-",
"-TTTTTTTTTTTTTTTTTFTTTTT PL T  U                            TTTTT             U       SSSSSSS-",
"-TTTTTTTTTTTTTTTTTFFFFFF  M T                               TTTTT          M          SSSSSSS-", 
"-TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTSSSSSSS-",
"----------------------------------------------------------------------------------------------"]

level3 = [
"----------------------------------------------------------------------------------------------",
"LLLLLLLLLLLL                            WWFWWWWS            TTT S                          -",
"SM                                        WWFWWWWS            TTT S              S             -",
"SSSSSSSSSSSSSl                           WWFWWWWS            TTT S             S    TTTTTTTTT-",
"S            l                           WWFWWWMS            TTT S      T       S    TTTTTTTTT-",
"S                               LL     LLWWFWWWWS                S             S   TTTTTTTTT-",
"S                     B             L    WWFWWWWS                S M             S           -",
"S       SSSSSSSSSSSSSSSSSSSSLLSSSSSSSSSSSSSSSSSSSSSSSSSFSSSSSS  SSS T     T     S             -",
"S               M                     FF               SS        S              S            -",
"SSSSSSSSSSSSSSSSSSSSSSS               SS          M  SSSS    FS  S     T       S    L   LM   -",
"-  l  l    S     l FFFF               SS       SSSSSSSSSS        S         T    S   TTTTTTTTT-",
"-  l  l M  S     l SSSSSSSSSSSSSSSSSSSSS               SS  FS    S             S            -",
"-  l  l    S     l                    S   B            SS  LL    S   T          S            -",
"-  l       S          SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS        S             S            -",
"-  l       S      B           LLLLLL                   SS     SFSST      LTTTT  S             -",
"-  l       STTlFTFFFFTTTTWWWWWWWWWWLLLLLLLLLLLLLLLLLLLLSS      LLS   L         S TTTT       -",
"-  l          l LLLLL    LLLLWWWWWWWWWWWWWWWWWWWWWWWW  SSSSS     S  TTT         S      TTTTTT-",
"-  l          l            LLLWWWWWWWWWWWWWWWWWWWWWWWW SSLLL     S   L         S            -",
"-  l                         LLLLLLLLLLLLLLLLLLLWWWWWWWSS         S  TTTTTTTT    S            -",
"-                                               LWWWWWWSS                   TT S            -",
"-                    B  LLLLLLLLLLLLLLLLLLLLLLLLWWWWWWWSS   FF       TTT        S    TTT     -",
"TTTTTTTTTTTTTTTTWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWSS   LL  TTT            S        TTTT -",
"TTTTTTTTTTTTTTTTTTWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWSS       TTWWWWWWWWWWTTTTTTTTTTTSSSSS-", 
"TTTTTTTTTTTTTTTTTTTTTTTTTLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLSSLLLLLLLTTTWWWWWWWWTSSSSSSSSSSSSSSSS-",
"----------------------------------------------------------------------------------------------"]
level4 = [
"----------------------------------------------------------------------------------------------",
"-SSSSSSSSSSS                                                     TT                          -",
"-SSSSSSSSSSS                                                     TT                          -",
"-         FF                                                     TT                          -",
"-         FF                                                     TT                          -",
"-         FF             B                       B               TT LLLLL        TTTTTL     L-",
"-SSS      SS       SSSFFFFFF  FFFF   FF  TTTTTSSSSSSS            TT              TTTTT       -",
"-         SS       SSSLLLLLLLLLLLLLLLLLLLSSSSS  M TTT            TT              TTTTTLLL    -",
"-         SS       SSS        M          SSSSS    TTT         M  TT      LLLLLL  TTTTT       -",
"-     SSSSSS       SSS                   SSSSS  S TTT        TTTTTT              TTTTT       -",
"-         SS       SSS                   SSSSS    TTT            TT              TTTTT   LLLL-",
"-         SS       SSS-                  SSSSS    TTTM B         TT LLLLLL       TTTTT       -",
"-SSS      SS       SSS         C   -     SSSSSS   TTTTTTTT       TT              TTTTT       -",
"-         SS       SSS  -                SSSSSL   TTT            TT              TTTTTLLLL   -",
"-         SS       SSS       C           SSSSS    TTT       M BL TT              TTTTT   M   -",
"-         SS       SSS-            C     SSSSS   STTT  LL   TTTTTTT   UUUUUUU    TTTTT UUUUU -",
"-         SS       SSS      -      -     SSSSS    TTT                            TTTTT       -",
"-                  SSS                   SSSSS    TTT                   B        TTTTTLL N L -",
"-      FFFSSSS     SSSSWWWWWWWWWWWWWWWWWSSSSSSWWWSTTTTTTTTTTWWWWWWTTTTTTTTTTTTTTTTTTTTTTTTTTT-",
"-         SSSS     SSSWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWTTTTTTTTTTTTTTTTTTTTTTTTTTT-",
"-         SSSS     FFFWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWTTTTTTTTTTTTTTTTTTTTTTTTTTTTT-",
"-         SSSS     FFFWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTT-",
"-         SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS-", 
"-LLLLLLLLLSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS -",
"----------------------------------------------------------------------------------------------"]
level5 = [
"----------------------------------------------------------------------------------------------",
"-                 11111111111111111111111111111111111111111111111111111111111111111111111111111-",
"-                 1              1             1                        1    oooooooo1oooo   o1-",
"-                 1       c      1      Mс     1          c             1               o    o1-",
"-                 1              1      IIIII1 1       c     c          1     R      I       o1-",
"-                 1     c M c    F    IIIIIII1 1                        1    ooooooooo   LMM  1-",
"-                 1              F   IIIIIIII1      C            C      1   1111111111111111111-",
"-                 1       C      1111111111111 111    11111111111  1111111  1          1       -",
"-                 111111111111FFL               1  MMM1                     1          1      M-",
"-                1L      C        c   L       U 1  MMM1     111111  111111111          11   111-",    
"-                1     111111111L         1111111111111    11      11       FFFF               -",
"-                1     1L       1111111111                11      II1       FFFF               -",
"-                1I    1                                  1         1     I oooo               -",
"-                     II                      111111111   1     I   1       ooooC              -",
"-                 I        11111111111111111111           1    c    1     I oooo           U   -",
"-                   III                 1           1111111        I1       oooo               -",
"-                                       1         L11       c     c 1I      ooooC              -",
"-             ILI          III          1        111      I         1       oooo               -",
"-                22222                  1     ///1             U    1       oooo        U      -",
"-          21111111111111               1        11111FF1111 MMM    1       oooo               -",
"-         221           12              1                  111111   1       ooooWIIIIIIII      -",
"-        2221IIIIMM      22             1                       11111    U  ooooWW             -",
"-       22221IMIIIII        C           1                         C         ooooWWWWW          -", 
"-IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII-",
"-----------------------------//----------------------------------------------------------------"
        ]
#B -mob
level6 = [
"----------------------------------------------------------------------------------------------",
        "-SSSSSSSSoSSSSSSSSSSSoSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS-",
        "-SSS     oooSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSoSSSSSSSSSSSSSSSSSSSSSS           SSS-",
        "-SSS       o                                C  ooooo                              SSS-",
        "-SSS                                             oo                               SSS-",
        "-SSS    M                     c          M        o       C                       SSS-",
        "-SSSSSSSSSSS   U   SS                  RRRRR                                B  M  SSS-",
        "-SS       SSLLL    SS                                                     SSSSSSSSSSS-",
        "-SS      MSS       SS                   C      B                            ooooooSSS-",
        "- c  SSSSSSS    LLLSS       SSSSSSSSSSSSSSSSSSSSSSSSSSS                     o  oo SSS-",
        "-SS       SS   U   SS       SSSSSSSSSSSSSSSSSSoSSSSSSSSLLL  UUU L   U           o SSS-",
        "-SS                SS       SSSSSSSSSSSSSSSSSSSoSSSSSSS        LSL                SSS-",
        "-SSS           U   SS             o        C  ooo         L     L        -        SSS-",
        "-SSSSSSSSSSS                             M     o         LSL       UU   -L        SSS-",
        "-SS       SS                                              L            -LSL       SSS-",
        "-SS    M  SS           SSSS            RRRRR                             L     M  SSS-",
        "-SS    SSSSS                           C                             SSSSSSSSSSSSSSSS-",
        "-SS       SS                                                                      SSS-",
        "-SS       SS                                              RRR                     SSS-",
        "-SS     SSSS          M          M      A     M          M                        SSS-",
        "-SS                      RRR            RRR                                M      SSS-",
        "-SS       R                                                          -    ---     SSS-",
        "-oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooSSS-", 
        "-SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS-",
        "--------------------------------------------------------------------------------------"]

label = pygame.font.Font('forgame/minecraft-ten-font-cyrillic.ttf', 45)
lose_label = label.render('You Lose', False, WHITE)
restart_label = label.render('Try again', False, WHITE)
restart_label_rect = restart_label.get_rect(topleft=(WIN_WIDTH//2-100, WIN_HEIGHT//2-150))

def draw_text(text, font1, color, x, y):
    """DRAW"""
    text_surface = font1.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

class Camera(object):
    """camera"""
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        """apply"""
        return target.rect.move(self.state.topleft)

    def update(self, target):
        """update"""
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    """camera"""
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2
    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы
    return Rect(l, t, w, h)
def game_loop():
    """GAME LOOP"""
    running = True
    main_menu = image.load('forgame/mainmenu.png')
    while running:
        for event in pygame.event.get():
       GAMEPLAY
                running = False
        screen.blit(main_menu,(0, 0))
        draw_text("Main menu", label, (0,0,0), WIN_WIDTH // 2 - 520, WIN_HEIGHT // 2 - 50)

        #Start Button
        start_button = pygame.Rect(WIN_WIDTH // 2 - 615, WIN_HEIGHT // 2 + 10, 185, 60)
        pygame.draw.rect(screen, DARTGREEN, start_button)
        draw_text("Start", label, "#FFFFFF", WIN_WIDTH // 2 - 520, WIN_HEIGHT //2 + 35)

        exit_button = Rect(WIN_WIDTH //2 - 600, WIN_HEIGHT // 2 + 90, 150, 50)
        draw.rect(screen, DARTGREEN, exit_button)
        draw_text("Exit", label, "#FFFFFF", WIN_WIDTH // 2 - 520, WIN_HEIGHT // 2 + 113)
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(mouse):
                start_game()
            elif exit_button.collidepoint(mouse):
                exit_game()
        # Обновление экрана
        display.update()

def exit_game():
    """EXIT GAME"""
    pygame.quit()
    sys.exit()

def restart_game():
    """RESTART GAME"""
    # gameplay = False
    # levelcount = 1
    hero = Player(100, 55,1)
    entities = pygame.sprite.Group()
    entities.add(hero)
    # left = True
    # right = True
    # up = True
    # restart = True

GAMEPLAY = True
'''Начало игрового цикла '''
def start_game():
    """START GAME"""
    global GAMEPLAY, level, level2,coin_count
    levelcount = 6
    if levelcount == 1 or levelcount == 4:
        xhero = 100
        yhero = 100
    # elif levelcount > 1:
    #     xhero = 200
    #     yhero = 600
    elif levelcount == 3:
        xhero = 200
        yhero = 600
    elif levelcount == 6:
        xhero = 2200
        yhero = 100
    hero = Player(xhero,yhero,levelcount) # создаем героя по (x,y) координатам
    left = right = False # по умолчанию - стоим
    up = False
    draw_Level = True
    timer = pygame.time.Clock()
    game = True
    blinkBool1 = False
    blinkBool2 = False
    for event in pygame.event.get():
        if event.type == KEYUP:
            left = right = up = False

    while game:
        timer.tick(60) # Основной цикл программ
        #--------------------------fun----------------------
        if draw_Level:
            if levelcount == 1:
                bg.blit(level1BG,(0,0))
                entities = pygame.sprite.Group() # Все объекты
                platforms = [] # то, во что мы будем врезаться или опираться
                lians = []
                waters = []
                teleport = []
                ices = []

                entities.add(hero)

                x=y=0 # координаты
                for row in level: # вся строка
                    for col in row: # каждый символ
                        if col == "-":
                            pf = Platform(x,y)
                            entities.add(pf)
                            platforms.append(pf)
                        if col == "9":
                            pf1 = Block1Level(x,y)
                            entities.add(pf1)
                            platforms.append(pf1)
                        elif col == "/":
                            bdr = BlinkRunY(x,y,levelcount,1)
                            entities.add(bdr)
                            platforms.append(bdr)
                        elif col == "F":
                            b = BlockFake(x,y,levelcount,1)
                            entities.add(b)
                        elif col == "w":
                            w = BlockWater(x,y)
                            entities.add(w)
                            waters.append(w)


                        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
                    y += PLATFORM_HEIGHT    #то же самое и с высотой
                    x = 0
                total_level_width  = len(level[0])*PLATFORM_WIDTH# Высчитываем фактическую ширину
                total_level_height = len(level)*PLATFORM_HEIGHT
                draw_Level = False

            elif levelcount == 2 and draw_Level:
                bg.blit(level2BG,(0,0))
                entities = pygame.sprite.Group() # Все объекты
                platforms = [] # то, во что мы будем врезаться или опираться
                lians = []
                waters = []
                teleport = []
                ices = []
                entities.add(hero)
                x=y=0 # координаты
                countFake = 0
                for row in level2: # вся строка
                    for col in row: # каждый символ
                        if col == "-":
                            pf2 = Platform(x,y)
                            entities.add(pf2)
                            platforms.append(pf2)
                        elif col == "T":
                            ground = BlockBambuck1(x,y)
                            entities.add(ground)
                            platforms.append(ground)
                        elif col == "w":
                            w = BlockWater(x,y)
                            entities.add(w)
                            waters.append(w)
                        elif col == "M":
                            coin = BlockMonetka(x,y)
                            entities.add(coin)
                            coins.append(coin)
                        elif col == "l":
                            lian = BlockLiana(x,y)
                            entities.add(lian)
                            lians.append(lian)
                        ########
                        elif col == "L":
                            trapStatic = BlockTrapStatic(x,y)
                            entities.add(trapStatic)
                            platforms.append(trapStatic)
                        elif col == "S":
                            stone = BlockStone(x,y)
                            entities.add(stone)
                            platforms.append(stone)
                        elif col == "U":
                            blockDinamicY = BlockRunY(x,y,300,100)
                            entities.add(blockDinamicY)
                            platforms.append(blockDinamicY)
                        elif col == "R":
                            blockDinamicX = BlockRunX(x,y,20,20)
                            entities.add(blockDinamicX)
                            platforms.append(blockDinamicX)
                        elif col == "t":
                            blockGrass = BlockBambuck2(x,y)
                            entities.add(blockGrass)
                            platforms.append(blockGrass)
                        elif col == "F":
                            b = BlockFake(x,y,levelcount,2)
                            entities.add(b)
                            countFake += 1
                            if(countFake >= 2):
                                b = BlockFake(x,y,levelcount,1)
                                entities.add(b)
                        elif col == "P":
                            tp = BlockTeleport(x,y,1000,100)
                            entities.add(tp)
                            teleport.append(tp)

                        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоковa
                    y += PLATFORM_HEIGHT    #то же самое и с высотой
                    x = 0  #на каждой новой строчке начинаем с нуля
                total_level_width  = len(level2[0])*PLATFORM_WIDTH#Высчитываем фактическую ширину
                total_level_height = len(level2)*PLATFORM_HEIGHT
                draw_Level = False

            elif levelcount == 3:
                bg.blit(level3BG,(0,0))
                entities = pygame.sprite.Group() # Все объекты
                platforms = [] # то, во что мы будем врезаться или опираться
                lians = []
                waters = []
                teleport = []
                ices = []
                entities.add(hero)
                countFake = 0

                x=y=0 # координаты
                for row in level3: # вся строка
                    for col in row: # каждый символ
                        if col == "-":
                            pf2 = Platform(x,y)
                            entities.add(pf2)
                            platforms.append(pf2)
                        elif col == "T":
                            ground = BlockTree(x,y)
                            entities.add(ground)
                            platforms.append(ground)
                        elif col == "W":
                            w = BlockWater(x,y)
                            entities.add(w)
                            waters.append(w)
                        elif col == "B":
                            mob = MobX(x,y,50,50,levelcount)
                            entities.add(mob)
                            platforms.append(mob)
                        elif col == "M":
                            coin = BlockMonetka(x,y)
                            entities.add(coin)
                            coins.append(coin)
                        elif col == "l":
                            lian = BlockLiana(x,y)
                            entities.add(lian)
                            lians.append(lian)
                        ########
                        elif col == "L":
                            trapStatic = BlockTrapStatic(x,y)
                            entities.add(trapStatic)
                            platforms.append(trapStatic)
                        elif col == "S":
                            stone = BlockBarrel(x,y)
                            entities.add(stone)
                            platforms.append(stone)
                        elif col == "U":
                            blockDinamicY = BlockRunY(x,y,300,100)
                            entities.add(blockDinamicY)
                            platforms.append(blockDinamicY)
                        elif col == "R":
                            blockDinamicX = BlockRunX(x,y,20,20)
                            entities.add(blockDinamicX)
                            platforms.append(blockDinamicX)
                        elif col == "F":
                            b = BlockFake(x,y,levelcount,3)
                            entities.add(b)
                            countFake += 1
                            if(countFake >= 16):
                                b = BlockFake(x,y,levelcount,1)
                                entities.add(b)
                        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоковa
                    y += PLATFORM_HEIGHT    #то же самое и с высотой
                    x = 0  #на каждой новой строчке начинаем с нуля
                total_level_width  = len(level2[0])*PLATFORM_WIDTH#Высчитываем фактическую ширину
                total_level_height = len(level2)*PLATFORM_HEIGHT
                draw_Level = False
            elif levelcount == 4:
                bg.blit(level4BG,(0,0))
                entities = pygame.sprite.Group() # Все объекты
                platforms = [] # то, во что мы будем врезаться или опираться
                lians = []
                waters = []
                teleport = []
                ices = []
                entities.add(hero)
                countFake = 0

                x=y=0 # координаты
                for row in level4: # вся строка
                    for col in row: # каждый символ
                        if col == "-":
                            pf2 = Platform(x,y)
                            entities.add(pf2)
                            platforms.append(pf2)
                        elif col == "S" or col == "T":
                            column = BlockCol(x,y)
                            entities.add(column)
                            platforms.append(column)
                        elif col == "W":
                            w = BlockWater(x,y)
                            entities.add(w)
                            waters.append(w)
                        elif col == "M":
                            coin = BlockMonetka(x,y)
                            entities.add(coin)
                            coins.append(coin)
                        elif col == "l":
                            lian = BlockLiana(x,y)
                            entities.add(lian)
                            lians.append(lian)
                        elif col == "B":
                            mob = MobX(x,y,50,50,levelcount)
                            entities.add(mob)
                            platforms.append(mob)
                        ########
                        elif col == "C":
                            trapDinamic = TrapRunX(x,y,100,100)
                            entities.add(trapDinamic)
                            platforms.append(trapDinamic)
                        elif col == "L":
                            trapStatic = BlockTrapStatic(x,y)
                            entities.add(trapStatic)
                            platforms.append(trapStatic)
                        elif col == "U":
                            blockDinamicY = BlockRunY(x,y,400,100)
                            entities.add(blockDinamicY)
                            platforms.append(blockDinamicY)
                        elif col == "R":
                            blockDinamicX = BlockRunX(x,y,100,100)
                            entities.add(blockDinamicX)
                            platforms.append(blockDinamicX)
                        elif col == "F":
                            b = BlockFake(x,y,levelcount,1)
                            entities.add(b)
                            countFake += 1
                            # if(countFake >= 15):
                            #     b = BlockFake(x,y,levelcount,1)
                            #     entities.add(b)
                        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоковa
                    y += PLATFORM_HEIGHT    #то же самое и с высотой
                    x = 0  #на каждой новой строчке начинаем с нуля
                total_level_width  = len(level2[0])*PLATFORM_WIDTH#Высчитываем фактическую ширину
                total_level_height = len(level2)*PLATFORM_HEIGHT
                draw_Level = False

            elif levelcount == 5:
                bg.blit(level5BG,(0,0))
                entities = pygame.sprite.Group() # Все объекты
                platforms = [] # то, во что мы будем врезаsться или опираться
                lians = []
                waters = []
                ices = []
                teleport = []
                entities.add(hero)
                countFake = 0

                x=y=0 # координаты
                for row in level5: # вся строка
                    for col in row: # каждый символ
                        if col == "-":
                            pf2 = Platform(x,y)
                            entities.add(pf2)
                            platforms.append(pf2)
                        elif col == "W":
                            w = BlockWater(x,y)
                            entities.add(w)
                            waters.append(w)
                        elif col == "M":
                            coin = BlockMonetka(x,y)
                            entities.add(coin)
                            coins.append(coin)
                        elif col =="1":
                            snow = BlockFullSnow(x,y)
                            entities.add(snow)
                            platforms.append(snow)
                        elif col =="2":
                            sn = BlockSnow(x,y)
                            entities.add(sn)
                            platforms.append(sn) 
                        ########
                        elif col == "I":
                            ice = BlockIce(x,y)
                            entities.add(ice)
                            ices.append(ice)
                            platforms.append(ice)
                        elif col == "L":
                            trapStatic = BlockTrapStatic(x,y)
                            entities.add(trapStatic)
                            platforms.append(trapStatic)
                        elif col == "U":
                            blockDinamicY = BlockRunY(x,y,100,50)
                            entities.add(blockDinamicY)
                            platforms.append(blockDinamicY)
                        elif col == "R":
                            blockDinamicX = BlockRunX(x,y,100,270)
                            entities.add(blockDinamicX)
                            platforms.append(blockDinamicX)
                        elif col == "c":
                            trapDinamic1 = TrapRunY(x,y,50,50,levelcount)
                            entities.add(trapDinamic1)
                            platforms.append(trapDinamic1)
                        elif col == "C":
                            trapDinamic = TrapRunX(x,y,200,100)
                            entities.add(trapDinamic)
                            platforms.append(trapDinamic)
                        elif col == "o":
                            ogon = BlockFire(x,y)
                            entities.add(ogon)
                            platforms.append(ogon)
                        elif col == "/":
                            bdr = BlinkRunY(x,y,levelcount,1)
                            entities.add(bdr)
                            platforms.append(bdr)
                            countFake += 1
                            if(countFake <= 4):
                                bdr = BlinkRunY(x,y,levelcount,1)
                                entities.add(bdr)
                        elif col == "F":
                            b = BlockFake(x,y,levelcount,1)
                            entities.add(b)
                            # countFake += 1
                            # if(countFake >= 14):
                            #     b = BlockFake(x,y,levelcount,1)
                            #     entities.add(b)
                        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоковa
                    y += PLATFORM_HEIGHT    #то же самое и с высотой
                    x = 0  #на каждой новой строчке начинаем с нуля
                total_level_width  = len(level2[0])*PLATFORM_WIDTH#Высчитываем фактическую ширину
                total_level_height = len(level2)*PLATFORM_HEIGHT
                draw_Level = False
                
            elif levelcount == 6:
                bg.blit(level6BG,(0,0))
                entities = pygame.sprite.Group() # Все объекты
                entities.add(hero)
                platforms = [] # то, во что мы будем врезаsться или опираться
                lians = []
                waters = []
                ices = []
                teleport = []
                ogons = []
                x=y=0 # координаты
                for row in level6: # вся строка
                    for col in row: # каждый символ
                        if col == "-":
                            pf2 = Platform(x,y)
                            entities.add(pf2)
                            platforms.append(pf2)
                        elif col == "S":
                            stone = BlockStone(x,y)
                            entities.add(stone)
                            platforms.append(stone)
                        elif col == "R":
                            blockDinamicX = BlockRunX(x,y,500,500)
                            entities.add(blockDinamicX)
                            platforms.append(blockDinamicX)
                        elif col == "c":
                            trapDinamic1 = TrapRunY(x,y,400,100,levelcount)
                            entities.add(trapDinamic1)
                            platforms.append(trapDinamic1)
                        elif col == "C":
                            trapDinamic = TrapRunX(x,y,400,500)
                            entities.add(trapDinamic)
                            platforms.append(trapDinamic)
                        elif col == "B":
                            mob = MobX(x,y,50,50,levelcount)
                            entities.add(mob)
                            platforms.append(mob)
                        elif col == "U":
                            blockDinamicY = BlockRunY(x,y,20,200)
                            entities.add(blockDinamicY)
                            platforms.append(blockDinamicY)
                        elif col == "o":
                            ogon = BlockFire(x,y)
                            entities.add(ogon)
                            platforms.append(ogon)
                        elif col == "M":
                            coin = BlockMonetka(x,y)
                            entities.add(coin)
                            coins.append(coin)
                        elif col == "L":
                            trapStatic = BlockTrapStatic(x,y)
                            entities.add(trapStatic)
                            platforms.append(trapStatic)


                        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоковa
                    y += PLATFORM_HEIGHT    #то же самое и с высотой
                    x = 0  #на каждой новой строчке начинаем с нуля
                total_level_width  = len(level2[0])*PLATFORM_WIDTH#Высчитываем фактическую ширину
                total_level_height = len(level2)*PLATFORM_HEIGHT
                draw_Level = False

        #-------------------------end----------------------------
        hero.update(left,right,up,platforms,waters,coins,lians,levelcount,teleport,ices)
        camera = Camera(camera_configure, total_level_width, total_level_height)
        if levelcount == 1:
            if hero.rect.x >=270 and hero.rect.y >=680:
                blinkBool1 = True
            if hero.rect.x >=820 and hero.rect.y >=680:
                blinkBool2 = True
            countBlink = 0
            if blinkBool1 == True:
                for e in entities:
                    if isinstance(e, BlinkRunY) and countBlink < 7 :  # Проверяем, является ли объект экземпляром BlockRun
                        e.update()
                        countBlink += 1
            if blinkBool2 == True:
                for e in entities:
                    if isinstance(e, BlinkRunY):  # Проверяем, является ли объект экземпляром BlockRun
                        e.update()
        elif levelcount == 5:
            for e in entities:
                if isinstance(e, BlinkRunY):  # Проверяем, является ли объект экземпляром BlockRun
                    e.update()

        ##----------------------------fun-----------------------
        if levelcount == 1 and hero.rect.x > 1300 and hero.rect.y == 100:
            levelcount = 2
            draw_Level = True
            hero.rect.x = 100
            hero.rect.y = 100
            entities.empty()  # Очистка группы
            for entity in entities:
                entity.kill()  # Удаление объектов из памяти
        if levelcount == 2 and len(coins) == 0 and hero.rect.x > 2401:
            levelcount = 3
            draw_Level = True
            hero.rect.x = 100
            hero.rect.y = 100
            entities.empty()  # Очистка группы
            for entity in entities:
                entity.kill()  # Удаление объектов из памяти
                
        if levelcount == 3 and len(coins) == 0 and hero.rect.x > 2401:
            levelcount = 4
            draw_Level = True
            hero.rect.x = 50
            hero.rect.y = 150
            entities.empty()  # Очистка группы
            for entity in entities:
                entity.kill()  # Удаление объектов из памяти
        if levelcount == 4 and len(coins) == 0 and hero.rect.x > 2401:
            levelcount = 5
            draw_Level = True
            hero.rect.x = 50
            hero.rect.y = 150
            entities.empty()  # Очистка группы
            for entity in entities:
                entity.kill()  # Удаление объектов из памяти
        if levelcount == 5 and len(coins) == 0 and hero.rect.x > 2401:
            levelcount = 6
            draw_Level = True
            hero.rect.x = 50
            hero.rect.y = 150
            entities.empty()  # Очистка группы
            for entity in entities:
                entity.kill()  # Удаление объектов из памяти
        if levelcount == 6 and hero.rect.x > 2401:
            levelcount = 7
            entities.empty()  # Очистка группы
            for entity in entities:
                entity.kill()

    #---------------------end--------------------------------
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit; "QUIT"
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True

            if e.type == KEYUP and e.key == K_SPACE:
                up = False  # Установите up в False, когда клавиша пробела отпущена
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False

        screen.blit(bg, (0,0)) # Каждую итерацию необходимо всё перерисовывать
        camera.update(hero) # центризируем камеру относительно персонажа
        #entities.draw(screen) # отображение

        for e in entities:
            screen.blit(e.image, camera.apply(e))
            if isinstance(e, BlockRunY) or isinstance(e, BlockRunX) or isinstance(e, TrapRunY) or isinstance(e, TrapRunX) or isinstance(e,MobX) :  # Проверяем, является ли объект экземпляром BlockRun
                e.update()
        pygame.display.update()

if __name__ == "__main__":
    game_loop()
