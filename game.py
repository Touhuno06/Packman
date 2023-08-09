from map import Map
from item import Player, Ghost, Block
from controller import Controller


class Game():
    def __init__(self) -> None:
        map_ = Map(7)
        player = Player([5,3])
        ghost = Ghost([1,3])
        controller = Controller()
        while True:
            controller.display(map_, [player, ghost] + map_.block_array)    
            player_pre_move = player.pre_move(controller.wait_input())
            player_judgement = map_.conflict(player_pre_move)
            if player_judgement == False:
                player.move(player_pre_move)
            ghost_pre_move = ghost.pre_move()
            ghost_judgement = map_.conflict(ghost_pre_move)            
            if ghost_judgement == False:
                ghost.move(ghost_pre_move)
            game_over = ghost.conflict(player.position)
            if game_over == True:
                break
        print("Game Over")
