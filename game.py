from map import Map, Block
from player import Player
from controller import Controller
from ghost import Ghost
class Game():
    def __init__(self):
        map=Map(7)
        
        
        player=Player([5,3])
        ghost=Ghost([1,3])
        controller=Controller()
        

        while True:
            controller.display(map,[player,ghost]+map.block_array)    
            player_pre_move=player.pre_move(controller.wait_input())
            player_judgement=map.conflict(player_pre_move)
            if player_judgement==False:
                player.move(player_pre_move)
            
            ghost_pre_move=ghost.pre_move()
            ghost_judgement=map.conflict(ghost_pre_move)            
            if ghost_judgement==False:
                ghost.move(ghost_pre_move)

            game_over=ghost.conflict(player.position)
            if game_over==True:
                break
        print("Game Over")



