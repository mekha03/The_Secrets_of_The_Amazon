import pygame
from support import import_csv_layout, import_cut_graphic
from tiles import Tile, StaticTile, Coins
from settings import tile_size, screen_width
from player import Player


class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.world_shift = -2

        # terrain setup
        Platform_layout = import_csv_layout(level_data['Platform'])
        self.Platform_sprites = self.create_tile_group(Platform_layout, 'Platform')

        # plants setup
        Plants_layout = import_csv_layout(level_data['Plants'])
        self.Plants_sprites = self.create_tile_group(Plants_layout, 'Plants')

        # coins
        Coins_layout = import_csv_layout(level_data['Coins'])
        self.Coins_sprites = self.create_tile_group(Coins_layout, 'Coins')


    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'Platform':
                        Platform_tile_list = import_cut_graphic('../graphics/Misc/p27_0-removebg-preview.png')
                        tile_surface = Platform_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'Plants':
                        Plants_tile_list = import_cut_graphic('../graphics/Misc/p27_1-removebg-preview.png')
                        tile_surface = Plants_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'Coins':
                        if int(val) == 0:
                            path = '../graphics/Misc/coin/gold'
                        else:
                            path = '../graphics/Misc/coin/silver'
                        sprite = Coins(tile_size, x, y, path)


                    sprite_group.add(sprite)
        return sprite_group

    def run(self):
        # platform
        self.Platform_sprites.update(self.world_shift)
        self.Platform_sprites.draw(self.display_surface)

        # plants
        self.Plants_sprites.draw(self.display_surface)
        self.Plants_sprites.update(self.world_shift)

        # coins
        self.Coins_sprites.update(self.world_shift)
        self.Coins_sprites.draw(self.display_surface)

