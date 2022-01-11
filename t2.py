
passed_students_c1 = []
passed_students_c2 = []
passed_students_c3 = []

abiturients = {

    "ab1": [273, 1, 3, 2],
    "ab2": [242, 2, 1, 3],
    "ab3": [256, 1, 3, 2],
    "ab4": [302, 3, 2, 1],
    "ab5": [264, 1, 3, 2],
    "ab6": [257, 3, 1, 2],
    "ab7": [278, 1, 3, 2],
    "ab8": [298, 3, 1, 2],
    "ab9": [237, 1, 2, 3],
    "ab10": [259, 2, 3, 1],
    "ab11": [278, 2, 1, 3],
    "ab12": [280, 2, 3, 1],
}

vacant = {
    "c1": [],
    "c2": [],
    "c3": [],
}
vacant_places_c1 = 3
vacant_places_c2 = 2
vacant_places_c3 = 4
c1 = []
c2 = []
c3 = []
for i in range(len(vacant.keys())):
    if i == 0:
        for ab in abiturients.keys():
            if ab not in passed_students_c1 or ab not in passed_students_c2 or ab not in passed_students_c3:
                prefer = abiturients.get(ab)[i + 1]
                points = abiturients.get(ab)[0]
                if prefer == 1:
                    c1.append((ab, points))
                elif prefer == 2:
                    c2.append((ab, points))
                elif prefer == 3:
                    c3.append((ab, points))
        lst = [c1, c2, c3]
        for l in lst:
            l.sort(key=lambda abit: abit[1], reverse=True)

        c1 = sorted(c1, key=lambda abit: abit[1], reverse=True)
        c2 = sorted(c2, key=lambda abit: abit[1], reverse=True)
        c3 = sorted(c3, key=lambda abit: abit[1], reverse=True)
        for abit in c1:
            if c1.index(abit) < vacant_places_c1:
                passed_students_c1.append(abit)
        for abit in c2:
            if c2.index(abit) < vacant_places_c2:
                passed_students_c2.append(abit)
        for abit in c3:
            if c3.index(abit) < vacant_places_c3:
                passed_students_c3.append(abit)
        vacant["c1"] = passed_students_c1
        vacant["c2"] = passed_students_c2
        vacant["c3"] = passed_students_c3
        print(f"прошедшие после первого{vacant}")
    elif i != 0:
        c1 = passed_students_c1
        c2 = passed_students_c2
        c3 = passed_students_c3
        passed_students_c1 = []
        passed_students_c2 = []
        passed_students_c3 = []
        lost_equal_abit = []
        for ab in abiturients.keys():
            abit = (ab, abiturients.get(ab)[0])
            if abit not in vacant.get("c1") and abit not in vacant.get("c2") and abit not in vacant.get("c3"):
                print(f"{ab} никуда не прошел")
                prefer = abiturients.get(ab)[i + 1]
                points = abiturients.get(ab)[0]
                if prefer == 1:
                    last_abit = vacant.get("c1")[-1]
                    last_abit_points = last_abit[1]
                    if points < last_abit_points:
                        pass
                    elif points > last_abit_points:
                        c1.append((ab, points))
                    elif points == last_abit_points:
                        #   !!!!!ПОСМОТРЕТЬ ЧЕ МОЖНО СДЕЛАТЬ !!!!!!
                        c1.append((ab, points))
                        lost_equal_abit.append((ab, points))

                if prefer == 2:
                    last_abit = vacant.get("c2")[-1]
                    last_abit_points = last_abit[1]
                    if points < last_abit_points:
                        pass
                    elif points > last_abit_points:
                        c2.append((ab, points))
                    elif points == last_abit_points:
                        #   !!!!!ПОСМОТРЕТЬ ЧЕ МОЖНО СДЕЛАТЬ !!!!!!
                        c2.append((ab, points))
                        lost_equal_abit.append((ab, points))

                if prefer == 3:
                    last_abit = vacant.get("c3")[-1]
                    last_abit_points = last_abit[1]
                    if points < last_abit_points:
                        pass
                    elif points > last_abit_points:
                        c3.append((ab, points))
                    elif points == last_abit_points:
                        #   !!!!!ПОСМОТРЕТЬ ЧЕ МОЖНО СДЕЛАТЬ !!!!!!
                        c3.append((ab, points))
                        lost_equal_abit.append((ab, points))

        c1 = sorted(c1, key=lambda abit: abit[1], reverse=True)
        c2 = sorted(c2, key=lambda abit: abit[1], reverse=True)
        c3 = sorted(c3, key=lambda abit: abit[1], reverse=True)

        for abit in c1:
            if c1.index(abit) < vacant_places_c1:
                passed_students_c1.append(abit)
            if abit in lost_equal_abit and c1.index(abit) == vacant_places_c1 - 1 and abit not in passed_students_c1:
                passed_students_c1.append(abit)
                print("на специальности c1 у вас два абитурианта с одинаковыми баллами ")

        for abit in c2:
            if c2.index(abit) < vacant_places_c2:
                passed_students_c2.append(abit)
            if abit in lost_equal_abit and c2.index(abit) == vacant_places_c2 - 1 and abit not in passed_students_c2:
                passed_students_c2.append(abit)
                print("на специальности c2 у вас два абитурианта с одинаковыми баллами ")

        for abit in c3:
            if c3.index(abit) < vacant_places_c3:
                passed_students_c3.append(abit)
            if abit in lost_equal_abit and c3.index(abit) == vacant_places_c3 - 1 and abit not in passed_students_c3:
                passed_students_c3.append(abit)
                print("на специальности c3 у вас два абитурианта с одинаковыми баллами ")

        vacant["c1"] = passed_students_c1
        vacant["c2"] = passed_students_c2
        vacant["c3"] = passed_students_c3

print(vacant)
