from itertools import chain
import csv
class Enrolee:
    def __init__(self, name, prefer, points):
        pref1 = prefer.copy()
        pref1.append("Не прошел")
        self.prefer = pref1   # список предпочтений от наиб к наим
        self.points = points
        self.name = name


class Faculty:
    def __init__(self, name, num_vacant_places):
        self.num_vacant_places = num_vacant_places   # список бюджетных мест на каждую специальность
        self.name = name
        self.passed = []


def stable_matching():
    for ab in applicants:
        abit = (ab.name, ab.points)
        if abit not in list(chain(*passed_studets)):
            pref = list(map(lambda x: f[x], ab.prefer))
            pref_copy = pref.copy()
            for pr in pref:
                if abit not in passed_studets[pr]:
                    passed_studets[pr].append(abit)
                lsl = sorted(passed_studets[pr], key=lambda x: x[1], reverse=True)[:faculties[pr]]
                if abit not in lsl:
                    passed_studets[pr].remove(abit)
                    pref_copy.remove(pr)
            if len(pref_copy) != 0:
                maxs = pref_copy[0]
                for elem in pref:
                    if abit in passed_studets[elem] and maxs != elem:
                        passed_studets[elem].remove(abit)
    for i, elem in enumerate(passed_studets):
        passed_studets[i] = sorted(elem, key=lambda x: x[1], reverse=True)[:faculties[i]]


applicants = []
with open("уир.csv", encoding="utf8") as f:
    reader = csv.reader(f, delimiter=';', quotechar=' ')
    for i, row in enumerate(reader):
        if i == 0:
            continue
        lst = row[0].split(",")
        lst = lst[1:]
        lst1 = []
        for elem in lst:
            lst1.append(elem[1:-1])
        applicants.append(Enrolee(lst1[0],lst1[8:13] ,lst1[1]))


fac1 = Faculty("Прикладная математика и информатика", 7)
fac2 = Faculty("Информационные системы и технологии", 8)
fac3 = Faculty("Фотоника и оптоинформатика", 7)
fac4 = Faculty('Прикладная механика', 8)
fac5 = Faculty("Системы управления движением и навигация", 6)
unpassed_places = len(applicants) - fac1.num_vacant_places - fac2.num_vacant_places - fac3.num_vacant_places - fac4.num_vacant_places - fac5.num_vacant_places
unpassed = Faculty("Не прошел", unpassed_places)
faculties = [fac1.num_vacant_places, fac2.num_vacant_places, fac3.num_vacant_places, fac4.num_vacant_places, fac5.num_vacant_places, unpassed.num_vacant_places]
facs = [fac1, fac2, fac3, fac4, fac5, unpassed]
f = {
    "Прикладная математика и информатика": 0,
    "Информационные системы и технологии": 1,
    "Фотоника и оптоинформатика": 2,
    'Прикладная механика': 3,
    'Системы управления движением и навигация': 4,
    'Не прошел': 5
}


passed_studets = [[] for _ in range(len(faculties))]
for i in range(len(applicants)**2):
    stable_matching()

for i, fac in enumerate(facs):
    fac.passed = passed_studets[i]
    print(fac.name, fac.passed)

with open("uir_spiski","w") as f:
    for i, fac in enumerate(facs):
        f.write("\n")
        f.write(f"{fac.name}:")
        f.write("\n")
        fac.passed = passed_studets[i]
        lst = [abit[0] + abit[1] + '\n' for abit in fac.passed]
        for ab in lst:
            f.write(ab)







