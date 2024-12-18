
""" this code was written with love by :
       Khodja walid abdelaziz
       Bafou imad 
       Ouazar rayan 
       Naimi ferras islem
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy.interpolate as spl



#fonction qui interpoles le signal d'entrée et l'echantillonne juste apres 
def interp_ech (t,V,N=1000000) :
    """
    @parm t : signal temps discret 
    @parm V : les valeurs de notre signal
    @parm N : nombre de points souhaité sur le nouveau signal echantillonné , egale à 1 million par defaut 
    @parm on connsidere que 1 million points  réguliérement réparties sur notre un intervalle donnent uunn h suffisament petit
    """
    # On commence par interpolé notre signal d'entrée suivant la méthode des splines cubique
    V_spline=spl.splrep(t, V)
    
    # On déscritise le nouveau axe du temps avec le nouveau nombre dde point 
    t1 = np.linspace(min(t), max(t), N)
    # On échantillonne notre signal 
    V1= spl.splev(t1, V_spline)
    
    #affichage de la tension d'entrée 
    plt.plot(t1,V1,'b', label = "signal d'entrée") 
    plt.grid()
    plt.title("Tension d'entrée")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    
    return t1,V1


#fonction d'appelle qui va utiliser les différentes fonctions deja définies ci dessous  
def appel (t,V):
    """
    @parm t : signal temps discret 
    @parm V : les valeurs de notre signal
    """
    
    m=["euler","runge_kutta","diff_finies"]  #les différentes méthodes utilisées pour la résolution des EDO
    
    print("Veuillez choisir l'ordre du ciruit à étudier comme suit :  \n - 1 : cuircuit du premier ordre \n - 2 : ciruit du second ordre ")
    ordre=int(input("Veuillez choisir 1 ou 2 : "))   
    
    
    print("Veuillez choisir la methode de résolution souhaitée parmis la liste suivante 'runge_kutta' 'euler' 'diff_finies'")
    methode = input("Veuillez choisir une methode : ")
    
    if methode in m :
        if ordre == 1 :  #on a 4 ciruits possible 
            
            print("Veuillez choisir un des ciruits à étudier parmis la liste suivante : 'CR' 'RC' 'RL' 'LR' .")
            circuit=input("Veuillez choisir un circuit : ")
            
            if  circuit == "RC" or circuit == "CR" : #on a besoin d'une resistance et un condensateur 
                R=float(input("Veuillez entrer la valeur de la résistance : "))
                C=float(input("Veuillez entrer la valeur de la capacitée : "))
                
            elif circuit == "LR" or  circuit == "RL" : #on a besoin d'une resistance et une indutance 
                R=float(input("Veuillez entrer la valeur de la résistance : "))
                L=float(input("Veuillez entrer la valeur de l'inductance' : "))
                
            else :
                print("Vous avez choisi un circuit qui n'existe pas dans la liste")
                
        elif ordre == 2 :
                print("Veuillez choisir un des ciruits à étudier parmis la liste suivante : 'RLC' 'RCL' 'CLR'.")
                print("Remarque : la tension est mésurée au bornes du dernier élement, exemple pour 'LCR' c'est aux bornes de R")
                circuit=input("Veuillez choisir un circuit : ")
                
                if circuit == "RLC" or circuit == "RCL" or circuit == "CLR" :  #CLR comme la mercedes CLR qui a fait des ailes durant les 24h du mans
                    R=float(input("Veuillez entrer la valeur de la résistance : "))
                    C=float(input("Veuillez entrer la valeur de la capacitée : "))
                    L=float(input("Veuillez entrer la valeur de l'inductnce : "))
                    
                else :
                    print("Vous avez choisi un circuit qui n'existe pas dans la liste")
                           
        else :
            print("Vous avez choisis un ordre du circuit qui n'existe pas dans la liste")
            
    else :
        print("Vous avez choisis une méthode qui n'existe pas dans la liste")
        
        
    if methode == m[0] : #methode d'euler 
        if circuit == "RC" :
            return euler_RC(t, V, R, C)
        elif circuit == "CR" :
            return euler_CR(t, V, R, C)       
        elif circuit == "RL" :
            return euler_RL(t, V, R, L)            
        elif circuit == "LR" :
            return euler_LR(t, V, R, L)            
        elif circuit == "RLC" :
            return euler_RLC(t, V, R, L, C)
        elif circuit == "CLR" :
            return euler_CLR(t, V, R, L, C)
        elif circuit == "RCL" :
            return euler_RCL(t, V, R, L, C)
    
    elif methode == m[1] : # methode de runge_kutta   
        if circuit == "RC" :
            return runge_kutta_RC(t, V, R, C)           
        elif circuit == "CR" :
            return runge_kutta_CR(t, V, R, C)            
        elif circuit == "RL" :
            return runge_kutta_RL(t, V, R, L)            
        elif circuit == "LR" :
            return runge_kutta_LR(t, V, R, L)            
        elif circuit == "RLC" :
            return runge_kutta_RLC(t, V, R, L, C)
        elif circuit == "CLR" :
            return runge_kutta_CLR(t, V, R, L, C)
        elif circuit == "RCL" :
            return runge_kutta_RCL(t, V, R, L, C)
    
    elif methode == m[2] :  #methode des diff_finies      
        if circuit == "RC" :
            return Diff_Fini_RC(t, V, R, C)           
        elif circuit == "CR" :
            return Diff_Fini_CR(t, V, R, C)            
        elif circuit == "RL" :
            return Diff_Fini_RL(t, V, R, L)            
        elif circuit == "LR" :
            return Diff_Fini_LR(t, V, R, L)            
        elif circuit == "RLC" :
            return Diff_Fini_RLC(t, V, R, L, C)
        elif circuit == "CLR" :
            return Diff_Fini_CLR(t, V, R, L, C)
        elif circuit == "RCL" :
            return Diff_Fini_RCL(t, V, R, L, C)
    else : 
        print("vous avez choisis une methode qui n'éxiste pas dans la liste")


#fonction d'appelle  qui permet de réaliser des systémes complexes (plusieurs filtres en cascade)        
def cascade(t,V) :
    """
    @parm t : signal temps discret 
    @parm V : les valeurs de notre signal
    """
    
    n=int(input("Veuillez choisir le nombre de circuits à mettre en cascade : "))
    v0=V
    for i in range (n) :
        print("\n")
        print("Veuillez configurez le ciruit numero ",i+1," : ")
        v1=appel(t,v0)
        v0=v1 #cette instruction met la sortie du circuit actuel à l'entrée du circuit suivant
        print("La tension afficher est la tension de sortie des",i+1,"filre cascadés")
    return v1   





       
#--------------------------------------------------------------------------------------------------------
#ciruit RC (tenson aux bornes du condensateur)
#equation différentielle 
#RC*(V0)'+V0+Ve

def euler_RC(t, V, R, C):  #methode  d'euler 
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm C la capacité du conndensateur
    """
    
    to=R*C   #constante du temps
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc on a un pas constant 
    CI=0  #condition initiale 
    V0=[CI] 
    
    for i in range(1,len(t)):
        v=V0[i-1]+h*(V[i-1]-V0[i-1])*(1/to)  #v represente y(i)
        V0.append(v)
        
    plt.plot(t,V0,'b', label = "signal de sortie")  #signal de sortie en bleu 
    #plt.plot(t,V,'r' , label = "signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes du condensateur__circuit RC__euler ")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0

def runge_kutta_RC(t, V, R ,C):  #methode de runge_kutta 
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm C la capacité du conndensateur
    """
    
    to=R*C  #constante du temps
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant  
    CI=0  #condition initiale 
    V0=[CI] 
    
    for i in range(1,len(t)):
        k1 = (h/2)*(V[i-1]-V0[i-1])*(1/to)
        k2 =(h/2)*(V[i-1]-2*k1-V0[i-1])*(1/to)
        V0.append(k1+k2+V0[i-1])
    
    plt.plot(t,V0,'b', label="signal de sortie")  #signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes du condensateur__circuit RC__runge kutta")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0
    
def Diff_Fini_RC(t, V, R, C): # methode des Differences Finies
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm C la capacité du conndensateur
    """

    to=R*C   #constante du temps
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant  
    CI=0  #condition initiale 
    V0=[CI,CI]
    
    for i in range(2,len(t)):
        val_new=2*h*(V[i-1]-V0[i-1])/to + V0[i-2] 
        V0.append(val_new)
    
    plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes du condensateur__circuit RC__différences finies")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0
    
  
  
  
  
  
#--------------------------------------------------------------------------------------------------------
#ciruit CR (tenson aux bornes de la resistance)
#equation différentielle 
#(V0)'+V0/rc=(Ve)'

def euler_CR(t,V,R,C):
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm C la capacité du conndensateur
    """
    
    to=R*C #constante du temps
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
    CI=0  #condition initiale 
    V0=[CI,CI] 
    
    for i in range(2,len(t)):
        v=V0[i-1]+h*( (V[i-1]-V[i-2])/h-(V0[i-1])*(1/to) )
        V0.append(v)
    
    plt.plot(t,V0,'b', label="signal de sortie")  #signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes de la resistance__circuit CR__euler")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0

def runge_kutta_CR(t,V,R,C) :
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm C la capacité du conndensateur
    """
    
    to=R*C  #constante du temps
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant  
    CI=0  #condition initiale 
    V0=[CI,CI] 
    
    for i in range(2,len(t)):
        k1 = (h/2)*((V[i-1]-V[i-2])/h-(V0[i-1])*(1/to))
        k2 =( (h/2)*( (V[i-1]-V[i-2])/h -(V0[i-1]+2*k1)*(1/to))) 
        V0.append(k1+k2+V0[i-1])
    
    plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes de la resistance__circuit CR__runge kutta")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0

def Diff_Fini_CR(t, V, R, C): 
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm C la capacité du conndensateur
    """

    to=R*C   #constante du temps 
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
    CI=0  #condition initiale 
    V0=[CI,CI]
    
    for i in range(2,len(t)):
        val=2*h*( (V[i-1]-V[i-2])/h -V0[i-1]/to ) +V0[i-2]
        V0.append(val)

    plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes de la resistance__circuit CR__différeences finies")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0





    
#--------------------------------------------------------------------------------------------------------
#ciruit LR (tenson aux bornes de la resistance)
#equation différentielle 
#V0+(L/R)*(V0)'=Ve

def euler_LR(t, V , R, L) :  
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm L la valeur de l'inductance
    """

    to=L/R #constante du temps 
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
    CI=0  #condition initiale 
    V0=[CI] 
    
    for i in range(1,len(t)):
        v=V0[i-1]+h*(V[i-1]-V0[i-1])*(1/to)
        V0.append(v)

    plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes de la resistance__circuit LR__euler")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0
    
def runge_kutta_LR(t, V, R, L):
    """
   @parm V la tension d'entrée
   @parm t l'axe du temps
   @parm R la valeur de la resistance
   @parm L la valeur de l'inductance
   """
    
    to=L/R   #constante du temps 
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
    CI=0  #condition initiale 
    V0=[CI] 
    
    for i in range(1,len(t)): 
        k1 = (h/2)*(V[i-1]-V0[i-1])*(1/to)
        k2 =((h/2)*(V[i-1]-2*k1-V0[i-1])*(1/to)) 
        V0.append(k1+k2+V0[i-1])

    plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes de la resistance__circuit LR__runge kutta")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0
    
def Diff_Fini_LR(t, V, R, L): 
      """
     @parm V la tension d'entrée
     @parm t l'axe du temps
     @parm R la valeur de la resistance
     @parm L la valeur de l'inductance
     """
     
      to=L/R   #constante du temps
      h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
      CI=0  #condition initiale 
      V0=[CI,CI]    
      
      for i in range(2,len(t)):
          val=2*h*(V[i-1]-V0[i-1])/to +V0[i-2]
          V0.append(val)

      plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
      #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
      plt.grid()
      plt.title("Tension aux bornes de la resistance__circuit LR__différences finies")
      plt.xlabel("temps t")
      plt.ylabel("Tension V")
      plt.legend()
      plt.show()
      return V0
      
      
      
 
    
 
#--------------------------------------------------------------------------------------------------------
 #ciruit RL (tenson aux bornes de l'inductance)
 #equation différentielle 
 #(V0)' = (Ve)' - V0/to
 
def euler_RL(t, V, R, L):
     """
     @parm V la tension d'entrée
     @parm t l'axe du temps
     @parm R la valeur de la resistance
     @parm L la valeur de l'inductance
     """
     
     to=L/R   #constante du temps 
     h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
     CI=0  #condition initiale 
     V0=[CI] 

     for i in range (1,len(t)):
         val = V0[i-1] - h*(1/to)* V0[i-1] + (V[i-1] - V[i-2])
         V0.append(val)

     plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
     #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
     plt.grid()
     plt.title("Tension aux bornes de l'inductance__circuit RL__euler")
     plt.xlabel("temps t")
     plt.ylabel("Tension V")
     plt.legend()
     plt.show()
     return V0
    

def runge_kutta_RL(t,V,R,L) :
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm L la valeur de l'inductance
    """
    
    to=L/R
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant  
    CI=0  #condition initiale 
    V0=[CI,CI] 
    
    for i in range(2,len(t)):
        k1 = (h/2)*((V[i-1]-V[i-2])/h-(V0[i-1])*(1/to))
        k2 =( (h/2)*( (V[i-1]-V[i-2])/h -(V0[i-1]+2*k1)*(1/to))) 
        V0.append(k1+k2+V0[i-1])
    
    plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes de l'inductance__circuit RL__runge kutta")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0

def Diff_Fini_RL(t, V, R, L):  
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm L la valeur de l'inductance
   """
   
    to=L/R   #constante du temps
    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
    CI=0  #condition initiale 
    V0=[CI,CI]
    
    for i in range(2,len(t)):
        # Différenciation centrée    
        val=2*h*( (V[i-1]-V[i-2])/h -V0[i-1]/to ) +V0[i-2]
        V0.append(val)

    plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes de l'inductance__circuit RL__edifférences finies")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0






#--------------------------------------------------------------------------------------------------------
#ciruit RLC (tenson aux bornes du condensateur)
#equation différentielle 
#R*C*(V0)'+L*C*(V0)''+V0 =Ve

def euler_RLC(t, V, R, L, C):
     """
     @parm V la tension d'entrée
     @parm t l'axe du temps
     @parm R la valeur de la resistance
     @parm L la valeur de l'inductance
     @parm C la capacité du conndensateur
    """
     
     h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
     CI=0   #condition initiale 
     V0=[CI] 
     X=[CI]
     
     for i in range (1,len(t)):
         val = V0[i-1] + h*X[i-1]
         xx= X[i-1] + h*(V[i-1]-V0[i-1]-(R*C)*X[i-1])/(L*C)
         V0.append(val)
         X.append(xx)

     plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu 
     #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
     plt.grid()
     plt.title("Tension aux bornes du condensateur__circuit RLC__euler")
     plt.xlabel("temps t")
     plt.ylabel("Tension V")
     plt.legend()
     plt.show()
     return V0
 
def runge_kutta_RLC(t, V, R, L, C):
    """
    @parm V la tension d'entrée
    @parm t l'axe du temps
    @parm R la valeur de la resistance
    @parm L la valeur de l'inductance
    @parm C la capacité du conndensateur
   """

    h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant 
    CI=0  #condition initiale 
    V0=[CI]
    X=[CI]
    
    for i in range(1,len(t)):
        kv1 = (h/2)*(X[i-1])
        kv2 =(h/2)*(X[i-1]) 
              
        kx1 = (h/2)*(V[i-1]-V0[i-1]-(R*C)*X[i-1])/(L*C)
        kx2 = (h/2)*(V[i-1]-V0[i-1]-(R*C)*(X[i-1]+2*kx1))/(L*C)
        
        V0.append(kv1+kv2+V0[i-1])
        X.append(kx1+kx2+X[i-1])

    plt.plot(t,V0,'b', label="signal de sotie")  ##signal sortie en bleu 
    #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge 
    plt.grid()
    plt.title("Tension aux bornes du condensateur__circuit RLC__runge kutta")
    plt.xlabel("temps t")
    plt.ylabel("Tension V")
    plt.legend()
    plt.show()
    return V0

def Diff_Fini_RLC(t, V, R, L,C):
      """
      @parm V la tension d'entrée
      @parm t l'axe du temps
      @parm R la valeur de la resistance
      @parm L la valeur de l'inductance
      @parm C la capacité du conndensateur
      """

      h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
     
      CI=0  #condition initiale
      V0=[CI,CI]
      X=[CI,CI]
     
      for i in range(2,len(t)):   # int(N)
          val=2*h*(X[i-1]) + V0[i-2]
          x= X[i-2] + ((2*h)*(1/L*C))*((V[i-1] - V0[i-1] - (R*C)*(X[i-1])))

          V0.append(val)
          X.append(x)

      plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu
      #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
      plt.grid()
      plt.title("Tension aux bornes du condensateur__circuit RLC__différences finies")
      plt.xlabel("temps t")
      plt.ylabel("Tension V")
      plt.legend()
      plt.show()
      return V0
  
    
    



#--------------------------------------------------------------------------------------------------------
#ciruit CLR (tenson aux bornes de la resistance)
#equation différentielle 
#V0*(1/(R*C))+V0'+(L/R)*V0''=Ve'

def euler_CLR(t, V, R, L, C):
     """
     @parm V la tension d'entrée
     @parm t l'axe du temps
     @parm R la valeur de la resistance
     @parm L la valeur de l'inductance
     @parm C la capacité du conndensateur
     """
     
     h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
     CI=0   #condition initiale
     V0=[CI,CI]
     X=[CI,CI]
     
     for i in range (2,len(t)):
         val = V0[i-1] + h*X[i-1]
         xx= X[i-1] + h*((V[i-1]-V[i-2])/h - (1/(R*C))*V0[i-1] - X[i-1])*(R/L)
         
         V0.append(val)
         X.append(xx)
     
     plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu
     #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
     plt.grid()
     plt.title("Tension aux bornes de la resistance__circuit CLR__euler")
     plt.xlabel("temps t")
     plt.ylabel("Tension V")
     plt.legend()
     plt.show()
     return V0

def runge_kutta_CLR(t, V, R, L, C):
     """
     @parm V la tension d'entrée
     @parm t l'axe du temps
     @parm R la valeur de la resistance
     @parm L la valeur de l'inductance
     @parm C la capacité du conndensateur
     """

     h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
     CI=0  #condition initiale
     V0=[CI,CI]
     X=[CI,CI]
     
     for i in range(2,len(t)):
         kv1 = (h/2)*(X[i-1])
         kv2 =(h/2)*(X[i-1])
               
         kx1 = (h/2)*((V[i-1]-V[i-2])/h-(1/(R*C))*V0[i-1]-X[i-1])*(R/L)
         kx2 = (h/2)*((V[i-1]-V[i-2])/h-(1/(R*C))*V0[i-1]-X[i-1]-2*kx1)*(R/L)
         
         V0.append(kv1+kv2+V0[i-1])
         X.append(kx1+kx2+X[i-1])

     plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu
     #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
     plt.grid()
     plt.title("Tension aux bornes de la resistance__circuit CLR__runge kutta")
     plt.xlabel("temps t")
     plt.ylabel("Tension V")
     plt.legend()
     plt.show()
     return V0
 
def Diff_Fini_CLR(t, V, R, L,C):
      """
      @parm V la tension d'entrée
      @parm t l'axe du temps
      @parm R la valeur de la resistance
      @parm L la valeur de l'inductance
      @parm C la capacité du conndensateur
      """

      h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
      CI=0  #condition initiale
      V0=[CI,CI]
      X=[CI,CI]
     
      for i in range(2,len(t)):   # int(N)
          val=2*h*(X[i-1]) + V0[i-2]
          x= X[i-2] + 2*h*(((V[i-1]-V[i-2])/h)*(R/L) -(1/L*C)* (V0[i-1]) - (R/L)*X[i-1])

          V0.append(val)
          X.append(x)

      plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu
      #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
      plt.grid()
      plt.title("Tension aux bornes de la resistance__circuit CLR__différences finies")
      plt.xlabel("temps t")
      plt.ylabel("Tension V")
      plt.legend()
      plt.show()
      return V0






#--------------------------------------------------------------------------------------------------------
#ciruit RCL (tenson aux bornes de l'inductance)
#equation différentielle 
#V0*(1/(L*C))+V0'*(R/L)+V0''=Ve''  

def euler_RCL(t, V, R, L, C):
     """
     @parm V la tension d'entrée
     @parm t l'axe du temps
     @parm R la valeur de la resistance
     @parm L la valeur de l'inductance
     @parm C la capacité du conndensateur
     """
     
     h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
     CI=0   #condition initiale
     V0=[CI,CI,CI]
     X=[CI,CI,CI]
     
     for i in range (3,len(t)):
         val = V0[i-1] + h*X[i-1]
         xx= X[i-1] + h*((V[i-1]-2*V[i-2]+V[i-3])/(h**2) - (1/(L*C))*V0[i-1] - (R/L)*X[i-1])
         
         V0.append(val)
         X.append(xx)
     
     plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu
     #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
     plt.grid()
     plt.title("Tension aux bornes de l'inductance__circuit RCL__euler")
     plt.xlabel("temps t")
     plt.ylabel("Tension V")
     plt.legend()
     plt.show()
     return V0
 
def runge_kutta_RCL(t, V, R, L, C):
     """
     @parm V la tension d'entrée
     @parm t l'axe du temps
     @parm R la valeur de la resistance
     @parm L la valeur de l'inductance
     @parm C la capacité du conndensateur
     """

     h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
     CI=0  #condition initiale
     V0=[CI,CI,CI]
     X=[CI,CI,CI]
     
     for i in range(3,len(t)):
         kv1 = (h/2)*(X[i-1])
         kv2 =(h/2)*(X[i-1])
               
         kx1 = (h/2)*((V[i-1]-2*V[i-2]+V[i-3])/(h**2) - (1/(L*C))*V0[i-1]-(R/L)*X[i-1])
         kx2 = (h/2)*((V[i-1]-2*V[i-2]+V[i-3])/(h**2) - (1/(L*C))*V0[i-1]-(R/L)*(X[i-1]+2*kx1))
         
         V0.append(kv1+kv2+V0[i-1])
         X.append(kx1+kx2+X[i-1])

     plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu
     #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
     plt.grid()
     plt.title("Tension aux bornes de la resistance__circuit RCL__runge kutta")
     plt.xlabel("temps t")
     plt.ylabel("Tension V")
     plt.legend()
     plt.show()
     return V0
 
def Diff_Fini_RCL(t, V, R, L,C):
      """
      @parm V la tension d'entrée
      @parm t l'axe du temps
      @parm R la valeur de la resistance
      @parm L la valeur de l'inductance
      @parm C la capacité du conndensateur
      """

      h=t[1]-t[0]  #on suppose qu'on travail sur un echantillonnage regulier donc un pas constant
      CI=0  #condition initiale
      V0=[CI,CI]
      X=[CI,CI]
     
      for i in range(2,len(t)):   # int(N)
          val=2*h*(X[i-1]) + V0[i-2]
          x= X[i-2] + 2*h*((V[i-1]-2*V[i-2]+V[i-3])/(h**2) -(1/L*C)* (V0[i-1]) - (R/L)*X[i-1])

          V0.append(val)
          X.append(x)

      plt.plot(t,V0,'b', label="signal de sortie")  ##signal sortie en bleu
      #plt.plot(t,V,'r' , label="signal d'entrée'")  #signal d'entrée en rouge
      plt.grid()
      plt.title("Tension aux bornes de l'inductance__circuit RCL__différences finies")
      plt.xlabel("temps t")
      plt.ylabel("Tension V")
      plt.legend()
      plt.show()
      return V0
    