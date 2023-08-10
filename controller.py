from copy import deepcopy
from item import Player, Ghost, Block
from map import Map
from getkey import getkey, keys

class Controller():
    ''' 以下の二つの機能を有する
            - Map, Player, Ghostを用いて描画処理を行う
            - 標準入力から方向に関する情報を受け取り、ベクトル形式で返す。ベクトルの定義は以下に示すとおり
        Def:
            方向の定義
                        w:上:[-1,0]
                        ^
                        |
          a:左:[0,-1]<-    -> d:右:[0,1]  
                        |   
                        v   
                    s:下:[1,0] 
    '''
    def wait_input(self) -> list[int]:
        ''' 
            Args:
                None
            Returns:
                direction: list[int] : 方向情報をベクトル形式で返す
            Examples:
                >>> ct = Contraller()
                >>> direction = ct.wait_input()
                >>> w, a, s, dのいずれかを入力してください: 
                a
                >>> print(direction)
                [0, -1]
        '''
        direction = None
        while direction == None:
            print("w, a, s, dのいずれかを入力してください: ")
            key = getkey().lower()
            print(f"入力された文字は {key} です。")
            if key == "w":
                direction = [-1, 0]
            elif key == "a":
                direction = [0, -1]
            elif key == "s":
                direction = [1, 0]
            elif key == "d":
                direction = [0, 1]
        return direction

    def display(self, map: Map, position: list[Player | Ghost | Block])->None:
        '''
            Player, Ghost, Blockの位置情報を受け取り、描画処理を行う
            Args:
                map: Map
                position: list[Player | Ghost | Block]
            Examples:
                >>> controller = Controller()
                >>> controller.display(map, [player, ghost, block])
        '''
        # mapのサイズを取得
        map_shape: tuple[int, int] = map.shape
        # screeをmapのサイズに合わせて初期化
        screen = []
        _screen: list[list[str]] = ['X'] * map_shape[1]
        for i in range(map_shape[0]):
            screen.append(deepcopy(_screen))
        # positionからオブジェクトの位置情報を取り出して、
        # アイコンを表示する位置を決定する
        for object in sorted(position):
            pos: list[int, int] = object.position
            screen[pos[0]][pos[1]]: str = object.icon
        # screenを表示する
        for row in screen:
            for col in row:
                print(col, end=" ")
            print()
    
def main():
    ct = Controller()
    map = Map(10)
    player = Player([2, 3])
    ghost = Ghost([4, 6])
    block = Block([9, 0])
    ct.display(map, [player, ghost, block])
    
if __name__ == "__main__":
    main()