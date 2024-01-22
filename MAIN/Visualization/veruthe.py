import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Text Display")

# Set the background color
background_color = (5, 22, 26)

def animated_text_display(word):
    for i in range(len(word) + 1):  # +1 to include the entire word
        # Create a surface with the current portion of the word
        partial_word = word[:i]
        text_surface = font.render(partial_word, True, text_color)

        # Clear the screen with the background color
        screen.fill(background_color)

        # Calculate the position to center the text on the screen
        x = (width - text_surface.get_width()) // 2
        y = (height - text_surface.get_height()) // 6  # Adjusted to place it a bit above the top

        # Draw the text on the screen
        screen.blit(text_surface, (x, y))

        # Update the display
        pygame.display.flip()

        # Pause for a short duration
        pygame.time.delay(100)  # You can adjust the delay to control the speed

# Your word to display
word_to_display = "Welcome"

# Set up font
font = pygame.font.Font(None, 83)  # Adjusted font size
text_color = (255, 255, 255)

# Call the animated_text_display function with the word
animated_text_display(word_to_display)

# Load the image
image = pygame.image.load("C:\\Users\\Hari\\Documents\\sort-search-algorithm-visualizer\\MAIN\\Visualization\\4lr0bzo89ti51.jpg")  # Replace with the actual image file path
image_rect = image.get_rect()
image_rect.center = (width // 2, height // 2)  # Center the image on the screen

# Display the image
screen.blit(image, image_rect)
pygame.display.flip()

# Show the message below the image
message_font = pygame.font.Font(None, 36)
message_color = (255, 255, 255)
message_text = "Click on the image to continue"
message_surface = message_font.render(message_text, True, message_color)

message_rect = message_surface.get_rect()
message_rect.center = (width // 2, height - 50)  # Adjusted to place it at the bottom

# Draw the message on the screen
screen.blit(message_surface, message_rect)
pygame.display.flip()

# Main loop
waiting_for_click = True
while waiting_for_click:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting_for_click = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the click is on the image
            if image_rect.collidepoint(event.pos):
                waiting_for_click = False

# Quit Pygame
pygame.quit()
sys.exit()
