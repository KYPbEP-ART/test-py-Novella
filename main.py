import os

from scenes import menu, play

class Game:
    def __init__(self):
        # Матрица и размер
        self.size_x = 63
        self.size_y = 32
        self.size_z = 15

        self.matrix = [[[" " for _ in range(self.size_x)] for _ in range(self.size_y)] for _ in range(self.size_z)]

        # Состояние игрока
        self.money = 100
        self.hp = 100
        self.time_h= 19.00
        self.karma = 0
        self.current_location = "pizzeria"

        # Начальная сцена
        self.current_scene = "play" 

    def clear(self):
        # Очистка экрана
        os.system('cls' if os.name == 'nt' else 'clear')

    def clear_matrix(self):
        # Очистка ДАННЫХ в памяти
        for z in range(self.size_z):
            for y in range(self.size_y):
                for x in range(self.size_x):
                    self.matrix[z][y][x] = " "

    def render(self):
        # Локальные переменные! Без self.
        rows = []
        for y in range(self.size_y):
            row = ""
            for x in range(self.size_x):
                for z in range(self.size_z):
                    if self.matrix[z][y][x] != " ":
                        row += self.matrix[z][y][x]
                        break
                else:
                    row += " "
            rows.append(row)
        return "\n".join(rows)
    
    def draw_sprite(self, sprite, x, y, z=0):
        """sprite - список строк. x, y - левый верхний угол."""
        for row_idx, row in enumerate(sprite):
            py = y + row_idx
            if not (0 <= py < self.size_y):
                continue                      # строка вне экрана - пропускаем
            for col_idx, char in enumerate(row):
                px = x + col_idx
                if not (0 <= px < self.size_x):
                    continue                  # символ вне экрана - пропускаем
                if char != " ":
                    self.matrix[z][py][px] = char

    def draw_frame(self):
        """Рисует рамку по краям матрицы"""
        for x in range(self.size_x):
            self.matrix[14][0][x] = "-"
            self.matrix[14][self.size_y-1][x] = "-"
        for y in range(self.size_y):
            self.matrix[14][y][0] = "|" 
            self.matrix[14][y][self.size_x-1] = "|"

        self.matrix[14][0][0] = "+"
        self.matrix[14][self.size_y-1][0] = "+"
        self.matrix[14][0][self.size_x-1] = "+"
        self.matrix[14][self.size_y-1][self.size_x-1] = "+"

    
    def run(self):
        # Главный цикл
        while self.current_scene != "quit":
            
            if self.current_scene == "menu":
                self.current_scene = menu.run(self)  
                
            elif self.current_scene == "play":
                self.current_scene = play.run(self)  
                
            else:
                self.current_scene = "quit"

# Точка входа
if __name__ == "__main__":
    game = Game()
    game.run()
