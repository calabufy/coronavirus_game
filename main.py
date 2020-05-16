import arcade
import random
import time
import typing
from Virus import *


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Победи коронавирус!'
fields_number = 4
VIRUS_SPEED = -1
score = 0





class Game(arcade.Window):
    def __init__(self, width, height):
        super(Game, self).__init__(width, height, SCREEN_TITLE)
        self.background = None
        self.music = arcade.Sound(f'data//sound//bg_music.mp3')
        self.sound_kill_virus = arcade.Sound('data//sound//kill_virus.wav')

    def setup(self):
        self.virus_list = arcade.SpriteList()
        self.background = arcade.load_texture("data//img//bg.png")
        self.music.play(0.1)

        self.view_left = 0
        self.view_bottom = 0

    def on_mouse_press(self, x, y, virus, key_modifiers):
        global score
        hit_sprites = arcade.get_sprites_at_point((x, y), self.virus_list)
        for sprite in hit_sprites:
            virus_sprite = typing.cast(Virus, sprite)
            if virus == arcade.MOUSE_BUTTON_LEFT:
                virus_sprite.remove_from_sprite_lists()
                self.sound_kill_virus.play(0.3)
                score += 1

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        for x in range(SCREEN_WIDTH // fields_number, SCREEN_WIDTH, SCREEN_WIDTH // fields_number):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, arcade.color.BLACK, 4)
        self.virus_list.draw()
        arcade.draw_text(str(score), self.view_left + 10, self.view_bottom + SCREEN_HEIGHT - 30, arcade.csscolor.BLACK, 20)

    def on_update(self, delta_time):
        global score, VIRUS_SPEED, kill_virus
        if random.randrange(50) == 0:
            virus = Virus(random.choice(range(fields_number)))
            virus.center_x = virus.way * SCREEN_WIDTH // fields_number + 50
            virus.center_y = SCREEN_HEIGHT + 50
            virus.change_y = VIRUS_SPEED - (score / 10)
            self.virus_list.append(virus)
        for virus in self.virus_list:
            if virus.center_y == 0:
                virus.remove_from_sprite_lists()
        self.virus_list.update()

        position = self.music.get_stream_position()
        if position == 0.0:
            self.music.play(0.1)


def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()
