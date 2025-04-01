import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
RED = (200, 0, 0)
BLUE = (0, 71, 119)

# Font
font = pygame.font.Font(None, 36)

# Game variables
secret_number = random.randint(1, 100)
input_text = ""
message = "Guess a number (1-100)"
running = True
attempts = 0

while running:
    screen.fill(BLUE)

    # Display instructions and feedback
    text_surface = font.render(message, True, WHITE)
    screen.blit(text_surface, (50, 50))

    # Display input box
    pygame.draw.rect(screen, WHITE, (50, 100, 400, 40), 1)
    input_surface = font.render(input_text, True, WHITE)
    screen.blit(input_surface, (60, 110))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Check guess on Enter
                try:
                    attempts += 1
                    guess = int(input_text)
                    if guess < secret_number:
                        message = "Too low! Try again."
                    elif guess > secret_number:
                        message = "Too high! Try again."
                    else:
                        message = f"Congratulations! in {attempts} attempts."
                except ValueError:
                    message = "Enter a valid number!"
                input_text = ""  # Reset input field
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]  # Remove last character
            else:
                input_text += event.unicode  # Add typed character

pygame.quit()
