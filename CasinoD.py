import pandas as pd
import random



def premier_tirage(deck):
    tirage = random.sample(deck, 5)
    for i in tirage:
        deck.remove(i)
    return tirage, deck



def choix_carte(chosen_cards):
    new_chosen_cards = []
    count = 0
    for card in chosen_cards:
        #if count < 4:
        print('Voulez vous garder la carte(y\n)? : ', card)
        user_answer = input()
        if user_answer =='y':
            #count +* 1
            new_chosen_cards.append(card)
    return new_chosen_cards


def deuxieme_tirage(jeu, deck):
    nb_carte = len(jeu)
    carte_a_tirer = 5 - nb_carte
    nouvelle_carte = random.sample(deck, carte_a_tirer)
    for i in nouvelle_carte:
        jeu.append(i)
    return jeu

def machine():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    tirage1, deck = premier_tirage(deck)
    print(tirage1)
    jeu = choix_carte(tirage1)
    tirage_final = deuxieme_tirage(jeu, deck)
    print(tirage_final)
    return tirage_final

def decompose_jeu(tirage):
    dic = {}
    keys = [1,2,3,4,5]
    valeur = []
    couleur = []
    for i,k in zip(tirage,keys):
        dic[k] = i.split('-')
    for key in dic.keys():
        valeur.append(dic[key][0])
        couleur.append(dic[key][1])
    return valeur, couleur

def convert_carte(liste):
    for e,i in zip(liste, range(0,5)):
        try:
            liste[i] = int(e)
        except:
            if e == 'J':
                liste[i] = 11
            elif e == 'Q':
                liste[i] = 12
            elif e == 'K':
                liste[i] = 13
            elif e == 'A':
                liste[i] = 1
            else:
                continue
    return liste

def quinte_flush_royale(tirage):
    valeur_gagnante = ['10','J','Q','K','A']
    valeur, couleur = decompose_jeu(tirage)
    if sorted(valeur_gagnante) == sorted(valeur) and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def quinte_flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def carre(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [1,4]:
        return True
    else:
        return False

def full(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [2,3]:
        return True
    else:
        return False

def flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    if couleur.count(couleur[0])  == 5:
        return True
    else:
        return False
    

def quinte(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 or valeur == [1, 10, 11, 12, 13,]:
        return True
    else:
        return False

def brelan(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 1, 3]:
        return True
    else:
        return False

def double_paire(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 2, 2]:
        return True
    else:
        return False

def paire(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 4 and sorted(count) == [1, 1, 1, 2]:
        return True
    else:
        return False

def gain(tirage_final, mise):
    if quinte_flush_royale(tirage_final) == True:
        g = mise*250
        resultat = "Quinte Flush Royale !! Vous gagnez " + str(g) + "euros ! Félicitaions!!"
        return g, resultat
    elif quinte_flush(tirage_final) == True:
        g = mise*50
        resultat = "Quinte Flush !! Vous gagnez" + str(g) + "euros ! Félicitations !!"
        return g, resultat
    elif carre(tirage_final) == True:
        g = mise*25
        resultat = "Carré !! Vous gagnez" + str(g) + "euros ! Félicitations !!"
        return g, resultat
    elif full(tirage_final) == True:
        g = mise*9
        resultat = "Full ! Vous gagnez" + str(g) + "euros ! Félicitations !"
        return g, resultat
    elif flush(tirage_final) == True:
        g = mise*6
        resultat = "Flush ! Vous gagnez" + str(g) + "euros ! Félicitations !"
        return g, resultat
    elif quinte(tirage_final) == True:
        g = mise*4
        resultat = "Quinte ! Vous gagnez" + str(g) + "euros ! Félicitations !"
        return g, resultat
    elif brelan(tirage_final) == True:
        g = mise*3
        resultat = "Brelan ! Vous gagnez" + str(g) + "euros ! Félicitations !"
        return g, resultat
    elif double_paire(tirage_final) == True:
        g = mise*2
        resultat = "Double paire !! Vous gagnez" + str(g) + "euros ! Félicitations !"
        return g, resultat
    elif paire(tirage_final) == True:
        g = mise*1
        resultat = "Paire ! Vous gagnez" + str(g) + "euros ! Félicitations !"
        return g, resultat
    else:
        g = 0
        resultat = "Perdu ! Réessaye Bro :D"
        return g, resultat

def partie(mise, bankroll):
    main = machine()
    g, resultat = gain(main, mise)
    bankroll = bankroll - mise
    bankroll += g
    return resultat, bankroll

def video_poker():
    bankroll = int(input("Bank"))
    mise_joueur = int(input("Faites vos jeux: "))
    
    while bankroll - mise_joueur >= 0:
        resultat, bankroll = partie(mise_joueur, bankroll)
        print(resultat)
        print("Bank: " + str(bankroll))
        if bankroll == 0:
            print("Game Over")
            break
        else:
            mise_joueur = int(input("Faites vos jeu:"))
            if bankroll - mise_joueur < 0:
                print("Mise trop elevée")
                mise_joueur = int(input("Faites vos jeu: "))

video_poker()