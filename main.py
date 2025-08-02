import pygame
import asyncio
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Higher or Lower")
FPS = 60

INSTRUCTIONS_FONT = pygame.font.Font(None, 75)
TITLE_FONT = pygame.font.Font(None, 100)
ANSWER_FONT = pygame.font.Font(None, 135)

BLUE = (55, 100, 240)
WHITE = (255, 255, 255)
BLACK = (50, 50, 50)
GREEN = (28, 232, 35)

# Game state variables
game_state = "start"
input_text = ""
active = False
number = random.randint(1, 100)
result_text = ""
result_color = WHITE

input_rect = pygame.Rect(300, 450, 400, 125)
color_active = pygame.Color('BLACK')
color_passive = pygame.Color('WHITE')
color = color_passive

def draw_start_screen():
    WIN.fill(BLUE)
    lines = [
        "The Computer has chosen a",
        "random number between 1 and 100",
        "You guess a number, and",
        "the Computer will tell you if",
        "your guess is higher or lower",
        "than the actual number.",
        "Press anywhere to start"
    ]
    for i, line in enumerate(lines):
        text = INSTRUCTIONS_FONT.render(line, True, WHITE)
        WIN.blit(text, (WIDTH//2 - text.get_width()//2, 50 + i*75))

def draw_guess_screen():
    WIN.fill(BLUE)
    title1 = TITLE_FONT.render("Pick a number between", True, WHITE)
    title2 = TITLE_FONT.render("1 and 100:", True, WHITE)
    WIN.blit(title1, (WIDTH//2 - title1.get_width()//2, 75))
    WIN.blit(title2, (WIDTH//2 - title2.get_width()//2, 175))

    pygame.draw.rect(WIN, BLUE, input_rect)
    pygame.draw.rect(WIN, color, input_rect, 2)

    text_surface = TITLE_FONT.render(input_text, True, WHITE)
    WIN.blit(text_surface, (input_rect.x + 145, input_rect.y + 25))

def draw_result_screen():
    WIN.fill(BLUE)
    text = ANSWER_FONT.render(result_text, True, result_color)
    WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

def draw_correct_screen():
    WIN.fill(BLUE)
    text = ANSWER_FONT.render("Correct!", True, GREEN)
    WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

async def main():
    global game_state, input_text, active, color, result_text, result_color, number

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if game_state == "start":
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    game_state = "guess"

            elif game_state == "guess":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                    color = color_active if active else color_passive

                if event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            guess = int(input_text.strip())
                            if 1 <= guess <= 100:
                                if guess == number:
                                    game_state = "correct"
                                elif guess > number:
                                    result_text = "Lower"
                                    result_color = WHITE
                                    game_state = "result"
                                else:
                                    result_text = "Higher"
                                    result_color = WHITE
                                    game_state = "result"
                            input_text = ""
                        except ValueError:
                            input_text = ""
                    else:
                        if event.unicode.isdigit() and len(input_text) < 3:
                            input_text += event.unicode

            elif game_state == "result":
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    game_state = "guess"

            elif game_state == "correct":
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    # Restart game
                    input_text = ""
                    number = random.randint(1, 100)
                    game_state = "start"

        # Draw current state
        if game_state == "start":
            draw_start_screen()
        elif game_state == "guess":
            draw_guess_screen()
        elif game_state == "result":
            draw_result_screen()
        elif game_state == "correct":
            draw_correct_screen()

        pygame.display.flip()
        await asyncio.sleep(0)

# For pygbag compatibility
if __name__ == "__main__":
    asyncio.run(main())