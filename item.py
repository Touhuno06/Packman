import random


class Item():
    """
    ディスプレイに表示されるアイテムのクラス

    Attributes:
        position (list[int]): Playerの位置を示す
    """
        
    def __init__(self, position: list[int], icon: str) -> None:
        """
        インスタンスの初期化

        Args:
            position (list[int]): 初期位置
            icon (str): プレイヤーの表示
        """
        self.position = position
        self.icon = icon

    def pre_move(self, movement_position: list[int]) -> list[int]:
        """
        次の位置の予測

        Args:
            movement_position (list[int]): 次の動作の相対的な位置

        Return:
            list[int]: 次の位置

        Example:
            >>> p = Player([0, 0])
            >>> p.pre_move([0, 1])
            [0, 1]

            >>> p = Player([0, 0])
            >>> p.pre_move([-1, 0])
            [-1, 0]

            >>> p = Player([1, 1])
            >>> p.pre_move([-1, 0])
            [0, 1]

        """
        result = list()
        for i, coordinate in enumerate(self.position):
            result.append(coordinate + movement_position[i])
        return result

    def conflict(self, position: list[int]) -> bool:
        '''
        敵の座標とプレイヤーの座標が一致しているかを判定する．
        Args:
            position (list[int]): プレイヤーの座標
        Returns:
            bool: 敵の座標とプレイヤーの座標が一致しているか、一致していたらTrue
        Example:
            >>> ghost_1 = Ghost([5, 4]) 
            >>> ghost_2 = Ghost([5, 2])
            >>> ghost_1.conflict([5, 4])
            True
            >>> ghost_1.conflict([5, 5])
            False
            >>> ghost_1.conflict([5, 4, 6])
            False
            >>> ghost_1.conflict([5.0, 4])
            True
            >>> ghost_1.conflict([5, 4.0])
            True
            >>> ghost_2.conflict([5, 2])
            True
            >>> ghost_2.conflict([2147483649, 4])
            False
            >>> ghost_1.conflict((5, 4))
            False
        '''

        return (self.position == position)

    def move(self, next_position: list[int]) -> None:
        """
        次の動作

        Args:
            next_position (list[int]): 次の動作の位置

        Return:
            None

        Example:
            >>> p = Player([1, 1])
            >>> p.position
            [1, 1]
            >>> p.move([1, 0])
            >>> p.position
            [1, 0]
        """

        self.position = next_position


class Player(Item):    
    """
    プレイヤーのクラス

    このクラスはプレイヤーの座標を管理する．
    Attributes:
        position (list[int]): プレイヤーの位置を示す
    """
    def __init__(self, position: list[int], icon: str = 'P') -> None:
        """
        インスタンスの初期化

        Args:
            position (list[int]): 初期位置
            icon (str): プレイヤーの表示
        """
        super().__init__(position, icon)


class Ghost(Item):
    '''
    お化けのクラス

    このクラスはお化けの座標を管理する．

    '''
    def __init__(self, position: list[int], icon: str = 'G') -> None:
        """
        インスタンスの初期化

        Args:
            position (list[int]): 初期位置
            icon (str): プレイヤーの表示
        """
        super().__init__(position, icon)

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


class Block(Item):
    def __init__(self, position: list[int], icon: str = 'B') -> None:
        """
        インスタンスの初期化

        Args:
            position (list[int]): 初期位置
            icon (str): プレイヤーの表示
        """
        super().__init__(position, icon)

    def pre_move(self, movement_position: list[int]) -> list[int]:
        """
        pre_moveにおけるブロックの例外処理
        
        Args:
            movement_position (list[int]): 次の動作の相対的な位置

        Return:
            list [int]: 次の位置

        Example:
            >>> b = Block([0,0])
            >>> try:
            ...     b.pre_move([0,1])
            ... except Exception as e:
            ...     print(e)
            ブロックは移動できません

            >>> b = Block([0,0])
            >>> try:
            ...     b.pre_move([-1,0])
            ... except Exception as e:
            ...     print(e)
            ブロックは移動できません

            >>> b = Block([1,0])
            >>> try:
            ...     b.pre_move([1,0])
            ... except Exception as e:
            ...     print(e)
            ブロックは移動できません
        """
        raise Exception('ブロックは移動できません')

    def move(self, next_position: list[int]) -> None:
        """
        moveにおけるブロックの例外処理
        
        Args:
            movement_position (list[int]): 次の動作の位置

        Return:
            list[int]: 次の位置

        Example:
            >>> b = Block([0, 0])
            >>> try:
            ...     b.move([0, 1])
            ... except Exception as e:
            ...     print(e)
            ブロックは移動できません

            >>> b = Block([0, 0])
            >>> try:
            ...     b.move([-1, 0])
            ... except Exception as e:
            ...     print(e)
            ブロックは移動できません

            >>> b = Block([1, 0])
            >>> try:
            ...     b.move([1, 0])
            ... except Exception as e:
            ...     print(e)
            ブロックは移動できません
        """
        raise Exception('ブロックは移動できません')


if __name__ == '__main__':
    import doctest
    doctest.testmod() 