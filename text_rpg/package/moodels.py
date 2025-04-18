# 플레이어 클래스

class Player:
    def __init__(self, nickname, level=1, gold=0 , attack=10, exp=0, max_exp=100, hp=100, max_hp=100, mp=50, max_mp=50, cri_luk=0, skills=None, items=None):
        self.nickname = nickname
        self.level = level
        self.gold = gold
        self.attack = attack
        self.exp = exp
        self.max_exp = max_exp
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp = max_mp
        self.cri_luk = cri_luk
        self.skills = skills if skills else [
            {"name": "달팽이 세마리", "mp_cost": 30, "damage_multiple":1.2},
            {"name": "달팽이 네마리", "mp_cost": 40, "damage_multiple": 1.5},
            {"name": "달팽이 다섯 마리", "mp_cost": 60, "damage_multiple": 1.8}
        ]
        self.items = items if items else []

    def to_dict(self):
        return self.__dict__ # 클래스(인스 턴스)의 내부 상태를 딕셔 너리로 변환



    @classmethod
    def from_dict(cls, date):
        return cls(**date) # ** 언패킹

    def apply_itme(self, item):
        self.attack += item["attack"]
        self.max_hp += item["max_hp"]
        self.max_mp += item["max_mp"]

        print(f"<{item["name"]}> \n공격력 +{item["attack"]} => {self.attack}\n최대 HP +{item["hp"]} => {self.max_hp}\n최대 MP +{item["mp"]}\n추가 치명타 확률 +{item["cri_luk"]}% => {self.cri_luk}")

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.max_exp:
            left_amount = amount - self.max_exp
            self.level_up(left_amount)


    def level_up(self, amount):
        self.level += 1
        self.attack += 5
        self.max_hp += 10
        self.max_mp += 10
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.exp = 0
        self.max_exp = int(self.max_exp * 1.5)
        print(f"레벨 업! {self.level + 1} 레벨이 되었 습니다. 공격력 +5, 최대 HP +10, 최대 MP +10")

    def mp_recovery(self, mp):
        self.mp = min(self.max_mp, self.mp + mp)
        print(f"현재 MP:{self.mp}")

    def play_dead(self):
        self.items = []


    """
    인스 턴스 메소드 => 우리가 기본적 으로 알고 있는 메소드
    스태틱 메소드 => 클래스 내에 유틸성 메소드, 즉 인스 턴스나 클래스의 속성에 접근할 수 없음
    클래스 메소드 => 인스 턴스를 생성 하지 않고 클래스에 직접적 으로 접근함
    첫번쨰 인자로 해당 클래스(기본값), 두번쨰 인자 데이터로 넣어서 딕셔 너리 언패킹
    """


# 몬스터 클래스
class Monster:
    def __init__(self, name, hp, max_hp,attack, exp_reward, gold_reward):
        self.name = name
        self.hp = max_hp
        self.max_hp = hp
        self.attack = attack
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward


