import sprite

def run(game):
    # Очищаем матрицу
    game.clear_matrix()  
    
    # Рисуем рамку по краям
    game.draw_frame()

    # Остальной интерфейс
    game.draw_sprite(sprite.main_menu[:18], 14, 1, 1)
    game.draw_sprite(sprite.main_menu[18:19], 22, 20, 1)
    game.draw_sprite(sprite.main_menu[19:23], 27, 22, 1)
    game.draw_sprite(sprite.main_menu[23:], 22, 27, 1)

    # Очищаем сам терминал и печатаем матрицу
    game.clear()
    print(game.render())  

    """TEST"""

    """/TEST"""
    
    # Ввод команды
    choice = input("> ")
    
    if choice == "1":
        return "play"
    elif choice == "0":
        return "quit"
    return "menu"