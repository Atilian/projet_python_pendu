#!/usr/bin/python3

import random


def bindWord():

    fichier = open("mots.txt", "r")

    lignes = fichier.readlines()

    rand = random.randint(0, 835)

    index = 0

    for ligne in lignes:

        if (index == rand):
            answer = ligne
            break

        index += 1

    return (answer[:-1:])


def bindDisplay(answerBind):

    display = []

    size = len(answerBind) - 1

    while size >= 0:

        display.append("*")

        size -= 1

    return (display)


def listToString(list):

    answer = ""

    for letter in list:

        answer += letter

    return answer


def play():

    vie = 5

    answerBind = bindWord()

    displayBlind = bindDisplay(answerBind)

    print(answerBind)

    while vie > 0:

        letterRep = input("Choice a letter \n\n//> ")

        index = 0

        bool = False

        for letter in answerBind:

            if (letterRep.upper() == letter):

                displayBlind[index] = letter

                bool = True

            index += 1

        if (bool == False):

            vie -= 1

        print(listToString(displayBlind))

        print("\n%d" % (vie))

        if (listToString(displayBlind) == answerBind):
            print("Bravo\n\n")
            break


def main():

    print("*****")

    print("Pendu")

    print("*****\n")

    rep = input("Do you want play Y/N ?\n\n//> ")

    if (rep.upper() == "Y"):

        play()

        while True:

            rep = input("Voulez vous rejouer ? Y/N\n\n//> ")

            if (rep.upper() == "Y"):

                play()
            
            else:

                break


main()
