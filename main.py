import sys, pyinputplus,random,time,os


win_dict = {}


def displaying_results():
    print("Statystyki wygranych: ")
    x = 1
    os.remove("Statystyki.txt")
    #zapisywanie wynikow w pliku
    for k , v in win_dict.items():
        with open("Statystyki.txt","a") as plik:
            plik.write(f"{x}.{k} - {v}")
        #wyswietlanie wynikow w konsoli
        print(f"{x}.{k} - {v}")
        x += 1
    print()


def do_you_want_play_again():
    do_you_play_again = pyinputplus.inputNum("Jeśli chcesz zagrać ponownie naciśnij 1."
                                  "Aby wyjść naciśnij inną cyfrę/liczbę ;): ")

    if do_you_play_again == 1:
        main()
    else:
        sys.exit(0)


def computer_selection_function(the_board):
    possible_choices = ["top-L","top-M","top-R","mid-L","mid-M","mid-R","down-L","down-M","down-R"]
    computer_choice = "mid-M"

    while the_board[computer_choice] == "X" or the_board[computer_choice] == "O":
        computer_choice = random.choice(possible_choices)

    return computer_choice


def game_selection():
    how_many_players = pyinputplus.inputChoice(["1", "2"],prompt="Wpisz dla ilu graczy ma wystartować gra (1 lub 2): ")

    if how_many_players == "2":
        return True
    else:
        return False


def pattern_printing():
    print("Oto wzór pozycji do wyboru: \n")
    print("top-L","|","top-M","|","top-R")
    print("------+-------+------")
    print("mid-L", "|", "mid-M", "|", "mid-R")
    print("------+-------+------")
    print("down-L|down-M |down-R\n")


def squares_printing(board):
    print("",board["top-L"],"|",board["top-M"],"|", board["top-R"])
    print("---+---+---")
    print("",board["mid-L"], "|", board["mid-M"], "|", board["mid-R"])
    print("---+---+---")
    print("",board["down-L"], "|", board["down-M"], "|", board["down-R"])


def winning_check(board, player_tokken):
    positions_won = [
        #wiersze
        ("top-L", "top-M", "top-R"),
        ("mid-L", "mid-M", "mid-R"),
        ("down-L", "down-M", "down-R"),
        # kolumny
        ("top-L", "mid-L", "down-L"),
        ("top-M", "mid-M", "down-M"),
        ("top-R", "mid-R", "down-R"),
        #przekatne
        ("top-L", "mid-M", "down-R"),
        ("down-L", "mid-M", "top-R"),
    ]
    # Sprawdzanie czy 3 pozycje wygrane mają ten sam znak
    for pos_1, pos_2, pos_3 in positions_won:
        if board[pos_1] == player_tokken and board[pos_2] == player_tokken and board[pos_3] == player_tokken:
            return True
    return False



def main():
    print("Witam w grze kółko i krzyżyk. Statystyki bedą zapisywane "
          "w 'cwd' dopóki program nie zakończy działania ;)\n")

    the_board = {"top-L": " ", "top-M": " ", "top-R": " ",
                 "mid-L": " ", "mid-M": " ", "mid-R": " ",
                 "down-L": " ", "down-M": " ", "down-R": " "}
    # wybieranie czy grasz z komputerem, czy z innym graczem
    if game_selection():
        name1 = input("Gracz nr 1 wpisz swoje imię: ")
        name2 = input("Gracz nr 2 wpisz swoje imię: ")
        pattern_printing()
        turn = "X"
        for i in range(9):
            #sprawdzanie, ktore imie gra w tej turze
            if turn == "X":
                which_name = name1
            else:
                which_name = name2
            #wybór pola w którym chcesz postawić znak
            square = pyinputplus.inputChoice(["top-L", "top-M","top-R","mid-L", "mid-M", "mid-R","down-L", "down-M", "down-R"],
                                            prompt=f"{which_name} w którym polu chcesz postawić {turn}: ")
            #ponowny wybór jeśli wybrane pole jest juz zajęte
            while the_board[square] == "X" or the_board[square] == "O":
                print("Niestety, to pole jest już zajęte, spróbuj jeszcze raz!\n")
                square = pyinputplus.inputChoice(["top-L", "top-M","top-R","mid-L", "mid-M", "mid-R","down-L", "down-M", "down-R"],
                                                prompt=f"W którym polu chcesz postawić {turn}: ")

            the_board[square] = turn
            squares_printing(the_board)
            if winning_check(the_board, turn):
                if turn == "X":
                    print(f"Wygrywa {name1}!")
                    # Tworzenie pary dla słownika, jesli klucz nie istnieje
                    win_dict.setdefault(name1, 0)
                    # Zwiększanie wartości istniejącego klucza o 1
                    if name1 in win_dict.keys():
                        win_dict[name1] = win_dict.get(name1) + 1

                else:
                    print(f"Wygrawa {name2}!")
                    # Tworzenie pary dla słownika, jesli klucz nie istnieje
                    win_dict.setdefault(name2, 0)
                    # Zwiększanie wartości istniejącego klucza o 1
                    if name2 in win_dict.keys():
                        win_dict[name2] = win_dict.get(name2) + 1

                displaying_results()
                do_you_want_play_again()
                sys.exit(0)
            #Zmiana znaku na drugi
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        # Wykonywane w przypadku remisu
        print("Remis")
        do_you_want_play_again()

    else:
        name = input("Wprowadź swoje imię: ")
        pattern_printing()
        turn = "X"
        if turn == "X":
            for i in range(9):
                # Wybór pola w którym chcesz postawić znak
                square = pyinputplus.inputChoice(["top-L", "top-M","top-R","mid-L", "mid-M", "mid-R","down-L", "down-M", "down-R"],
                                                prompt=f"W którym polu chcesz postawić {turn}: ")
                # Ponowny wybór jeśli wybrane pole jest juz zajęte
                while the_board[square] == "X" or the_board[square] == "O":
                    print("Niestety, to pole jest już zajęte, spróbuj jeszcze raz!\n")
                    square = pyinputplus.inputChoice(["top-L", "top-M","top-R","mid-L", "mid-M", "mid-R","down-L", "down-M", "down-R"],
                                                    prompt=f"W którym polu chcesz postawić {turn}: ")

                the_board[square] = turn
                squares_printing(the_board)
                if winning_check(the_board, turn):
                    print(f"Wygrywa gracz o imieniu {name}!")
                    # Tworzenie pary dla słownika, jesli klucz nie istnieje
                    win_dict.setdefault(name, 0)
                    # Zwiększanie wartości istniejącego klucza o 1
                    if name in win_dict.keys():
                        win_dict[name] = win_dict.get(name) + 1

                    displaying_results()
                    do_you_want_play_again()
                # Gra komputera/zmiana tur
                if turn == "X":
                    turn = "O"
                    print("----------------")
                    print("\nRuch komputera...")
                    time.sleep(2)
                    computer_selection = computer_selection_function(the_board)
                    the_board[computer_selection] = turn
                    squares_printing(the_board)
                    if winning_check(the_board, turn):
                        print(f"Wygrywa Komputer!")
                        # Tworzenie pary dla słownika, jesli klucz("komputer") nie istnieje
                        win_dict.setdefault("Komputer", 0)
                        # Zwiększanie wartości istniejącego klucza o 1
                        if "Komputer" in win_dict.keys():
                            win_dict["Komputer"] = win_dict.get("Komputer") + 1

                        displaying_results()
                        do_you_want_play_again()
                    turn = "X"
                else:
                    turn = "X"
            # Wykonywane w przypadku remisu
            print("Remis")
            do_you_want_play_again()

main()
