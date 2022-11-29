# name surname: Omer Faruk AYDIN
# school id: 150210726

def read_puzzle():
    # Take size of 2d matrix as an input from user and create a 2d char list.
    row_x_col = input()
    rxc_input = list(map(int, row_x_col.split(' ')))
    puzzlex = [[] * int(rxc_input[0])] * int(rxc_input[1])

    # Take the rows of matrix as an input and fill in the empty rows of 2d char list with them.
    for i in range(0, int(rxc_input[0])):
        row_input = input()
        rows = list(map(str, row_input.split(' ')))
        puzzlex[i] = rows

    return puzzlex


def read_words():
    # Take number of words as an input and create a list.
    xword = int(input())
    word_list = [""] * xword

    # Take the words as an input and fill in the empty rows of word list.
    for i in range(0, xword):
        word_list[i] = input()

    return word_list


def print_puzzle(puzzle):
    # Print each of the elements of 2d char list.
    j = 0
    for i in puzzle:
        print(*i, sep=" ")
        j = j + 1
    pass


def print_words(words):
    # Print each of the elements of word list with a tab and space between word number and word.
    for i in words:
        print(f"{i[0]}\t {i[2:]}")


def horizontal_search(puzzle, word, puzzle_to_modify):
    x = word[2:]  # Take the word without number.
    rx = ''.join(reversed(x))  # Reverse the word for reverse search.
    s_puzzle = []

    # Convert each line of 2d char list to string and add them to list of strings.
    for line in puzzle:
        hsearch = ""
        for i in line:
            hsearch = hsearch + i
        s_puzzle.append(hsearch)

    g = len(x)
    j = 1
    # Search our word in each line of the list of string.
    for line in s_puzzle:
        if line.find(x) != -1 or line.find(rx) != -1:

            # Right to left search
            if line.find(rx) == -1:
                y = line.find(x)
                print(f"{x} found in horizontal search [{j}][{y + 1}] to [{j}][{y + g}]")
                r = j
                c = y + 1

                # Delete our word from the 2d char list
                while c <= y + g:
                    puzzle_to_modify[r - 1][c - 1] = ' '
                    c = c + 1

            # Left to right search
            if line.find(x) == -1:
                t = line.find(rx)
                print(f"{x} found in horizontal search [{j}][{t + g}] to [{j}][{t + 1}]")
                r = j
                c = t + 1

                # Delete our word from the 2d char list
                while c <= t + g:
                    puzzle_to_modify[r - 1][c - 1] = ' '
                    c = c + 1
        else:
            j = j + 1
    return False, puzzle_to_modify


def vertical_search(puzzle, word, puzzle_to_modify):
    x = word[2:]  # Take the word without number.
    rx = ''.join(reversed(x))  # Reverse the word for reverse search.
    s_puzzle = []
    count = 0

    # Convert each column of 2d char list to string and add them to list of strings.
    for line in puzzle:
        count = count + 1
    n = 0
    for q in range(0, count):
        vsearch = ""
        for line in puzzle:
            vsearch = vsearch + line[n]

        s_puzzle.append(vsearch)
        n = n + 1

    g = len(x)
    j = 1
    # Search our word in each line of the list of string(column of the 2d char list).
    for line in s_puzzle:
        if line.find(x) != -1 or line.find(rx) != -1:

            # Top to bottom search
            if line.find(rx) == -1:
                y = line.find(x)
                print(f"{x} found in vertical search [{y + 1}][{j}] to [{y + g}][{j}]")
                r = y + 1
                c = j

                # Delete our word from the 2d char list
                while r <= y + g:
                    puzzle_to_modify[r - 1][c - 1] = ' '
                    r = r + 1

            # Bottom to top search
            if line.find(x) == -1:
                t = line.find(rx)
                print(f"{x} found in vertical search [{t + g}][{j}] to [{t + 1}][{j}]")
                r = t + 1
                c = j

                # Delete our word from the 2d char list
                while r <= t + g:
                    puzzle_to_modify[r - 1][c - 1] = ' '
                    r = r + 1
        else:
            j = j + 1

    return False, puzzle_to_modify


def diagonal_search(puzzle, word, puzzle_to_modify):
    x = word[2:]  # Take the word without number.
    rx = ''.join(reversed(x))  # Reverse the word for reverse search.
    rowCounter = -1
    rowLength = len(puzzle)
    columnLength=len(puzzle[0])
    # Search our word in each diagonal line of the list of string(diagonal lines of the 2d char list).
    for row in puzzle:
        rowCounter = rowCounter + 1
        columnCounter = -1
        temp = ""
        for cell in row:
            columnCounter = columnCounter + 1
            tempColumnCounter = columnCounter
            tempRowCounter = rowCounter

            # Left to right search
            while tempRowCounter != rowLength and tempColumnCounter != columnLength:
                temp = temp + puzzle[tempRowCounter][tempColumnCounter]
                tempRowCounter = tempRowCounter + 1
                tempColumnCounter = tempColumnCounter + 1

                # Top to bottom search
                if temp == x:
                    print(
                        f"{x} found in diagonal search [{rowCounter + 1}][{columnCounter + 1}] to [{tempRowCounter}][{tempColumnCounter}]")
                    r = rowCounter - 1
                    c = columnCounter - 1
                    # Delete our word from the 2d char list
                    while r <= tempRowCounter - 2 and c <= tempColumnCounter - 2:
                        puzzle_to_modify[r + 1][c + 1] = ' '
                        r = r + 1
                        c = c + 1

                # Bottom to top search
                if temp == rx:
                    print(
                        f"{x} found in diagonal search [{tempRowCounter}][{tempColumnCounter}] to [{rowCounter + 1}][{columnCounter + 1}]")
                    r = rowCounter - 1
                    c = columnCounter - 1
                    # Delete our word from the 2d char list
                    while r <= tempRowCounter - 2 and c <= tempColumnCounter - 2:
                        puzzle_to_modify[r + 1][c + 1] = ' '
                        r = r + 1
                        c = c + 1

            temp = ""
            tempRowCounter = rowCounter
            tempColumnCounter = columnCounter

            # Right to left search
            while (tempColumnCounter >= 0 and tempRowCounter != rowLength):
                temp = temp + puzzle[tempRowCounter][tempColumnCounter]
                tempRowCounter = tempRowCounter + 1
                tempColumnCounter = tempColumnCounter - 1

                # Top to bottom search
                if temp == x:
                    print(
                        f"{x} found in diagonal search [{rowCounter + 1}][{columnCounter + 1}] to [{tempRowCounter}][{tempColumnCounter + 2}]")
                    r = rowCounter - 1
                    c = columnCounter + 1
                    # Delete our word from the 2d char list
                    while r <= tempRowCounter and c >= tempColumnCounter + 2:
                        puzzle_to_modify[r + 1][c - 1] = ' '
                        r = r + 1
                        c = c - 1
                # Bottom to top search
                if temp == rx:
                    print(
                        f"{x} found in diagonal search [{tempRowCounter}][{tempColumnCounter + 2}] to [{rowCounter + 1}][{columnCounter + 1}]")
                    r = rowCounter - 1
                    c = columnCounter + 1
                    # Delete our word from the 2d char list
                    while r <= tempRowCounter and c >= tempColumnCounter + 2:
                        puzzle_to_modify[r + 1][c - 1] = ' '
                        r = r + 1
                        c = c - 1
            temp = ""

    return False, puzzle_to_modify


# Do not change below in any case.
if __name__ == "__main__":
    # puzzle = read_puzzle()
    puzzle = [['A', 'S', 'F', 'G', 'V', 'E', 'D', 'H', 'K', 'L', 'E', 'R', 'D', 'G', 'M'],
          ['K', 'G', 'V', 'A', 'N', 'D', 'E', 'R', 'V', 'A', 'L', 'S', 'S', 'M', 'A'],
          ['A', 'C', 'L', 'M', 'S', 'R', 'I', 'I', 'E', 'E', 'A', 'L', 'E', 'N', 'D'],
          ['Y', 'D', 'G', 'A', 'I', 'S', 'T', 'P', 'T', 'E', 'D', 'T', 'G', 'R', 'J'],
          ['L', 'K', 'J', 'D', 'E', 'A', 'G', 'D', 'O', 'F', 'A', 'H', 'E', 'A', 'U'],
          ['O', 'L', 'E', 'C', 'D', 'A', 'F', 'M', 'O', 'L', 'E', 'K', 'U', 'L', 'S'],
          ['U', 'J', 'L', 'A', 'L', 'V', 'I', 'U', 'A', 'G', 'D', 'I', 'A', 'K', 'K'],
          ['L', 'N', 'E', 'J', 'H', 'H', 'J', 'S', 'M', 'H', 'D', 'I', 'L', 'M', 'O'],
          ['S', 'B', 'M', 'N', 'A', 'I', 'B', 'S', 'K', 'J', 'H', 'U', 'P', 'C', 'V'],
          ['T', 'V', 'E', 'A', 'V', 'D', 'V', 'I', 'J', 'R', 'L', 'K', 'K', 'O', 'A'],
          ['B', 'C', 'N', 'G', 'T', 'R', 'N', 'E', 'O', 'N', 'U', 'A', 'F', 'V', 'L'],
          ['N', 'E', 'T', 'F', 'A', 'O', 'A', 'R', 'O', 'W', 'U', 'E', 'J', 'Z', 'E'],
          ['M', 'W', 'U', 'U', 'Y', 'J', 'M', 'S', 'L', 'T', 'S', 'T', 'U', 'E', 'N'],
          ['M', 'D', 'I', 'I', 'K', 'E', 'E', 'A', 'J', 'S', 'Z', 'J', 'Y', 'G', 'T'],
          ['A', 'S', 'L', 'K', 'L', 'N', 'V', 'K', 'G', 'A', 'C', 'L', 'K', 'J', 'K']]

    # words = read_words()
    words = ["1 KOVALENT","2 VANDERVALS","3 IYONIK","4 HIDROJEN","5 DIPOLDIPOL","6 ELEMENT","7 ATOM","8 MOLEKUL","9 METAL"]

    print_puzzle(puzzle)
    print_words(words)
    puzzle_to_modify = [item.copy() for item in puzzle]

    for word in words:
        found, puzzle_to_modify = horizontal_search(puzzle, word, puzzle_to_modify)
        if not found:
            found, puzzle_to_modify = vertical_search(puzzle, word, puzzle_to_modify)
        if not found:
            found, puzzle_to_modify = diagonal_search(puzzle, word, puzzle_to_modify)

    print_puzzle(puzzle_to_modify)
    
# Sample output:
#      A S F G V E D H K L E R D G M
#      K G V A N D E R V A L S S M A
#      A C L M S R I I E E A L E N D
#      Y D G A I S T P T E D T G R J
#      L K J D E A G D O F A H E A U
#      O L E C D A F M O L E K U L S
#      U J L A L V I U A G D I A K K
#      L N E J H H J S M H D I L M O
#      S B M N A I B S K J H U P C V
#      T V E A V D V I J R L K K O A
#      B C N G T R N E O N U A F V L
#      N E T F A O A R O W U E J Z E
#      M W U U Y J M S L T S T U E N
#      M D I I K E E A J S Z J Y G T
#      A S L K L N V K G A C L K J K
#      1	 KOVALENT
#      2	 VANDERVALS
#      3	 IYONIK
#      4	 HIDROJEN
#      5	 DIPOLDIPOL
#      6	 ELEMENT
#      7	 ATOM
#      8	 MOLEKUL
#      9	 METAL
#      KOVALENT found in vertical search [7][15] to [14][15]
#      VANDERVALS found in horizontal search [2][3] to [2][12]
#      IYONIK found in diagonal search [14][4] to [9][9]
#      HIDROJEN found in vertical search [8][6] to [15][6]
#      DIPOLDIPOL found in diagonal search [2][6] to [11][15]
#      ELEMENT found in vertical search [6][3] to [12][3]
#      ATOM found in diagonal search [10][4] to [13][7]
#      MOLEKUL found in horizontal search [6][8] to [6][14]
#      METAL found in diagonal search [2][14] to [6][10]
#      A S F G V E D H K L E R D G M
#      K G                     S   A
#      A C L M S R   I E E A L   N D
#      Y D G A I S T   T E D   G R J
#      L K J D E A G D   F   H E A U
#      O L   C D A F               S
#      U J   A L V I U A G   I A K  
#      L N   J H   J S M H D   L M  
#      S B   N A   B S   J H U   C  
#      T V     V   V   J R L K K    
#      B C   G       E O N U A F V  
#      N E   F A   A R O W U E J Z  
#      M W U U       S L T S T U E  
#      M D I   K   E A J S Z J Y G  
#      A S L K L   V K G A C L K J K

