import pygame
import random

GRID_SIZE = 32  
GRID_WIDTH = 20  
GRID_HEIGHT = 16 
SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH  
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT  

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_position = (0, 0)  
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()
        running = True

        def draw_grid():
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, (200, 200, 200), (0, y), (SCREEN_WIDTH, y))

        def move_mole_randomly():
            x = random.randrange(0, GRID_WIDTH) * GRID_SIZE
            y = random.randrange(0, GRID_HEIGHT) * GRID_SIZE
            return (x, y)

        # Main game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_x, mole_y = mole_position
                    if mole_x <= mouse_x < mole_x + GRID_SIZE and mole_y <= mouse_y < mole_y + GRID_SIZE:
                        mole_position = move_mole_randomly()  # Move the mole to a new random position

            # Clear the screen and draw the grid
            screen.fill("light green")
            draw_grid()

            # Draw the mole at its current position
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))

            # Update the display and control the frame rate
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

# Run the game
if __name__ == "__main__":
    main()