from item import Block, Cookie


class Map():
    """マップ上のオブジェクトを保持し、衝突判定を行うクラス.

    Attributes:
        size (int): マップのサイズ.(マップはsize*sizeのサイズとなる)
    """
    def __init__(self, size: int) -> None:
        """Mapクラスのコンストラクタ.
        マップのサイズ定義とBlockオブジェクトの配置を行う.

        Args:
            size (int): マップのサイズ.(マップはsize*sizeのサイズとなる)
        
        Example:
            >>> map = Map(3)
            >>> map.shape
            (3, 3)
            >>> for items in map.map_items.values():
            ...      print(items.position)
            [0, 0]
            [0, 1]
            [0, 2]
            [1, 0]
            [1, 1]
            [1, 2]
            [2, 0]
            [2, 1]
            [2, 2]

            >>> for k in map.map_items.keys():
            ...      print(k)
            (0, 0)
            (0, 1)
            (0, 2)
            (1, 0)
            (1, 1)
            (1, 2)
            (2, 0)
            (2, 1)
            (2, 2)
        """
        self.map_items = dict()
        self.shape = (size, size)
        for i in range(size):
            for j in range(size):
                if(i==0 or j==0 or i==size-1 or j==size-1):
                    self.map_items[(i, j)] = Block([i, j])
                else:
                    self.map_items[(i, j)] = Cookie([i, j])

    def conflict(self, position: list[int]) -> bool | str:
        """マップ上のオブジェクトと与えられた位置との衝突判定を行うメソッド.
        想定しているマップの範囲外をpositionで指定した場合も衝突したと判定する.

        Args:
            position (list[int]): 衝突判定を行う相手の位置.

        Returns:
            bool: 衝突した時その対象のクラス名を返し、衝突しなければFalseを返す.

        Example:
            >>> map = Map(3)
            >>> map.conflict([0, 0])
            'Block'
            >>> map.conflict([0, 1])
            'Block'
            >>> map.conflict([0, 2])
            'Block'
            >>> map.conflict([1, 0])
            'Block'
            >>> map.conflict([1, 1])
            'Cookie'
            >>> map.conflict([1, 2])
            'Block'
            >>> map.conflict([2, 0])
            'Block'
            >>> map.conflict([2, 1])
            'Block'
            >>> map.conflict([2, 2])
            'Block'
            >>> map.conflict([3, 1])
            'Block'
            >>> map.conflict([-1, 1])
            'Block'
        """
        for i, coordinate in enumerate(position):
            if(coordinate < 0 or coordinate >= self.shape[i]):
                return Block.__name__
        items_value = self.map_items.get(tuple(position))
        if(items_value == None):
            return  False
        else:
            return type(items_value).__name__
        
    def delete_item(self, position: list[int]) -> None:
        """
        衝突したマップ上のアイテムを削除するメソッド

        Args:
            position(list[int]): 消去する対象の位置
        
        
        """
        self.map_items.pop(tuple(position))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
