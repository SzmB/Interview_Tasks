import glob
from datetime import datetime

required_start = datetime.fromisoformat('2022-06-01 11:00:00')
duration_minutes = 30
how_many_necessary = 2


# program
def select_function(e):
    return e[1]


filenames = glob.glob("*.txt")
list_of_peoples = []

for filename in filenames:
    file = open(filename, 'r')

    lines = file.readlines()
    for line in lines:
        split_line = line.replace('\n', '').split(' - ')
        start_time = datetime.fromisoformat(split_line[0])
        end_time = datetime.fromisoformat(split_line[1])
        list_of_peoples.append((filename, start_time, end_time))

persons_availability = []
for filename in filenames:
    sorted_dates = []
    for person in list_of_peoples:
        if person[0] == filename:
            sorted_dates.append(person)
    sorted_dates.sort(key=select_function)

    available_times = []
    for i in range(0, len(sorted_dates)):
        if i == 0:
            available_times.append((filename, None, sorted_dates[i][1]))
        elif i == len(sorted_dates)-1:
            available_times.append((filename, sorted_dates[i][2], None))
        elif (sorted_dates[i+1][1] - sorted_dates[i][2]).total_seconds() >= duration_minutes*60:
            available_times.append((filename, sorted_dates[i][2], sorted_dates[i+1][1]))

    persons_availability.append(available_times)

available_persons = 0
for perso in persons_availability:
    print(perso)
# tutaj szukanie wspolnych przerw
# persons_availability -> lista przerw dla wszystkich [imie.txt, start przerwy, koniec przerwy]

# iteruj po nazwach osob
for person_name in filenames:
    # iteruj po liscie dostepnosci dla wszystkich osob
    for person in persons_availability:
        # iteruj po dostepnosci dla konkretnej osoby
        for availability in person:
            # wybierz przerwy dla pierwszej osoby
            if availability[0] == person_name:
                # zeruj ile osob jest dostepnych
                how_many_available = 0
                search_time_start = None

                # iteruj po nazwach osob
                for person2_name in filenames:
                    # nie sprawdzaj tej samej osoby co w petli wyzej
                    if person2_name != person_name:
                        # iteruj po liscie dostepnosci dla wszystkich osob
                        for person2 in persons_availability:
                            # iteruj po dostepnosci dla konkretnej osoby
                            for availability2 in person2:
                                # wybierz przerwy dla drugiej osoby
                                if availability2[0] == person2_name:
                                    # wybierz przerwy dla godzin o znanych zakresach
                                    if availability[1] is not None and availability2[2] is not None and availability[2] is not None and availability2[1] is not None:
                                        if (availability2[2] - availability[1]).total_seconds() >= duration_minutes*60 and (availability[2] - availability2[1]).total_seconds() >= duration_minutes*60:
                                            how_many_available = how_many_available + 1
                                            if availability[1] > availability2[1]:
                                                search_time_start = availability[1]
                                            else:
                                                search_time_start = availability2[1]

                                            if how_many_available == how_many_necessary:
                                                # znaleziono przerwe o wymaganej dlugosci
                                                print(search_time_start)
                                                exit()
                                    # wybierz przerwy dla godzin jesli nie znane jest start time zakresu przerwy
                                    # wybierz przerwy dla godzin jesli nie znane jest end time
                                    # wybierz przerwy dla godzin jesli nie znaje jest start time i end time