def hangman(word) :

    wrong = 0
    stages = ["",
        "_______       ",
        "|             ",
        "|      |      ",
        "|      O      ",
        "|     /|\     ",
        "|     / \     ",
        "|             "
        ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    msg = "1文字を予想してね"
    
    while wrong < len(stages) - 1 :
        print("\n")
        c = input(msg)
        if c in rletters :
            cind = rletters.index(c)
            board[cind] = c
            rletters[cind] = '$'
        else :
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ちです")
            print(" ".join(board))
            win = True
            break
        
    if not win :
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

def select_word(path) :
    import random
    with open(path, 'r', encoding='utf-8') as f :
        words = f.readlines()
    
    return words[random.randint(0,len(words) - 1)].rstrip().lower()

import os
path = os.path.join(os.path.dirname(__file__), 'word list.txt')

hangman(select_word(path))
        
