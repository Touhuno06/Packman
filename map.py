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
            >>> for block in map.block_array:
            ...      block.position
            [0, 0]
            [0, 1]
            [0, 2]
            [1, 0]
            [1, 2]
            [2, 0]
            [2, 1]
            [2, 2]
        """
        self.block_array = list()
        self.shape = (size, size)
        for i in range(size):
            for j in range(size):
                if(i==0 or j==0 or i==size-1 or j==size-1):
                    self.block_array.append(Block([i, j]))

    def conflict(self, position: list[int]) -> bool:
        """マップ上のオブジェクトと与えられた位置との衝突判定を行うメソッド.
        想定しているマップの範囲外をpositionで指定した場合も衝突したと判定する.

        Args:
            position (list[int]): 衝突判定を行う相手の位置.

        Returns:
            bool: 衝突するならTrue, しなければFalse.

        Example:
            >>> map = Map(3)
            >>> map.conflict([0, 0])
            True
            >>> map.conflict([0, 1])
            True
            >>> map.conflict([0, 2])
            True
            >>> map.conflict([1, 0])
            True
            >>> map.conflict([1, 1])
            False
            >>> map.conflict([1, 2])
            True
            >>> map.conflict([2, 0])
            True
            >>> map.conflict([2, 1])
            True
            >>> map.conflict([2, 2])
            True
            >>> map.conflict([3, 1])
            True
            >>> map.conflict([-1, 1])
            True
        """
        for i, coordinate in enumerate(position):
            if(coordinate<0 or coordinate>=self.shape[i]):
                return True
        for block in self.block_array:
            if(position==block.position):
                return True
        return False
    

class Block():
    """一つのブロックの位置を保持し衝突判定を行うクラス.

    Attributes:
        size (list[int]): マップのサイズ.(マップはsize*sizeのサイズとなる)
    """
    def __init__(self, position: list[int]) -> None:
        self.position = position
    
    def conflict(self, position: list[int]) -> bool:
        """ブロックとの衝突判定を行うメソッド.

        Args:
            position (list[int]): 衝突判定を行う相手の位置.

        Returns:
            bool: 衝突するならTrue, しなければFalse.

        Example:
            >>> block = Block([0,4])
            >>> block.conflict([0,4])
            True
            >>> block.conflict([1,4])
            False
        """
        if(position==self.position):
            return True
        else:
            return False
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
