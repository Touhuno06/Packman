from map import Map
from item import Player, Ghost, Block
from controller import Controller


class Game():
    def __init__(self) -> None:
        map_ = Map(8)
        player = Player([6,4])
        ghost1 = Ghost([2,2])
        ghost2 = Ghost([2,6])

        controller = Controller()
        while True:
            controller.display(map_, [player, ghost1,ghost2] + map_.block_array)    
            player_pre_move = player.pre_move(controller.wait_input())
            player_judgement = map_.conflict(player_pre_move)
            if player_judgement == False:
                player.move(player_pre_move)
            ghost_pre_move = ghost1.pre_move()
            ghost_judgement = map_.conflict(ghost_pre_move)            
            if ghost_judgement == False:
                ghost1.move(ghost_pre_move)
            ghost_pre_move = ghost2.pre_move()
            ghost_judgement = map_.conflict(ghost_pre_move)            
            if ghost_judgement == False:
                ghost2.move(ghost_pre_move)
            game_over1 = ghost1.conflict(player.position)
            game_over2 = ghost2.conflict(player.position)
            if game_over1 | game_over2 == True:
                break
        print("Game Over")
