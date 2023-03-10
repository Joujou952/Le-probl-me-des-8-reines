# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:14:44 2023

@author: Josep
"""

import random
echec_dim=8

class individu:
    def __init__(self,val=None):
        if val==None:
            self.val=random.sample(range(echec_dim), echec_dim)
        else:
            self.val=val

    def conflict(p1,p2):
        """ return true si la reine à la position p1 est
        en conflit avec la reine en position p2"""
        x1, y1 = p1
        x2, y2 = p2
        # vérifier si les reines sont sur la même colonne ou la même ligne
        if x1 == x2 or y1 == y2:
            return True
        # vérifier si les reines sont sur la même diagonale
        if abs(x1 - x2) == abs(y1 - y2):
            return True
        return False
    
    def fitness(self):
        """ evaluer l'individu c'est conaitre le nombre de conflit"""
        self.nbconflict=0
        for i in range(len(self.val)):
            for j in range(i+1, len(self.val)):
                if(individu.conflict ([i,self.val[i]],[j,self.val[j]])):
                    self.nbconflict=self.nbconflict+1
        return self.nbconflict
    
    def __str__(self):
        """ Retourne une chaîne de caractères représentant l'individu """
        return " ".join(str(x) for x in self.val)
    
def create_rand_pop(count):
    """ Créer une liste de 'count' individus aléatoires """
    pop = []
    for i in range(count):
        ind = individu()
        pop.append(ind)
    return pop   
    
def evaluate(pop):
    """ Évalue la population et retourne une liste des individus triés selon le nombre de conflits"""
    return sorted(pop, key=lambda ind: ind.fitness())
    
def selection(pop, hcount, lcount):
    """ Retourne une sous population avec les “hcount” premiers éléments et les “lcount” derniers éléments de la liste pop"""
    return pop[:hcount] + pop[-lcount:]
    
def croisement(ind1, ind2):
    """ Retourne une liste de deux individus à partir de deux individus ind1 et ind2 (4 premières données de ind1 suivies des 4 dernières de ind2 puis 4 premières données de ind2 suivies des 4 dernières de ind1)"""
    return [individu(ind1.val[:4] + ind2.val[4:]), individu(ind2.val[:4] + ind1.val[4:])]
    
def mutation(ind):
    """ Retourne un individu suite à la mutation de ind. Il s’agit de prendre un indice aléatoire de l’individu et de remplacer la donnée correspondante par une nouvelle valeur aléatoire (entre 0 et 7)."""
    idx = random.randint(0, len(ind.val)-1)
    val = random.randint(0, echec_dim-1)
    new_val = ind.val.copy()
    new_val[idx] = val
    return individu(new_val)    
        
        
def algoloopSimple():
    pop=create_rand_pop(25)
    solutiontrouvee=False
    nbiteration=0
    while not solutiontrouvee:
        print("itération numéro : ",nbiteration)
        nbiteration+=1
        evaluation=evaluate(pop)
        if evaluation[0].fitness()==0:
            solutiontrouvee=True
        else:
            select=selection(evaluation,10,4)
            croises=[]
            for i in range(0,len(select),2):
                croises+=croisement(select[i],select[i+1])
            mutes=[]
            for i in select:
                mutes.append(mutation(i))
            newalea=create_rand_pop(5)
            pop=select[:]+croises[:]+mutes[:]+newalea[:]
    print(evaluation[0])
    
    
    
    
    
    
    
    
    
    
        