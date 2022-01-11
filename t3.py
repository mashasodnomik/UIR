abiturients = [("ab1", [273, 1, 3, 2]), ("ab2", [242, 2, 1, 3]), ("ab3", [256, 1, 3, 2]), ("ab4", [302, 3, 2, 1])]


def StableMatching(list_of_abiturients, num_of_faculties):

    for i in range(num_of_faculties):
        for ab in list_of_abiturients:

