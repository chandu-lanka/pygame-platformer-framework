import pygame

class Collision():
    def __init__(self):
        pass

    def TileCollision(self, player, tiles):
        player_sprite = player.sprite
        player_sprite.rect.x += player_sprite.direction.x * player_sprite.speed
        player_sprite.apply_gravity()

        # horizontal collision detection
        for sprite in tiles:
            if sprite.rect.colliderect(player_sprite.rect):
                if player_sprite.direction.x < 0:
                    player_sprite.rect.left = sprite.rect.right
                elif player_sprite.direction.x > 0:
                    player_sprite.rect.right = sprite.rect.left

        # vertical collision detection
        for sprite in tiles:
            if sprite.rect.colliderect(player_sprite.rect):
                if player_sprite.direction.y > 0:
                    player_sprite.rect.bottom = sprite.rect.top
                elif player_sprite.direction.y < 0:
                    player_sprite.rect.top = sprite.rect.bottom
        
