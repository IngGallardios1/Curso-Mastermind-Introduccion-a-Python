import PySimpleGUI as sg

BUTTON_SIZE = (12, 6)
PLAYER_1 = "X"
PLAYER_2 = "O"
WINNER_PLAYS = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]


def rematch(window):
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
    for i in range(9):
        window.Element("-{}-".format(i)).Update(text="")
    window.Element("-WINNER-").Update("")


def exit(event):
    return event == sg.WIN_CLOSED or event == "-Out-"


def layout():
    layout = [[
        sg.Button("", key="-0-", size=BUTTON_SIZE),
        sg.Button("", key="-1-", size=BUTTON_SIZE),
        sg.Button("", key="-2-", size=BUTTON_SIZE)],
        [
            sg.Button("", key="-3-", size=BUTTON_SIZE),
            sg.Button("", key="-4-", size=BUTTON_SIZE),
            sg.Button("", key="-5-", size=BUTTON_SIZE)],
        [
            sg.Button("", key="-6-", size=BUTTON_SIZE),
            sg.Button("", key="-7-", size=BUTTON_SIZE),
            sg.Button("", key="-8-", size=BUTTON_SIZE)],
        [sg.Text("", key="-WINNER-")],
        [sg.Button("Terminado", key="-Out-", size=(19, 2)), sg.Button("Revancha", key="-Remach-", size=(19, 2))]]
    window = sg.Window("Demo", layout)
    return window



def main():
    window = layout()
    current_player = PLAYER_1
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
    while True:
        event, value = window.read()
        if exit(event):
            break
        if event == "-Remach-":
            rematch(window)

        if window.Element(event).ButtonText == "":
            index = int(event.replace("-", ""))
            deck[index] = current_player
            window.Element(event).Update(text=current_player)

            for winner_play in WINNER_PLAYS:
                if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
                    if deck[winner_play[0]] == PLAYER_1:
                        window.Element("-WINNER-").Update("Ha ganado el Jugador 1 -> X")
                    else:
                        window.Element("-WINNER-").Update("Ha ganado el Jugador 2 -> O")

            if current_player == PLAYER_1:
                current_player = PLAYER_2
            else:
                current_player = PLAYER_1
    window.close()


if __name__ == "__main__":
    main()
