import sprite
from location import LOCATIONS

def mode_play(game):
    background = LOCATIONS[game.current_location]["background"]

    # Рисуем интерфейс
    game.draw_sprite(sprite.play_menu, 0, 24, 1)
    game.draw_sprite(sprite.play_game, 20, 27, 1)
    game.draw_sprite(background, 0, 1, game.size_z-1)

    game.clear()
    print(game.render())
    
    # Команда
    choice = input("> ")

    if choice == "4":
        return "map"     # Переключаемся на карту
    elif choice == "0":
        return "menu"    # Выходим из игры в меню
    else:
        return "play"    # Остаемся в этом же режиме

def mode_map(game):
    x_player, y_player = LOCATIONS[game.current_location]["coords"]

    # Рисуем интерфейс
    game.draw_sprite(sprite.map, 12, 0, 1)
    game.draw_sprite(sprite.play_menu, 0, 24, 1)
    game.draw_sprite(sprite.map_buttons, 23, 27, 1)

    game.draw_sprite(["■"], y_player, x_player, z=1)
    
    game.clear()
    print(game.render())
    
    # Команда
    choice = input("> ")

    if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
        routes = LOCATIONS[game.current_location]["routes"]
        if choice in routes:
            next_location = routes[choice]
            if next_location in LOCATIONS:
                game.current_location = next_location
                return "play"
            else:
                print(f"[нет локации: {next_location}]")
                return "map"
        else:
            print("[тут прохода нет]")
            return "map"
    
    elif choice == "0":
        return "play" # Переключаемся в игру
    else:   
        return "map" # Остаемся в этом же режиме

def mode_menu(game):
    # Рисуем меню паузы
    game.draw_sprite(sprite.play_menu, 0, 24, 1) 
    game.clear()
    print(game.render())
    
    choice = input("> ")
    if choice == "1":
        return "play"
    return "menu"

def run(game):
    current_mode = "play" # Начинаем с режима игры
    
    # Главный цикл сцены play
    while current_mode != "menu":
        game.clear_matrix()  
        game.draw_frame()
        
        # Роутинг режимов
        if current_mode == "play":
            current_mode = mode_play(game)
        elif current_mode == "map":
            current_mode = mode_map(game)
        elif current_mode == "mode_menu":
            current_mode = mode_menu(game)
            
    # Когда цикл прервался (current_mode стал "menu")
    return "menu" # Возвращаем управление в main.py