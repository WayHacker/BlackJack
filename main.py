import pygame
import sys
import random
import time


pygame.init()
pygame.display.set_caption('Deadly blackjack')
screen = pygame.display.set_mode((1600, 900))
bg = pygame.image.load("sprites/table1600900.png")
screen.blit(bg,(0,0))
font_score = pygame.font.SysFont('dejavusansmono', 20)
clock = pygame.time.Clock()
player_turn_plashka = pygame.image.load("sprites/panel_button.png")


def shuffle_deck(deck):
    random.shuffle(deck)

bot_hand = pygame.sprite.Group()
player_hand = pygame.sprite.Group()
init_new_card = False
deck = ['1','2','3','4','5','6','7','8','9','10','11']
shuffle_deck(deck)
back_card_sprite = pygame.image.load("sprites/card_back.png")
white = (255,255,255)

def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))


class Card(pygame.sprite.Sprite):
    def __init__ (self, x, y, card_rating, card_pos, secret):
        pygame.sprite.Sprite.__init__(self)
        self.secret = secret    
        self.card_rating = card_rating
        if secret == 1:
            self.image = back_card_sprite
        else:
            self.image = pygame.image.load("sprites/card"+ card_rating +".png")
        
        self.card_pos = card_pos * 200
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 200
    def update(self):
        if(self.rect.x >= self.card_pos):
            self.rect.x -= 20


first_card = Card(2000,600, deck.pop(), len(player_hand)+1, 1)
player_hand.add(first_card)
bot_first_card = Card(2000,100, deck.pop(), len(bot_hand)+1, 1)
bot_hand.add(bot_first_card)
second_card = Card(2300,600, deck.pop(), len(player_hand)+1, 0)
player_hand.add(second_card)  
bot_second_card = Card(2300,100, deck.pop(), len(bot_hand)+1, 0)
bot_hand.add(bot_second_card)
bot_score = int(bot_first_card.card_rating) + int (bot_second_card.card_rating)
player_score = int(first_card.card_rating) + int(second_card.card_rating)
player_turn = True


while (True):
    screen.blit(bg,(0,0))
    player_hand.update()
    player_hand.draw(screen)
    bot_hand.update()
    bot_hand.draw(screen)
    draw_text('score:' + str(player_score),font_score, white, 50,500)
    # if player_turn == True:
    #     screen.blit(player_turn_plashka, (400,700))

    if init_new_card == True:
        print(len(player_hand))
        new_card = Card(2000,600, deck.pop(),len(player_hand)+1, 0 )
        player_score += int(new_card.card_rating)
        player_hand.add(new_card)
        init_new_card = False
        print(new_card.card_pos)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and player_turn == True:
            if event.key == pygame.K_SPACE:

                if (len(deck)>=1):        
                    init_new_card = True
                    player_turn = False
                else:
                    print("deck is empty!")   
            if event.key == pygame.K_x and player_turn == True:
                print("Player skip!")
                player_turn = False
        
            


    if player_turn == False and len(deck) >= 1:
        #bot choose logic...
        new_card = Card(2300,100, deck.pop(),len(bot_hand)+1, 0 )
        bot_score += int(new_card.card_rating)
        bot_hand.add(new_card)
        print(new_card.card_pos)
        player_turn = True
    elif len(deck) <= 1:
        print("deck is empty!")
    clock.tick(60)
    pygame.display.update()
    