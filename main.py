import pygame
import asyncio
import random
import sys

pygame.font.init()

WIDTH,HEIGHT = 1000,650
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Higher or Lower")

FPS = 60

draw_start = True

INSTRUCTIONS_FONT = pygame.font.Font(None, 75)
TITLE_FONT = pygame.font.Font(None, 100)
ANSWER_FONT = pygame.font.Font(None, 135)

BLUE = (55, 100, 240)
WHITE = (255, 255, 255)
BLACK = (50, 50, 50)
GREEN = (28, 232, 35)

def draw_window(number):
    WIN.fill(BLUE)
    TITLE_1 = TITLE_FONT.render("Pick a number between", 1, WHITE)
    TITLE_2 = TITLE_FONT.render("1 and 100:", 1, WHITE)
    WIN.blit(TITLE_1, (WIDTH//2 - TITLE_1.get_width()//2, 75))
    WIN.blit(TITLE_2, (WIDTH//2 - TITLE_2.get_width()//2, 175))

    input_rect = pygame.Rect(300, 450, 400, 125)
    pygame.draw.rect(WIN, WHITE, input_rect, 2)
    pygame.display.flip()

    color_active = pygame.Color('BLACK')
    color_passive = pygame.Color('WHITE')
    color = color_passive

    active = False
    input_text = ''
    print("hi")

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if active:
                color = color_active
            else:
                color = color_passive
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN and len(input_text) > 0:
                    if int(input_text) <= 100:
                        run = False
                    else:
                        input_text = ""
                else:
                    try:
                        int(event.unicode)
                        if len(input_text) < 3:
                            input_text += event.unicode
                    except ValueError:
                        pass
                
            pygame.draw.rect(WIN, BLUE, input_rect)
            pygame.draw.rect(WIN, color, input_rect, 2)

            text_surface = TITLE_FONT.render(input_text, True, (255, 255, 255))

            WIN.blit(text_surface, (input_rect.x+145, input_rect.y+25))
            pygame.display.flip()

    print(input_text)

    if int(input_text) == number:
        correct_function()
    elif int(input_text) > number:
        ANSWER_TEXT = ANSWER_FONT.render("Lower", 1, WHITE)
    else:
        ANSWER_TEXT = ANSWER_FONT.render("Higher", 1, WHITE)


    WIN.blit(ANSWER_TEXT, (WIDTH//2 - ANSWER_TEXT.get_width()//2,
            HEIGHT//1.925 - ANSWER_TEXT.get_height()//2))
    pygame.display.update()
    pygame.time.delay(2000)

def correct_function():
    CORRECT_TEXT = ANSWER_FONT.render("Correct!", 1, GREEN)
    WIN.blit(CORRECT_TEXT, (WIDTH//2 - CORRECT_TEXT.get_width()//2,
        HEIGHT//1.925 - CORRECT_TEXT.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3500)
    sys.exit()

def start_text():
    WIN.fill(BLUE)
    INSTRUCTIONS_1 = INSTRUCTIONS_FONT.render("The Computer has chosen a", 1, WHITE)
    INSTRUCTIONS_2 = INSTRUCTIONS_FONT.render("random number between 1 and 100", 1, WHITE)
    INSTRUCTIONS_3 = INSTRUCTIONS_FONT.render("You guess a number, and", 1, WHITE)
    INSTRUCTIONS_4 = INSTRUCTIONS_FONT.render("the Computer will tell you if", 1, WHITE)
    INSTRUCTIONS_5 = INSTRUCTIONS_FONT.render("your guess is higher or lower", 1, WHITE)
    INSTRUCTIONS_6 = INSTRUCTIONS_FONT.render("than the actual number.", 1, WHITE)
    INSTRUCTIONS_7 = INSTRUCTIONS_FONT.render("Press anywhere to start", 1, WHITE)

    WIN.blit(INSTRUCTIONS_1, (WIDTH//2 - INSTRUCTIONS_1.get_width()//2,
                    HEIGHT-575 - INSTRUCTIONS_1.get_height()//2))
    WIN.blit(INSTRUCTIONS_2, (WIDTH//2 - INSTRUCTIONS_2.get_width()//2,
                    HEIGHT-495 - INSTRUCTIONS_2.get_height()//2))
    WIN.blit(INSTRUCTIONS_3, (WIDTH//2 - INSTRUCTIONS_3.get_width()//2,
                    HEIGHT-415 - INSTRUCTIONS_3.get_height()//2))
    WIN.blit(INSTRUCTIONS_4, (WIDTH//2 - INSTRUCTIONS_4.get_width()//2,
                    HEIGHT-335 - INSTRUCTIONS_4.get_height()//2))
    WIN.blit(INSTRUCTIONS_5, (WIDTH//2 - INSTRUCTIONS_5.get_width()//2,
                    HEIGHT-255 - INSTRUCTIONS_5.get_height()//2))
    WIN.blit(INSTRUCTIONS_6, (WIDTH//2 - INSTRUCTIONS_6.get_width()//2,
                    HEIGHT-175 - INSTRUCTIONS_6.get_height()//2))
    WIN.blit(INSTRUCTIONS_7, (WIDTH//2 - INSTRUCTIONS_7.get_width()//2,
                    HEIGHT-75 - INSTRUCTIONS_7.get_height()//2))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                

async def main():
    START = True
    number = random.randint(1, 100)
    print(number)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if START == True:
            START = False
            start_text()

        draw_window(number)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
