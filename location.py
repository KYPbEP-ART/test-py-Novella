import sprite

LOCATIONS = {
    "pizzeria": {
        "name": "Пиццерия",                         # имя локации
        "background": sprite.city_night,            # фон
        "coords": [16, 29],                         # координаты отрисовки игрока
        "routes": {"1": "checkpoint", "3": "lane"}, # пути
        "event": None,                              # квесты
    },
    "checkpoint": {
        "name": "Блокпост",
        "background": sprite.main_menu,
        "coords": [16, 13], 
        "routes": {"3": "тест", "8": "pizzeria"},
        "event": None,    
    },
    "lane": {
        "name": "Периулок",
        "background": sprite.city_night,
        "coords": [20, 13], 
        "routes": {"6": "pizzeria", "1": "тест", "3":"тест", "5":"тест"},
        "event": None,    
    },
}