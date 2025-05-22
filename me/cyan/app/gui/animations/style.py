import time

def MainColor(menu1
):
    start_color = (0, 200, 150)  # Starting color (RGB)
    end_color = (0, 255, 255)  # Ending color (RGB)
    num_steps = 15  # Number of gradient steps

    # Generating a list of colors transitioning from start to end
    colors = []
    for i in range(num_steps
):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))

    colors += list(reversed(colors[:-1]))  # Mirroring the gradient for a smooth effect

    gradient_chars = '┌─┬│└┐┘┴├┤▓▒░█▄▌▀┃━┣━└$━┛┗'  # Characters to apply gradient
    num_colors = len(colors)

    def text_color(r, g, b
):
        return f"\033[38;2;{r};{g};{b}m"  # ANSI escape sequence for RGB colors

    lines = menu1.split('\n')
    result = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            color = colors[color_index]

            if char in gradient_chars:
                result.append(text_color(*color) + char + "\033[0m")  # Apply gradient
            else:
                result.append(char)

        if i < len(lines) - 1:
            result.append('\n')

    return ''.join(result)

# Function to print text slowly with a delay between each line (creates animation effect)
def Slow(text
):
    delai = 0.03  # Delay time (30ms between lines)
    lignes = text.split('\n')  # Split input text into lines
    for ligne in lignes:
        print(ligne)  # Print each line
        time.sleep(delai)  # Pause between prints for the animation effect