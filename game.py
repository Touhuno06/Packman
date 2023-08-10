from map import Map
from item import Player, Ghost, Block,Cookie
from controller import Controller


class Game():
    def __init__(self) -> None:
        map_ = Map(8)
        player = Player([6,4])
        ghosts = [Ghost([2,2]), Ghost([2,5])]
        controller = Controller()
        while True:
            controller.display(map_, [player] + ghosts + list(map_.map_items.values()))    
            player_pre_move = player.pre_move(controller.wait_input())
            player_judgement = map_.conflict(player_pre_move)
            if player_judgement == False:
                player.move(player_pre_move)
            elif player_judgement == Cookie.__name__:
                map_.delete_item(player_pre_move)
                player.move(player_pre_move)
            game_over = False
            for g in ghosts:
                ghost_pre_move = g.pre_move()
                ghost_judgement = map_.conflict(ghost_pre_move)     
                if ghost_judgement == False:
                    g.move(ghost_pre_move)
                elif ghost_judgement == Cookie.__name__:
                    g.move(ghost_pre_move)
                game_over = g.conflict(player.position)
                if game_over == True:
                    break
            if game_over:
                print("Game Over")
                break
