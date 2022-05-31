class DanceTeam:
    def __init__(self, team_members=0, team_name=""):
        self.team_members = team_members
        self.team_name = team_name

    def members_check(self):
        list = []
        for i in range(self.team_members):
            a = input('введите фамилию участника:')
            list.append(a)
        return list

    def members_comparison(self, lst1, lst2):
        res = list(map(lambda x: (x, x), filter(lambda y: y in lst1, lst2)))
        if res == []:
            print('Совпадений не обнаружено')
        else:
            print(len(res), 'В командах совпадают участники и это:', res)

    def name_check(self, nm1: tuple):
        asd = []
        for i in range(len(nm1)):
            for j in range(len(nm1)):
                if i == j:
                    continue
                if nm1[i].team_name == nm1[j].team_name and not (nm1[i].team_name in asd):
                    # print("ааааааааааааа", end=" ")
                    # print(nm1[i].team_name)
                    asd.append(nm1[i].team_name)
        if asd == []:
            pass
        else:
            print('Команд(а)ы', asd[::], "ввела данные несколько раз")


b = DanceTeam(2, 'stepout')
# b.members_check()
h = DanceTeam(1, 'epout')
h1 = DanceTeam(1, 'epout')
h2 = DanceTeam(1, 'stepout')
# h.members_check()
b.members_comparison(b.members_check(), h.members_check())
DanceTeam().name_check((h1, h2))
