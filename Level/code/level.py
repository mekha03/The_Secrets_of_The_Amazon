import pygame
from support import import_csv_layout, import_cut_graphic
from tiles import Tile, StaticTile, Coins
from settings import tile_size, screen_width
from Enemy import Enemy
from player import Player


class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.world_shift = -2

        # player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # terrain setup
        Platform_layout = import_csv_layout(level_data['Platform'])
        self.Platform_sprites = self.create_tile_group(Platform_layout, 'Platform')

        # plants setup
        Plants_layout = import_csv_layout(level_data['Plants'])
        self.Plants_sprites = self.create_tile_group(Plants_layout, 'Plants')

        # coins
        Coins_layout = import_csv_layout(level_data['Coins'])
        self.Coins_sprites = self.create_tile_group(Coins_layout, 'Coins')

        # enemy_worm
        Enemy_worm_layout = import_csv_layout(level_data['Enemy_worm'])
        self.Enemy_worm_sprites = self.create_tile_group(Enemy_worm_layout,'Enemy_worm')

        # Constraint enemy_worm
        Constraints_worm_layout = import_csv_layout(level_data['Constraints_worm'])
        self.Constraints_worm_sprites = self.create_tile_group(Constraints_worm_layout,'Constraints_worm')


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

                    if type == 'Enemy_worm':
                        sprite = Enemy(tile_size,x,y)

                    if type == 'Constraints_worm':
                        sprite = Tile(tile_size,x,y)

                    sprite_group.add(sprite)
        return sprite_group

    def player_setup(self,layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '253':
                    print('player goes here')
                if val == '239':
                    level_end_surface = pygame.image.load('../graphics/Misc/Level_end.png').convert_alpha()
                    sprite = StaticTile(tile_size,x,y,level_end_surface)
                    self.goal.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.Enemy_worm_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.Constraints_worm_sprites,False):
                enemy.reverse()
    
    def run(self):
        # platform
        self.Platform_sprites.update(self.world_shift)
        self.Platform_sprites.draw(self.display_surface)

        # plants
        self.Plants_sprites.draw(self.display_surface)
        self.Plants_sprites.update(self.world_shift)

        # enemy_worm
        self.Enemy_worm_sprites.update(self.world_shift)
        self.Constraints_worm_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.Enemy_worm_sprites.draw(self.display_surface)
        
        # coins
        self.Coins_sprites.update(self.world_shift)
        self.Coins_sprites.draw(self.display_surface)

        # player sprites
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

