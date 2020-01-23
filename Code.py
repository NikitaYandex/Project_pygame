import pygame
import os
import time
import sys
import random
from PIL import Image


all_sprites = pygame.sprite.Group()
Play1 = pygame.sprite.Group()
Play2 = pygame.sprite.Group()
Tornado1 = pygame.sprite.Group()
Tornado2 = pygame.sprite.Group()
Scene = pygame.sprite.Group()
pygame.init()
size = width, height = 950, 544
screen = pygame.display.set_mode(size)
screen.fill((255, 0, 255))
Supers = pygame.sprite.Group()
pl1 = 0
pl2 = 0
hero1 = input('''Введите 1 бойца:
Stallion
Soldier
Volcano
Vortex ''')
hero2 = input('''Введите 2 бойца:
Stallion
Soldier
Volcano
Vortex ''')
is_tornado1 = False
is_tornado2 = False


def load_image(hero1, name, colorkey=None):
    fullname = os.path.join('Data', hero1, name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_image2(hero2, name, colorkey=None):
    fullname = os.path.join('Data2', hero2, name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Scenes(pygame.sprite.Sprite):
    image = load_image('Scene', "Фон" + str(random.choice([1, 2, 3, 4, 5])) + ".jpg")

    def __init__(self, group):
        super().__init__(group)
        self.image = Scenes.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.c = 1

    def update(self, even):
        pass


class Ultimate1(pygame.sprite.Sprite):
    global hero1
    image = load_image(hero1, hero1 + "_super.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Ultimate1.image
        Supers.add(self)
        Play1.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if pygame.sprite.spritecollideany(self, Play2) is not None:
            if pygame.sprite.spritecollideany(self, Play2) == pl2:
                pl2.life = pl2.life - (40 * pl2.is_block)
            else:
                pygame.sprite.spritecollideany(self, Play2).kill()
            self.kill()
            self.rect = self.rect.move(10000, 0)
        else:
            if 950 > self.rect.x > 0:
                for i in range(10):
                    self.rect = self.rect.move(10, 0)
                    all_sprites.draw(screen)
                    pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                    if pl1.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                    if pl2.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                    pygame.display.flip()
                    if pygame.sprite.spritecollideany(self, Play2) is not None:
                        if pygame.sprite.spritecollideany(self, Play2) == pl2:
                            pl2.life = pl2.life - (40 * pl2.is_block)
                            self.rect = self.rect.move(10000, 0)
                            break
                        else:
                            pygame.sprite.spritecollideany(self, Play2).kill()
                        self.kill()
                        self.rect = self.rect.move(10000, 0)
                    time.sleep(0.05)
                if pygame.sprite.spritecollideany(self, Play2) is not None:
                    if pygame.sprite.spritecollideany(self, Play2) == pl2:
                        pl2.life = pl2.life - (40 * pl2.is_block)
                    else:
                        pygame.sprite.spritecollideany(self, Play2).kill()
                    self.kill()
                    self.rect = self.rect.move(10000, 0)
            else:
                self.kill()


class Ultimate2(pygame.sprite.Sprite):
    global hero2
    image = load_image2(hero2, hero2 + "_super.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Ultimate2.image
        Supers.add(self)
        Play2.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if pygame.sprite.spritecollideany(self, Play1) is not None:
            if pygame.sprite.spritecollideany(self, Play1) == pl1:
                pl1.life = pl1.life - (40 * pl1.is_block)
            else:
                pygame.sprite.spritecollideany(self, Play1).kill()
            self.kill()
            self.rect = self.rect.move(-10000, 0)
        else:
            if 950 > self.rect.x > 0:
                for i in range(10):
                    self.rect = self.rect.move(-10, 0)
                    all_sprites.draw(screen)
                    pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                    if pl1.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                    if pl2.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                    pygame.display.flip()
                    if pygame.sprite.spritecollideany(self, Play1) is not None:
                        if pygame.sprite.spritecollideany(self, Play1) == pl1:
                            pl1.life = pl1.life - (40 * pl1.is_block)
                            self.rect = self.rect.move(10000, 0)
                            break
                        else:
                            pygame.sprite.spritecollideany(self, Play1).kill()
                        self.kill()
                        self.rect = self.rect.move(-10000, 0)
                    time.sleep(0.05)
                if pygame.sprite.spritecollideany(self, Play1) is not None:
                    if pygame.sprite.spritecollideany(self, Play1) == pl1:
                        pl1.life = pl1.life - (40 * pl1.is_block)
                    self.kill()
                    self.rect = self.rect.move(-10000, 0)
            else:
                self.kill()


class Bullet1(pygame.sprite.Sprite):
    global hero2
    image = load_image2('Soldier', "bullet.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Bullet1.image
        Supers.add(self)
        Play1.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if pygame.sprite.spritecollideany(self, Play2) is not None:
            if pygame.sprite.spritecollideany(self, Play2) == pl2:
                pl2.life = pl2.life - (20 * pl2.is_block)
            else:
                pygame.sprite.spritecollideany(self, Play2).kill()
            self.kill()
            self.rect = self.rect.move(-10000, 0)
        else:
            if 950 > self.rect.x > 0:
                for i in range(10):
                    self.rect = self.rect.move(30, 0)
                    all_sprites.draw(screen)
                    pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                    if pl1.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                    if pl2.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                    pygame.display.flip()
                    if pygame.sprite.spritecollideany(self, Play2) is not None:
                        if pygame.sprite.spritecollideany(self, Play2) == pl2:
                            pl2.life = pl2.life - (10 * pl2.is_block)
                            self.rect = self.rect.move(10000, 0)
                            break
                        else:
                            pygame.sprite.spritecollideany(self, Play2).kill()
                        self.kill()
                        self.rect = self.rect.move(-10000, 0)
                    time.sleep(0.05)
                if pygame.sprite.spritecollideany(self, Play2) is not None:
                    if pygame.sprite.spritecollideany(self, Play2) == pl2:
                        pl2.life = pl2.life - (10 * pl2.is_block)
                    else:
                        pygame.sprite.spritecollideany(self, Play2).kill()
                    self.kill()
                    self.rect = self.rect.move(-10000, 0)
            else:
                self.kill()


class Bullet2(pygame.sprite.Sprite):
    global hero2
    image = load_image2('Soldier', "bullet.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Bullet2.image
        Supers.add(self)
        Play2.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if pygame.sprite.spritecollideany(self, Play1) is not None:
            if pygame.sprite.spritecollideany(self, Play1) == pl1:
                pl1.life = pl1.life - (20 * pl1.is_block)
            else:
                pygame.sprite.spritecollideany(self, Play1).kill()
            self.kill()
            self.rect = self.rect.move(-10000, 0)
        else:
            if 950 > self.rect.x > 0:
                for i in range(10):
                    self.rect = self.rect.move(-30, 0)
                    all_sprites.draw(screen)
                    pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                    if pl1.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                    if pl2.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                    pygame.display.flip()
                    if pygame.sprite.spritecollideany(self, Play1) is not None:
                        if pygame.sprite.spritecollideany(self, Play1) == pl1:
                            pl1.life = pl1.life - (10 * pl1.is_block)
                            self.rect = self.rect.move(10000, 0)
                            break
                        else:
                            pygame.sprite.spritecollideany(self, Play1).kill()
                        self.kill()
                        self.rect = self.rect.move(-10000, 0)
                    time.sleep(0.05)
                if pygame.sprite.spritecollideany(self, Play1) is not None:
                    if pygame.sprite.spritecollideany(self, Play1) == pl1:
                        pl1.life = pl1.life - (10 * pl1.is_block)
                    self.kill()
                    self.rect = self.rect.move(-10000, 0)
            else:
                self.kill()


class Ult_stallion(pygame.sprite.Sprite):
    image = load_image2('Stallion', "Stallion_super.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Ult_stallion.image
        Supers.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        for i in range(10):
            self.rect = self.rect.move(0, -20)
            all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(0.025)
        self.kill()


class tornado_1(pygame.sprite.Sprite):
    global is_tornado1
    image = load_image('Vortex', "Vortex_super.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = tornado_1.image
        Supers.add(self)
        Tornado1.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.schet = 0
        is_tornado1 = True

    def update(self):
        for i in all_sprites:
            if i != pl1:
                if i != sc:
                    if i != self:
                        if pl2 in pygame.sprite.spritecollide(self, Play2, False) and pl2 == i:
                            pl2.life = pl2.life - 10
                        elif i not in pygame.sprite.spritecollide(self, all_sprites, False):
                            for j in range(10):
                                if i.rect.x != self.rect.x:
                                    i.rect = i.rect.move(10 * ((self.rect.x - i.rect.x) // abs(self.rect.x - i.rect.x)),
                                                         0)
                                all_sprites.draw(screen)
                                pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                                pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                                pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                                pygame.draw.rect(screen, pygame.color.Color('red'),
                                                 (750 + pl2.life, 0, 200 - pl2.life, 30))
                                if pl1.c >= 3:
                                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                                else:
                                    pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                                if pl2.c >= 3:
                                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                                else:
                                    pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                                pygame.display.flip()
                                time.sleep(0.05)
        if self.schet < 20:
            if 950 > self.rect.x > 0:
                for i in range(10):
                    self.rect = self.rect.move(4, 0)
                    all_sprites.draw(screen)
                    pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                    if pl1.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                    if pl2.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                    pygame.display.flip()
                    time.sleep(0.05)
            self.schet += 1
        else:
            is_tornado1 = False
            self.kill()


class tornado_2(pygame.sprite.Sprite):
    global is_tornado2
    image = load_image2('Vortex', "Vortex_super.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = tornado_2.image
        Supers.add(self)
        Tornado2.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.schet = 0
        is_tornado2 = True

    def update(self):
        for i in all_sprites:
            if i != pl2:
                if i != sc:
                    if i != self:
                        if pl1 in pygame.sprite.spritecollide(self, Play1, False) and pl1 == i:
                            pl1.life = pl1.life - 10
                        elif i not in pygame.sprite.spritecollide(self, all_sprites, False):
                            for j in range(10):
                                if i.rect.x != self.rect.x:
                                    i.rect = i.rect.move(10 * ((self.rect.x - i.rect.x) // abs(self.rect.x - i.rect.x)),
                                                         0)
                                all_sprites.draw(screen)
                                pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                                pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                                pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                                pygame.draw.rect(screen, pygame.color.Color('red'),
                                                 (750 + pl2.life, 0, 200 - pl2.life, 30))
                                if pl1.c >= 3:
                                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                                else:
                                    pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                                if pl2.c >= 3:
                                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                                else:
                                    pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                                pygame.display.flip()
                                time.sleep(0.05)
        if self.schet < 20:
            if 950 > self.rect.x > 0:
                for i in range(10):
                    self.rect = self.rect.move(-4, 0)
                    all_sprites.draw(screen)
                    pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                    pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                    if pl1.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                    if pl2.c >= 3:
                        pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                    else:
                        pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                    pygame.display.flip()
                    time.sleep(0.05)
            self.schet += 1
        else:
            is_tornado2 = False
            self.kill()


class Player1(pygame.sprite.Sprite):
    global hero1
    image = load_image(hero1, hero1 + "_comfort.jpg")

    def __init__(self, group):
        super().__init__(group)
        self.image = Player1.image
        self.life = 200
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 400
        self.c = 1
        self.strange = 1
        self.is_block = 1

    def update(self, even):
        all_sprites.draw(screen)
        pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
        if pl1.c >= 3:
            pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
        else:
            pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
        if pl2.c >= 3:
            pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
        else:
            pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
        pygame.display.flip()
        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_LEFT:
                self.is_block = 1
                if self.rect.x - 20 >= 0:
                    self.image = load_image(hero1, hero1 + "_move.jpg")
                    for i in range(5):
                        self.rect = self.rect.move(-10, 0)
                        all_sprites.draw(screen)
                        pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                        if pl1.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                        if pl2.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                        pygame.display.flip()
                        time.sleep(0.05)
                    self.image = load_image(hero1, hero1 + "_comfort.jpg")
            elif even.key == pygame.K_RIGHT:
                self.is_block = 1
                if self.rect.x + 20 < 950:
                    self.image = load_image(hero1, hero1 + "_move.jpg")
                    for i in range(5):
                        self.rect = self.rect.move(10, 0)
                        all_sprites.draw(screen)
                        pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                        if pl1.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                        if pl2.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                        pygame.display.flip()
                        time.sleep(0.05)
                    self.image = load_image(hero1, hero1 + "_comfort.jpg")
            elif even.key == pygame.K_UP:
                self.is_block = 1
                self.image = load_image(hero1, hero1 + "_attack.jpg")
                all_sprites.draw(screen)
                pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                if pl1.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                if pl2.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                pygame.display.flip()
                if hero1 != 'Soldier':
                    if pygame.sprite.spritecollideany(self, Play2) is not None:
                        if pl2 != 0:
                            pl2.life = pl2.life - (10 * pl2.is_block * self.strange)
                            self.c += 1
                    if True:
                        time.sleep(0.35)
                else:
                    b = Bullet1(all_sprites, self.rect.x, self.rect.y)
                    self.c += 1
                    time.sleep(0.5)
                self.image = load_image(hero1, hero1 + "_comfort.jpg")
                self.strange = 1
            elif even.key == pygame.K_DOWN:
                self.is_block = 1
                if self.c >= 3:
                    if hero1 != 'Vortex':
                        if hero1 != 'Stallion':
                            if hero1 != 'Soldier':
                                self.image = load_image(hero1, hero1 + "_call.jpg")
                            else:
                                self.image = load_image(hero1, hero1 + "_attack.jpg")
                            a = Ultimate1(all_sprites, self.rect.x, self.rect.y)
                            all_sprites.draw(screen)
                            pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                            pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                            pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                            pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                            if pl1.c >= 3:
                                pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                            else:
                                pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                            if pl2.c >= 3:
                                pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                            else:
                                pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                            pygame.display.flip()
                            self.c = self.c - 3
                        else:
                            sil = Ult_stallion(all_sprites, self.rect.x, self.rect.y)
                            self.strange = self.strange * 4
                            self.c = self.c - 3
                    else:
                        torn = tornado_1(all_sprites, self.rect.x, self.rect.y)
                        self.c = self.c - 3
                time.sleep(0.45)
                self.image = load_image(hero1, hero1 + "_comfort.jpg")
            elif even.key == pygame.K_l:
                self.is_block = 0.25
                self.image = load_image(hero1, hero1 + "_block.jpg")
            else:
                if self.is_block != 0.25:
                    self.image = load_image(hero1, hero1 + "_comfort.jpg")
        if self.life <= 0:
            self.is_died = True
            if hero1 != 'Volcano':
                self.image = load_image(hero1, hero1 + "_died.jpg")
                all_sprites.draw(screen)
                pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                if pl1.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                if pl2.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                pygame.display.flip()
                time.sleep(2)
            print('Победа 2 игрока!!!')
            sys.exit(0)


class Player2(pygame.sprite.Sprite):
    global hero2
    image = load_image2(hero2, hero2 + "_comfort.jpg")

    def __init__(self, group):
        super().__init__(group)
        self.image = Player2.image
        self.life = 200
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 400
        self.c = 1
        self.strange = 1
        self.is_block = 1

    def update(self, even):
        all_sprites.draw(screen)
        pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
        if pl1.c >= 3:
            pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
        else:
            pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
        if pl2.c >= 3:
            pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
        else:
            pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
        pygame.display.flip()
        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_a:
                self.is_block = 1
                if self.rect.x - 20 >= 0:
                    self.image = load_image2(hero2, hero2 + "_move.jpg")
                    for i in range(5):
                        self.rect = self.rect.move(-10, 0)
                        all_sprites.draw(screen)
                        pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                        if pl1.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                        if pl2.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                        pygame.display.flip()
                        time.sleep(0.05)
                self.image = load_image2(hero2, hero2 + "_comfort.jpg")
            elif even.key == pygame.K_d:
                self.is_block = 1
                if self.rect.x + 20 < 950:
                    self.image = load_image2(hero2, hero2 + "_move.jpg")
                    for i in range(5):
                        self.rect = self.rect.move(10, 0)
                        all_sprites.draw(screen)
                        pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                        pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                        if pl1.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                        if pl2.c >= 3:
                            pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                        else:
                            pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                        pygame.display.flip()
                        time.sleep(0.05)
                self.image = load_image2(hero2, hero2 + "_comfort.jpg")
            elif even.key == pygame.K_e:
                self.is_block = 1
                self.image = load_image2(hero2, hero2 + "_attack.jpg")
                all_sprites.draw(screen)
                pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                if pl1.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                if pl2.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                pygame.display.flip()
                if hero2 != 'Soldier':
                    if pygame.sprite.spritecollideany(self, Play1) is not None:
                        if pl1 != 0 and pygame.sprite.spritecollideany(self, Play1) == pl1:
                            pl1.life = pl1.life - (10 * pl1.is_block * self.strange)
                            self.c += 1
                    time.sleep(0.35)
                    self.strange = 1
                else:
                    b = Bullet2(all_sprites, self.rect.x, self.rect.y)
                    self.c += 1
                    time.sleep(0.5)
                self.image = load_image2(hero2, hero2 + "_comfort.jpg")
            elif even.key == pygame.K_s:
                self.is_block = 1
                if self.c >= 3:
                    if hero2 != 'Vortex':
                        if hero2 != 'Stallion':
                            if hero2 != 'Soldier':
                                self.image = load_image2(hero2, hero2 + "_call.jpg")
                            else:
                                self.image = load_image2(hero2, hero2 + "_attack.jpg")
                            a = Ultimate2(all_sprites, self.rect.x, self.rect.y)
                            self.c = self.c - 3
                        else:
                            sil = Ult_stallion(all_sprites, self.rect.x, self.rect.y)
                            self.strange = self.strange * 4
                            self.c = self.c - 3
                    else:
                        torn = tornado_2(all_sprites, self.rect.x, self.rect.y)
                        self.c = self.c - 3
            elif even.key == pygame.K_q:
                self.image = load_image2(hero2, hero2 + "_block.jpg")
                self.is_block = 0.25
            else:
                if self.is_block == 1:
                    self.image = load_image2(hero2, hero2 + "_comfort.jpg")
        if self.life <= 0:
            self.is_died = True
            if hero2 != 'Volcano':
                self.image = load_image2(hero2, hero2 + "_died.jpg")
                all_sprites.draw(screen)
                pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
                pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
                if pl1.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
                if pl2.c >= 3:
                    pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
                pygame.display.flip()
            time.sleep(2)
            print('Победа 1 игрока!!!')
            sys.exit(0)


all_sprites.draw(screen)
running = True
sc = Scenes(all_sprites)
pl1 = Player1(all_sprites)
pl2 = Player2(all_sprites)
Play1.add(pl1)
Play2.add(pl2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pl1.update(event)
        pl2.update(event)
        pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
        pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
    Supers.update()
    all_sprites.draw(screen)
    pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
    pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
    pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
    pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
    if pl1.c >= 3:
        pygame.draw.rect(screen, pygame.color.Color('yellow'), (200, 0, 30, 30))
    else:
        pygame.draw.rect(screen, pygame.color.Color('grey'), (200, 0, 30, 30))
    if pl2.c >= 3:
        pygame.draw.rect(screen, pygame.color.Color('yellow'), (720, 0, 30, 30))
    else:
        pygame.draw.rect(screen, pygame.color.Color('grey'), (720, 0, 30, 30))
    pygame.display.flip()
    screen.fill((255, 255, 255))
    if pl1.life <= 0:
        if hero1 != 'Volcano':
            pl1.image = load_image(hero1, hero1 + "_died.jpg")
            all_sprites.draw(screen)
            pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
            pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
            pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
            pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
            pygame.display.flip()
            time.sleep(2)
        print('Победа 2 игрока!!!')
        sys.exit(0)
    if pl2.life <= 0:
        if hero2 != 'Volcano':
            pl2.image = load_image2(hero2, hero2 + "_died.jpg")
            all_sprites.draw(screen)
            pygame.draw.rect(screen, pygame.color.Color('green'), (0, 0, pl1.life, 30))
            pygame.draw.rect(screen, pygame.color.Color('red'), (pl1.life, 0, 200 - pl1.life, 30))
            pygame.draw.rect(screen, pygame.color.Color('green'), (750, 0, pl2.life, 30))
            pygame.draw.rect(screen, pygame.color.Color('red'), (750 + pl2.life, 0, 200 - pl2.life, 30))
            pygame.display.flip()
            time.sleep(2)
        print('Победа 1 игрока!!!')
        sys.exit(0)
