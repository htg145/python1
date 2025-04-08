from package.moodels import Monster

monsters = [
    Monster("주황버섯", 1, 30, 30,5, 30),
    Monster("슬라임", 2, 50, 50, 10, 50),
    Monster("핑크빈", 5, 100, 100, 30, 100)
]

shop_items = [
    {"name": "도란의 검", "attack": 10, "hp": 0, "mp": 0, "cri_luk": 10, "price": 50},
    {"name": "롱소드", "attack": 30, "hp": 0, "mp": 0, "cri_luk": 80, "price": 50},
    {"name": "민첩성 망토", "attack": 30, "hp": 50, "mp": 20, "cri_luk": 100, "price": 50},
    {"name": "사파 이어 수정", "attack": 60, "hp": 0, "mp": 60, "cri_luk": 20, "price": 55},
    {"name": "여신의 눈", "attack": 5, "hp": 0, "mp": 100, "cri_luk": 50, "price": 50},
    {"name": "삼위 일체", "attack": 60, "hp": 60, "mp": 60, "cri_luk": 60, "price": 300}
]