import random


class Ghost():
    '''
    お化けのクラス

    このクラスはお化けの座標を管理する．

    '''
    def __init__(self, position: list[int]):
        '''
        敵の初期座標を設定する．
        Args:
            position (list[int]): 敵の初期座標
        Example:
            >>> ghost_1 = Ghost([5, 4])
            >>> ghost_1.position
            [5, 4]
        '''

        self.position = position
    
    def pre_move(self) -> list[int]:
        '''
        敵の次の座標を決定する．
        Returns:
            next_position (list[int]): 敵の次の座標
        Example:
            >>> ghost_1=Ghost([5, 4])
            >>> random.seed(0)
            >>> ghost_1.pre_move()
            [5, 3]
        '''
        enemy_move_direction = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        next_position = []
        move_vector = random.choice(enemy_move_direction)
        for i in range(2):
            next_position.append(self.position[i] + move_vector[i])
        return next_position
    
    def conflict(self, position: list[int]) -> bool:
        '''
        敵の座標とプレイヤーの座標が一致しているかを判定する．
        Args:
            position (list[int]): プレイヤーの座標
        Returns:
            bool: 敵の座標とプレイヤーの座標が一致しているか、一致していたらTrue
        Example:
            >>> ghost_1=Ghost([5,4]) 
            >>> ghost_2=Ghost([5,2])
            >>> ghost_1.conflict([5,4])
            True
            >>> ghost_1.conflict([5,5])
            False
            >>> ghost_1.conflict([5,4,6])
            False
            >>> ghost_1.conflict([5.0,4])
            True
            >>> ghost_1.conflict([5,4.0])
            True
            >>> ghost_2.conflict([5,2])
            True
            >>> ghost_2.conflict([2147483649,4])
            False
            >>> ghost_1.conflict((5,4))
            False
        '''

        return (self.position == position)
    
    def move(self, next_position: list[int]) -> None:
        '''
        敵の座標を更新するただし次の座標の次元が2次元でない場合は更新しない
        Args:
            next_position （list[int]）: 敵の次の座標
        ----------
        Example:
            >>> ghost_1=Ghost([5,4])
            >>> ghost_1.move([5,5])
            >>> ghost_1.position
            [5, 5]
            >>> ghost_2=Ghost([5,4])
            >>> ghost_2.move([5,5,6])
            >>> ghost_2.position
            [5, 4]
        '''
        if len(next_position) == 2:
            self.position = next_position


if __name__ == '__main__':
    import doctest
    doctest.testmod()


