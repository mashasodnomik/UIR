from itertools import chain

class Enrolee:
    def __init__(self, name, prefer, points):
        self.prefer = prefer   # список предпочтений от наиб к наим
        self.points = points
        self.name = name


class Faculty:
    def __init__(self, name, num_vacant_places):
        self.num_vacant_places = num_vacant_places   # список бюджетных мест на каждую специальность
        self.name = name


def stable_matching(ab, prefer):
    abit = (ab.name, ab.points)
    if count == 0:
        passed_studets[prefer - 1].append(abit)
    else:
        last_abit = passed_studets[prefer-1][-1]
        last_abit_points = last_abit[1]
        if ab.points < last_abit_points:
            pass
        elif ab.points > last_abit_points:
            passed_studets[prefer - 1].append(abit)
        elif ab.points == last_abit_points:
            #   !!!!!ПОСМОТРЕТЬ ЧЕ МОЖНО СДЕЛАТЬ !!!!!!
            passed_studets[prefer - 1].append(abit)
            lost_equal_abit.append(abit)


ab1 = Enrolee("abit1", ["c1", "c3", "c2"], 273)
ab2 = Enrolee("abit2", ["c2", "c1", "c3"], 242)
ab3 = Enrolee("abit3", ["c1", "c3", "c2"], 256)
ab4 = Enrolee("abit4", ["c3", "c2", "c1"], 302)
ab5 = Enrolee("abit5", ["c1", "c3", "c2"], 264)
ab6 = Enrolee("abit6", ["c3", "c1", "c2"], 257)
ab7 = Enrolee("abit7", ["c1", "c3", "c2"], 278)
ab8 = Enrolee("abit8", ["c3", "c1", "c2"], 298)
ab9 = Enrolee("abit9", ["c1", "c2", "c3"], 237)
ab10 = Enrolee("abit10", ["c2", "c3", "c1"], 259)
ab11 = Enrolee("abit11", ["c2", "c1", "c3"], 278)
ab12 = Enrolee("abit12", ["c2", "c3", "c1"], 280)

applicants = [ab1, ab2, ab3, ab4, ab5, ab6, ab7, ab8, ab9, ab10, ab11, ab12]

fac1 = Faculty("dtg", 3)
fac2 = Faculty("srf", 2)
fac3 = Faculty("stts", 4)
faculties = [fac1.num_vacant_places, fac2.num_vacant_places, fac3.num_vacant_places]

f = {}
for i in range(len(faculties)):
    f[f"c{i + 1}"] = i + 1

count = 0
passed_studets = [[] for _ in range(len(faculties))]
for i in range(len(faculties)):
    lost_equal_abit = []
    for ab in applicants:
        abit = (ab.name, ab.points)
        pref = f[ab.prefer[i]]
        if abit not in list(chain(*passed_studets)):
            stable_matching(ab, pref)
    for e, l in enumerate(passed_studets):
        l.sort(key=lambda abit: abit[1], reverse=True)
        l = l[:faculties[e]]
        for abit in l:
            if abit in lost_equal_abit and abit not in l:
                l.append(abit)
                print(f"на специальность {l} зачислены абитуриенты с одинаковым кол-вом баллов, что превышает кол-во бюджетным мест")
        passed_studets[e] = l
    count = count + 1

print(*passed_studets, sep="\n")

