import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SNAKE_SIZE = 10
FPS = 12
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize screen
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gowd's Snake Game")

# Snake and food
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]

food_x, food_y = random.randrange(0, WIDTH, SNAKE_SIZE), random.randrange(0, HEIGHT, SNAKE_SIZE)

# Clock and score
clock = pygame.time.Clock()
score = 0

# Functions
def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y, score

    # Update snake position
    snake_x = (snake_x + change_x) % WIDTH
    snake_y = (snake_y + change_y) % HEIGHT

    # Check self-collision
    if (snake_x, snake_y) in snake_body[1:]:
        game_over()

    # Add new position to snake
    snake_body.append((snake_x, snake_y))

    # Check if snake eats food
    if (food_x, food_y) == (snake_x, snake_y):
        score += 1
        # Ensure food does not spawn on the snake
        while (food_x, food_y) in snake_body:
            food_x, food_y = random.randrange(0, WIDTH, SNAKE_SIZE), random.randrange(0, HEIGHT, SNAKE_SIZE)
    else:
        # Remove the tail if no food eaten
        del snake_body[0]

    # Draw everything
    game_screen.fill(BLACK)
    pygame.draw.rect(game_screen, GREEN, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])
    for x, y in snake_body:
        pygame.draw.rect(game_screen, WHITE, [x, y, SNAKE_SIZE, SNAKE_SIZE])

    # Display score
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    game_screen.blit(score_text, (10, 10))

    pygame.display.update()

def game_over():
    font = pygame.font.SysFont(None, 55)
    game_over_text = font.render("Game Over!", True, WHITE)
    game_screen.fill(BLACK)
    game_screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x != SNAKE_SIZE:
                change_x, change_y = -SNAKE_SIZE, 0
            elif event.key == pygame.K_RIGHT and change_x != -SNAKE_SIZE:
                change_x, change_y = SNAKE_SIZE, 0
            elif event.key == pygame.K_UP and change_y != SNAKE_SIZE:
                change_x, change_y = 0, -SNAKE_SIZE
            elif event.key == pygame.K_DOWN and change_y != -SNAKE_SIZE:
                change_x, change_y = 0, SNAKE_SIZE

    display_snake_and_food()
    clock.tick(FPS)
