class Board:
    def init_board(self):
        Board_Actual = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 
        return Board_Actual

    def display_board(self, Act_Board):
        #print("\033c", end="")
        print (Act_Board[0],"|",Act_Board[1], "|", Act_Board[2])
        print ("---------")
        print (Act_Board[3],"|",Act_Board[4], "|", Act_Board[5])
        print ("---------")
        print (Act_Board[6],"|",Act_Board[7], "|", Act_Board[8])

