import pygame
from i3ipc import Connection

pygame.init()

pygame.display.set_caption('gear bar')

white = (255, 255, 255)

# offscreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen_w = offscreen.get_width()
# screen_h = offscreen.get_height()

# bar_height = int(screen_h / .8)

screen_w = 1920
screen_h = 200

screen = pygame.display.set_mode((screen_w, screen_h))

font_size = 24
font = pygame.font.Font(pygame.font.get_default_font(), font_size)

button_spacing = int(font_size * 4)

current_gear = 0


def draw_hud():
    text_surface = font.render('Gear', True, white)
    screen.blit(text_surface,
                dest=(int(font_size / 2), int(font_size / 2))
                )

    line_start_y = font_size
    line_start_x = int(screen_h / 2)
    line_end_x = int(screen_h / 2)
    line_end_y = screen_w - font_size

    pygame.draw.line(screen, white,
                     (line_start_y, line_start_x),
                     (line_end_y, line_end_x),
                     5
                     )

    bottom_bar_y_axis = screen_h - int(screen_h / 4) - int(font_size / 2)

    gear_text = font.render(str(current_gear), True, white)
    screen.blit(gear_text, dest=(font_size, bottom_bar_y_axis))

    plus_text = font.render("+", True, white)
    neutral_text = font.render("N", True, white)
    minus_text = font.render("-", True, white)

    plus_text_loc = plus_text.get_rect(center=(int(screen_w / 2), bottom_bar_y_axis + int(font_size / 2)))
    screen.blit(plus_text, plus_text_loc)
    plus_rect_loc = plus_text_loc.inflate(int(font_size * 2), int(font_size * .5))
    pygame.draw.rect(screen, white, plus_rect_loc, 5)

    neutral_text_loc = neutral_text.get_rect(center=(
        int(screen_w / 2) + button_spacing,
        bottom_bar_y_axis + int(font_size / 2)
    ))
    screen.blit(neutral_text, neutral_text_loc)
    neutral_rect_loc = neutral_text_loc.inflate(int(font_size * 2), int(font_size * .5))
    pygame.draw.rect(screen, white, neutral_rect_loc, 5)

    minus_text_loc = minus_text.get_rect(center=(
        int(screen_w / 2) + button_spacing*2,
        bottom_bar_y_axis + int(font_size / 2)
    ))
    screen.blit(minus_text, minus_text_loc)
    minus_rect_loc = minus_text_loc.inflate(int(font_size * 2), int(font_size * .5))
    pygame.draw.rect(screen, white, minus_rect_loc, 5)


def i3_setup():
    i3 = Connection()
    i3.command("workspace bar")
    i3.command("split v")
    i3.command("exec google-chrome-stable")
    i3.command("focus name 'gear bar'")
    i3.command("border none")
    i3.command("resize shrink width 30 px or 30 ppt")


if __name__ == "__main__":
    draw_hud()
    i3_setup()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            pygame.display.update()
