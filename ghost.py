import random
class Ghost():
    def __init__(self, position: list[int]):
        '''
        敵の初期座標を設定する．
        ----------
        >>> a=Ghost(5,4)
        >>> a.positon[0]
        5
        >>> a.positon[1]
        4
        '''

        self.position = position
    
    def pre_move(self) -> list[int]:
        '''
        敵の次の座標を決定する．
        ----------
        >>> a=Ghost(5,4)
        >>> a.pre_move()
        [5,5]
        '''
        enemy_move_direction=[[1,0],[-1,0],[0,1],[0,-1]]
        next_position=[]
        move_vector=random.choice(enemy_move_direction)
        for i in range(2):
            next_position.append(self.position[i]+move_vector[i])
        return next_position
    
    def conflict(self, position: list[int]) -> bool:
        return (self.position == position)
    
    def move(self, next_position: list[int]) -> None:
        self.position = next_position
if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    a=Ghost([5,4])
    print(a.pre_move())