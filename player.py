"""
Playerクラスの動作
"""


class Player():    
    """
    初期位置の設定

    Attributes:
        position (list[int]): Playerの位置を示す
    """

    def __init__(self, position: list[int], icon: str = 'P') -> None:
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


if __name__ == '__main__':
    import doctest
    doctest.testmod() 
