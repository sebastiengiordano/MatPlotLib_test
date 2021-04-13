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


Graph 1
    30 000 points * 11 courbes:
    30 000 points * 6 courbes:
Graph 2
    30 000 points * 6 courbes:
        Test add + display:
            DISPLAY_DATA_LIMIT = 2000
            STORED_DATA_LIMIT = 10000
            DATA_TO_REMOVED = 6000
            DISPLAY_REFRESH = 0.125
        Temps après     1000    lignes: 242.83 s
        Temps après     2000    lignes: 247.82 s


        Test add + display:
            DISPLAY_DATA_LIMIT = 1000
            STORED_DATA_LIMIT = 10000
            DATA_TO_REMOVED = STORED_DATA_LIMIT - (2 * DISPLAY_DATA_LIMIT)
            DISPLAY_REFRESH = 0.125
        Temps après     1000    lignes: 238.33 s
        Temps après     2000    lignes: 231.64 s


        Test add + display:
            DISPLAY_DATA_LIMIT = 3000
            STORED_DATA_LIMIT = 10000
            DATA_TO_REMOVED = STORED_DATA_LIMIT - (2 * DISPLAY_DATA_LIMIT)
            DISPLAY_REFRESH = 0.125
            Temps après     1000    lignes: 230.42 s
            Temps après     2000    lignes: 237.76 s
            Temps après     3000    lignes: 229.65 s
            Temps après     4000    lignes: 237.48 s
            Temps après     5000    lignes: 236.58 s
            Temps après     6000    lignes: 233.99 s
            Temps après     7000    lignes: 234.74 s
            Temps après     8000    lignes: 236.79 s
            Temps après     9000    lignes: 238.97 s


        Test add + display:
            DISPLAY_DATA_LIMIT = 3000
            STORED_DATA_LIMIT = 10000
            DATA_TO_REMOVED = STORED_DATA_LIMIT - (2 * DISPLAY_DATA_LIMIT)
            DISPLAY_REFRESH = 0.500
                Temps après     1000    lignes: 3.69 s
                Temps après     2000    lignes: 3.53 s
                Temps après     3000    lignes: 4.97 s
                Temps après     4000    lignes: 3.54 s
                Temps après     5000    lignes: 3.54 s
                Temps après     6000    lignes: 3.56 s
                Temps après     7000    lignes: 3.38 s
                Temps après     8000    lignes: 3.75 s
                Temps après     9000    lignes: 3.43 s
                Temps après     10000   lignes: 3.76 s
                Temps après     11000   lignes: 3.30 s
                Temps après     12000   lignes: 3.56 s
                Temps après     13000   lignes: 3.57 s
                Temps après     14000   lignes: 3.93 s
                Temps après     15000   lignes: 3.54 s
                Temps après     16000   lignes: 3.57 s
                Temps après     17000   lignes: 3.59 s
                Temps après     18000   lignes: 3.59 s
                Temps après     19000   lignes: 3.40 s
                Temps après     20000   lignes: 3.49 s
                Temps après     21000   lignes: 3.84 s
                Temps après     22000   lignes: 3.66 s
                Temps après     23000   lignes: 3.58 s
                Temps après     24000   lignes: 3.54 s
                Temps après     25000   lignes: 3.57 s
                Temps après     26000   lignes: 3.62 s
                Temps après     27000   lignes: 3.55 s
                Temps après     28000   lignes: 3.60 s
                Temps après     29000   lignes: 3.40 s
                Durée du test: 108.82 s
                Durée ajout data: 108.82 s






        Test add data then display (no limit):
            DISPLAY_DATA_LIMIT > data to display
            STORED_DATA_LIMIT  > data to display
        Durée ajout data: 71.85 s
        Temps affichage: 0.51 s

        Test add data+drop then display (no limit):
            DISPLAY_DATA_LIMIT > data to display
            STORED_DATA_LIMIT = 10000
            DATA_TO_REMOVED = 6000
        Durée ajout data: 57.11 s
        Temps affichage: 0.47 s

        Test add data+drop then display:
            DISPLAY_DATA_LIMIT = 1000
            STORED_DATA_LIMIT = 10000
            DATA_TO_REMOVED = STORED_DATA_LIMIT - (2 * DISPLAY_DATA_LIMIT)
        Durée ajout data: 57.50 s
        Temps affichage: 0.47 s


        