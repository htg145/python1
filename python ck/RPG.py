import os
import random
import time
import json

# ---------------------------전역변수---------------------------

player = {
    "name": "",
    "lvl": 1,
    "hp": 100,
    "max_hp": 100,
    "atk": 10,
    "exp": 0,
    "max_exp": 100,
    "gold": 0
}

monsters = [
    {"name": "슬라임", "hp": 30, "atk": 7, "exp": 60, "gold": 20},
    {"name": "고블린", "hp": 50, "atk": 12, "exp": 80, "gold": 45},
    {"name": "드래곤", "hp": 80, "atk": 28, "exp": 120, "gold": 60}
]


# ---------------------------유틸리티 함수---------------------------

def clear_console():
    # Windows는 'cls', Mac/Linux는 'clear' 명령어 사용
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter_to_continue1():
    print("")
    input("게임을 시작하려면 아무키를 눌러주세요 . . .")
    clear_console()
    print("")


def save_game():
    with open("save_data.json", "w", encoding="utf-8") as file:
        json.dump(player, file, indent=4, ensure_ascii=False)
    print("저장되었습니다.")


def load_game():
    global player
    try:
        with open("save_data.json", "r", encoding="utf-8") as file:
            player = json.load(file)
        print("불러오기 성공!")
    except FileNotFoundError:
        print("저장된 데이터가 없습니다.")


# ---------------------------플레이어 관련 함수---------------------------

def player_init():
    while True:  # 닉네임이 유효할 때까지 반복
        init_name = input("닉네임을 입력해주세요 . . . ")

        if init_name.strip() == "":  # 빈 문자열 또는 공백만 입력 시
            print("❌ 닉네임은 비워둘 수 없습니다. 다시 입력해주세요.")
        else:
            clear_console()
            break  # 유효한 닉네임이면 반복 종료

    player["name"] = init_name
    print(f"닉네임이 설정되었습니다 . . .{player['name']}")


def view_info():
    clear_console()
    print("\n👤 [내 정보]")
    print(f"닉네임: {player['name']}")
    print(f"레벨: {player['lvl']}")
    print(f"HP: {player['hp']}/{player['max_hp']}")
    print(f"공격력: {player['atk']}")
    print(f"경험치: {player['exp']}/{player['max_exp']}")
    print(f"골드: {player['gold']}")


# ---------------------------사냥 함수---------------------------

def select_monster():
    clear_console()
    print("몬스터를 선택하세요.")
    for i in range(len(monsters)):
        print(f"{i + 1}. {monsters[i]['name']}")
    hunt(input(". . ."))


def hunt(id):
    clear_console()
    mon_id = int(id)
    monster = monsters[mon_id - 1].copy()  # 몬스터 사본 생성
    print(f"⚔️ {monster['name']}를 만났습니다!")

    while monster["hp"] > 0 and player["hp"] > 0:
        # ▶️ 플레이어의 턴
        print(f"\n🧍 {player['name']} HP: {player['hp']}/{player['max_hp']} | 🐲 {monster['name']} HP: {monster['hp']}")

        print("\n===== 🗡️ [플레이어의 턴] =====")
        print("1. 공격")
        print("2. 도망치기")
        choice = input("행동을 선택하세요: ")

        if choice == "1":  # 공격 선택
            clear_console()
            print(f"{player['name']}의 공격! ({player['atk']} 데미지)")
            monster["hp"] -= player["atk"]
            time.sleep(1.5)
            if monster["hp"] <= 0:
                print(f"🎯 {monster['name']}를 처치했습니다!")
                gain_rewards(monster)
                break

        elif choice == "2":  # 도망치기 선택
            clear_console()
            if random.random() < 0.4:  # 40% 확률로 도망 성공
                print("🏃 도망치기에 성공했습니다!")
                time.sleep(1.5)
                break
            else:
                print("❌ 도망치기에 실패했습니다!")
                time.sleep(1.5)

        else:
            print("❌ 잘못된 입력입니다. 1 또는 2를 선택하세요.")
            continue  # 잘못된 입력 시 다시 플레이어의 턴으로

        # ▶️ 몬스터의 턴
        if monster["hp"] > 0:
            print(f"\n===== 🐲 [몬스터의 턴] =====")
            time.sleep(1.5)
            print(f"{monster['name']}의 공격! ({monster['atk']} 데미지)")
            player["hp"] -= monster["atk"]
            time.sleep(1.5)
            if player["hp"] <= 0:
                print("💀 당신은 쓰러졌습니다...")
                player["hp"] = player["max_hp"]  # 사망 후 체력 복구 (임시)
                break


def gain_rewards(monster):
    player["exp"] += monster["exp"]
    player["gold"] += monster["gold"]
    print(f"🎁 경험치 +{monster['exp']} / 골드 +{monster['gold']}")
    check_level_up()


def check_level_up():
    while player["exp"] >= player["max_exp"]:
        player["lvl"] += 1
        player["exp"] -= player["max_exp"]
        player["max_exp"] = int(player["max_exp"] * 1.5)
        player["max_hp"] += 20
        player["atk"] += 5
        player["hp"] = player["max_hp"]
        print(f"🎉 레벨업! 현재 레벨: {player['lvl']}")


# ---------------------------메뉴 선택---------------------------

def select_menu():
    while True:
        print("\n===== 📜 메뉴 =====")
        print("""
          1. 사냥
          2. 내 정보 조회
          3. 저장하기
          4. 불러오기
          5. 게임 종료
        """)

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            select_monster()
        elif choice == "2":
            view_info()
        elif choice == "3":
            save_game()
        elif choice == "4":
            load_game()
        elif choice == "5":
            clear_console()
            print("👋 게임을 종료합니다. 감사합니다!")
            break  # 반복문 종료 → 게임 종료
        else:
            print("❌ 잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")


def main():
    press_enter_to_continue1()
    player_init()
    select_menu()


# ---------------------------메인 실행부---------------------------
if __name__ == "__main__":
    main()