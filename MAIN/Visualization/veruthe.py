import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Text Display")

# Set up font
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

def animated_text_display(word):
    for i in range(len(word) + 1):  # +1 to include the entire word
        # Create a surface with the current portion of the word
        partial_word = word[:i]
        text_surface = font.render(partial_word, True, text_color)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Calculate the position to center the text on the screen
        x = (width - text_surface.get_width()) // 2
        y = (height - text_surface.get_height()) // 2

        # Draw the text on the screen
        screen.blit(text_surface, (x, y))

        # Update the display
        pygame.display.flip()

        # Pause for a short duration
        pygame.time.delay(100)  # You can adjust the delay to control the speed

# Your word to display
word_to_display = "Hello"

# Call the animated_text_display function with the word
animated_text_display(word_to_display)

# Main loop
running = True
while running:
    screen.fill((5, 22, 26))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
sys.exit()
