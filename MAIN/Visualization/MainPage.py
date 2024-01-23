import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1500, 750  # Updated dimensions
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algorithm Visualizer")

# Set the background color
background_color = (5, 22, 26)

def animated_text_display(word):
    for i in range(len(word) + 1):  # +1 to include the entire word
        # Create a surface with the current portion of the word
        partial_word = word[:i]
        text_surface = font.render(partial_word, True, text_color)

        # Clear the screen with the background image
        screen.blit(background_image, (0, 0))

        # Calculate the position to center the text on the screen
        x = (width - text_surface.get_width()) // 2
        y = (height - text_surface.get_height()) // 20  # Adjusted to place it just below the top

        # Draw the text on the screen
        screen.blit(text_surface, (x, y))

        # Update the display
        pygame.display.flip()

        # Pause for a short duration
        pygame.time.delay(100)  # You can adjust the delay to control the speed

# Set up font for Welcome text
font_path = "sort-search-algorithm-visualizer/MAIN/Assets/fonts/static/RobotoMono-Bold.ttf"
font = pygame.font.Font(font_path, 75)  # Adjusted font size
text_color = (255, 255, 255)  # Set font color to black

# Load the background image
image_path = "sort-search-algorithm-visualizer/MAIN/Assets/comascii.jpg"
background_image = pygame.image.load(image_path)  # Replace with the actual image file path
background_image = pygame.transform.scale(background_image, (width, height))

# Display the background image
screen.blit(background_image, (0, 0))
pygame.display.flip()

# Your word to display
word_to_display = "Welcome To Algorithm Visualizer"

# Call the animated_text_display function with the word
animated_text_display(word_to_display)

# Set up font for message
message_font_path = "sort-search-algorithm-visualizer/MAIN/Assets/fonts/static/RobotoMono-Bold.ttf"
message_font = pygame.font.Font(message_font_path, 36)
message_color = (255, 255, 255)

# Your message to display below the image
message_text = "Explore the World of Algorithms On A Click!"
message_surface = message_font.render(message_text, True, message_color)

message_rect = message_surface.get_rect()
message_rect.center = (width // 2, height - 50)  # Adjusted to place it at the bottom

# Draw the message on the screen
screen.blit(message_surface, message_rect)
pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                screen = pygame.display.set_mode((1200,750))
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the click is on the image
            if pygame.Rect(0, 0, width, height).collidepoint(event.pos):
                import Menu

# Quit Pygame
pygame.quit()
sys.exit()
