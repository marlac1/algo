# python v 3.9
import random

#handle inputs errors : type errors and probability checked
#PB : doesn't go to the except block
def analyseinputs(p1, p2):
    try:
        if (isinstance(p1, (int, float)) and isinstance(p2, (int, float))):
            try:
                if p1 + p2 == 1:
                    return True
            except:
                print("Check your input probabilities")
    except:
        print("Wrong input types")

"""def analyseinputs(p1, p2):
    if (isinstance(p1, (int, float)) and isinstance(p2, (int, float))):
        if p1 + p2 == 1:
            return True
        print("Check your input probabilities")
    print("Wrong input types")"""

#defines a limit to a set : 25 points with 2 ecart margin
#returns True if the set is finished
#returns False is the set goes on
def endofset(ptsone, ptstwo):
    if (ptsone >= 25 and ptsone - ptstwo >= 2) or (ptstwo >= 25 and ptstwo - ptsone >= 2):
        return True
    return False

#simulates one whole set
#play probability game with python random.random() tool to count team points
def winoneset(p1, p2):
    #team one and team two points
    ptsone = ptstwo = 0
    while not endofset(ptsone, ptstwo):
        if random.random() * p1 > random.random() * p2:
            ptsone += 1
        else:
            ptstwo += 1
    #display scores
    print(f"{ptsone}-{ptstwo}")
    return ptsone, ptstwo

#simulates of a whole match
#inputs are two probabilities
#output displays all scores
def winsets(p1, p2):
    #team one and team two points
    ptsone = ptstwo = 0
    #counters of sets for team one and team two
    cptone = cpttwo = 1

    #number of sets
    numset = 1
    #check inputs
    if analyseinputs(p1, p2):
        print("0-0")
        #max 5 sets for a match
        while numset <= 5:
            ptsone, ptstwo = winoneset(p1, p2)
            #number of won sets for each team : at 3, end of the match
            #ICI IMPLEMENTER FONCTION APPELEE A NUMSET = 2 QUI COMPARE SCORE DES DEUX
            #FACTORISER ?
            if ptsone > ptstwo:
                if cptone == 3:
                    break #ou numset = 4 ??
                cptone += 1
            elif ptstwo > ptsone:
                if cpttwo == 3:
                    break
                cpttwo += 1
            else:#equal
                continue
            numset += 1
        # display the scores for each set
        return True
#winsets("bla", "oui")
if __name__ == "__main__":
# __name-- = variable spéciale automatiquement remplie à l'exécution
# Dans le module principal, sa valeur sera égale à __main__.
#Le test if (__name__ == __main__) permet de faire la distinction entre les deux cas.
# Cette condition est utilisée pour développer un module pouvant à la fois être exécuté directement
# mais aussi être importé par un autre module pour apporter ses fonctions.
#Cette condition permet donc de regrouper les instructions que l'on veut utiliser
#dans le cas d'une exécution directe du module.
    #TESTS
    #winsets(1.0, 0.0)
    #winsets(0.7, 0.3)
    winsets(000000000, "oui")
