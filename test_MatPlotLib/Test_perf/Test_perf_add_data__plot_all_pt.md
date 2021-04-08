30 000 points * 6 courbes:

    Append method
    Durée ajout data: 94.88 s
    Temps affichage: 0.17 s


    Concact method:
    Durée ajout data: 89.12 s
    Temps affichage: 0.16 s

    Concact method + drop:
        DISPLAY_DATA_LIMIT = 2000
        STORED_DATA_LIMIT = 10000
        DATA_TO_REMOVED = STORED_DATA_LIMIT - DISPLAY_DATA_LIMIT * 2


30 000 points * 11 courbes:
    Append method
    Durée ajout data: 139.86 s
    Temps affichage: 0.20 s

    Concact method:
    Durée ajout data: 134.49 s
    Temps affichage: 0.20 s

    Concact method + drop:
        DISPLAY_DATA_LIMIT = 2000
        STORED_DATA_LIMIT = 10000
        DATA_TO_REMOVED = STORED_DATA_LIMIT - DISPLAY_DATA_LIMIT * 2
    Durée ajout data: 85.77 s
    Temps affichage: 0.15 s     (2000 pts)


        DISPLAY_DATA_LIMIT = 2000
        STORED_DATA_LIMIT = 10000
        DATA_TO_REMOVED = STORED_DATA_LIMIT - DISPLAY_DATA_LIMIT * 3
    Durée ajout data: 87.71 s
    Temps affichage: 0.16 s


    concat method + new_DataFrame:
        Durée ajout data: 88.41 s
        Temps affichage: 0.16 s
