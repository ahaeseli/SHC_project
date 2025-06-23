# -*- coding: utf-8 -*-
"""
Created on Fr Mar 28 15:07:16 2014

@author: Dr. Dennis Roskosch
"""
'''
Benötigt Stoffdatenprogramm Fluid_CP.py
Erstellung von T-s-Diagrammen einfacher Wärmepumpen- und Kälteprozesse (Reinstoffe)
Zustandsänderungen: Verdichten, Kondensieren, Drosseln, Verdampfen
Zustände:
z1: Verdichtereintritt
z2: Kondensatoreintritt
z3: Expansionsventileintritt
z4: Verdampfereintritt

Syntax Zustand: z=[T, p, v, u, h, s, x]
Einheitensystem: von state siehe Programm FLuid_CP.py
'''

from pylab import *
sys.path.insert(0,'/Users/lliebl/Desktop/MyProject/Teaching/SHCT/CoolProp') # path to the Fluid_CP
import Fluid_CP as Fl
 

def Ts(z1,z2,z3,z4,fluid,Eh):

    Eh_=Eh
    figure(figsize=(12,8))
    info=Fl.get_fluid_info(fluid,Eh_)
    
    #Isentroper Verdichterwirkungsgrad
    h2_s=Fl.state(['p','s'],[z2["p"],z1["s"]],fluid,Eh_)["h"]
    eta_s=(h2_s-z1["h"])/(z2["h"]-z1["h"])
    
    
    
 
    # Berechnung und plot der Siede- bzw. Taulinie
    T=linspace(z4["T"]-15.,info["T_crit"]-.11,200)
    s_siede=zeros(200,float)
    s_tau=zeros(200,float)
    
    for i in range(200):
        s_siede[i]=Fl.state(['T','x'],[T[i],0],fluid,Eh_)["s"]
        s_tau[i]=Fl.state(['T','x'],[T[i],1],fluid,Eh_)["s"]
    s_krit=Fl.state(['T','p'],[.99*info["T_crit"],.99*info["p_crit"]],fluid,Eh_)["s"]
    
    s=zeros(401,float)
    T_all=zeros(401,float)

    for z in range(401):
        if z<200:
            s[z]=s_siede[z]
            T_all[z]=T[z]
        elif z==200:
            s[z]=s_krit
            T_all[z]=info["T_crit"]
        else:
            s[z]=s_tau[400-z]
            T_all[z]=T[400-z]
    T_all[200]=.5*(T_all[199]+T_all[201])
    s[200]=.5*(s[199]+s[201])
    plot(s,T_all, color='k',linewidth=4.)
    
   
    # Verbindungen der Zustände
    ### von 1 nach 2
    p12=linspace(z1["p"],z2["p"],20)
    T12=zeros(20)
    s12=zeros(20)
    for i6 in range(20):
        h2_s=Fl.state(['p','s'],[p12[i6],z1["s"]],fluid,Eh_)["h"]
        h2=(h2_s-z1["h"])/eta_s+z1["h"]
        zw=Fl.state(['p','h'],[p12[i6],h2],fluid,Eh_)
        T12[i6],s12[i6]=zw["T"], zw["s"]
    plot(s12,T12,color='b',linewidth=3)    
   
    ##### von 2 nach 3
    if z2["p"]>=info["p_crit"]:
        T23=zeros(100,float)
        s23=linspace(z2["s"],z3["s"],100)
        for u in range(100):
            T23[u]=Fl.state(["p","s"],[z2["p"],s23[u]],fluid,Eh_)["T"]
        plot(s23,T23,color='b',linewidth=3)
    else:
        if z2["x"]==998 and z3["x"]==-998:
           
            s2x=Fl.state(['p','x'],[z2["p"],1],fluid,Eh_)["s"]
            s2xx=Fl.state(['p','x'],[z2["p"],0],fluid,Eh_)["s"]
            T2x=Fl.state(['p','x'],[z2["p"],0],fluid,Eh_)["T"]
            s22x=linspace(z2["s"],s2x,10)
            T22x=zeros(10,float)        
            for g in range(10):
                T22x[g]=Fl.state(['p','s'],[z2["p"],s22x[g]],fluid,Eh_)["T"]
            
            T2x2xx=zeros(20)
            s2x2xx=linspace(s2x,s2xx,20)
            for i3 in range(20):
                T2x2xx[i3]=Fl.state(['p','s'],[z2["p"],s2x2xx[i3]],fluid,Eh_)["T"]
            s2xx3=[s2xx,z3["s"]]
            T2xx3=[T2x,z3["T"]]
            plot(s22x,T22x,color='b',linewidth=3)   
            plot(s2x2xx,T2x2xx,color='b',linewidth=3)    
            plot(s2xx3,T2xx3,color='b',linewidth=3)  
        
        elif z2["x"]==998 and (z3["x"]<=1 and z3["x"]>=0):
        
            s2x=Fl.state(['p','x'],[z2["p"],1],fluid,Eh_)["s"]
            T2x=Fl.state(['p','x'],[z2["p"],1],fluid,Eh_)["T"]         
            s22x=linspace(z2["s"],s2x,10)
            T22x=zeros(10,float)        
            for g in range(10):
                T22x[g]=Fl.state(['p','s'],[z2["p"],s22x[g]],fluid,Eh_)["T"] 
            T2x3=zeros(20)
            s2x3=linspace(s2x,z3["s"],20)
            for i3 in range(20):
                T2x3[i3]=Fl.state(['p','s'],[z2["p"],s2x3[i3]],fluid,Eh_)["T"]

            plot(s22x,T22x,color='b',linewidth=3)
            plot(s2x3,T2x3,color='b',linewidth=3)  
            
        elif (z2["x"]<=1 and z2["x"]>=0) and z3["x"]==-998:
            zw2=Fl.state(['p','x'],[z2["p"],0],fluid,Eh_)
            s2xx,T2xx=zw2["s"], zw2["T"]
            
            T22xx=zeros(20)
            s22xx=linspace(z2["s"],s2xx,20)
            for i3 in range(20):
                T22xx[i3]=Fl.state(['p','s'],[z2["p"],s22xx[i3]],fluid,Eh_)["T"]
            
            s2xx3=[s2xx,z3["s"]]
            T2xx3=[T2xx,z3["T"]]
            plot(s22xx,T22xx,color='b',linewidth=3)    
            plot(s2xx3,T2xx3,color='b',linewidth=3)
        else:
            T23=zeros(20)
            s23=linspace(z2["s"],z3["s"],20)
            for i3 in range(20):
                T23[i3]=Fl.state(['p','s'],[z2["p"],s23[i3]],fluid,Eh_)["T"]

            plot(s23,T23,color='b',linewidth=3)

########### von 3 nach 4 #####################     
    p34=linspace(z3["p"],z4["p"],20)
    s34=zeros(20)

    T34=zeros(20,float)
    for u2 in range(20):
        zw3=Fl.state(['h','p'],[z3["h"],p34[u2]],fluid,Eh_)
        T34[u2],s34[u2]=zw3["T"], zw3["s"]
    plot(s34,T34,color='b',linewidth=3)

######### von 4 nach 1 ####################    
    if (z1["x"]<=1 and z1["x"]>=0):
        s41=linspace(z4["s"],z1["s"],20)
        T41=zeros(20)
        for i4 in range(20):
            T41[i4]=Fl.state(['p','s'],[z1["p"],s41[i4]],fluid,Eh_)["T"]
        plot(s41,T41,color='b',linewidth=3)  
    elif z1["x"]==998:
        s4x=Fl.state(['p','x'],[z1["p"],1],fluid,Eh_)["s"]  
        
        s44x=linspace(z4["s"],s4x,20)
        T44x=zeros(20)
        for i4 in range(20):
            T44x[i4]=Fl.state(['p','s'],[z1["p"],s44x[i4]],fluid,Eh_)["T"]
        
        s4x1=linspace(s4x,z1["s"],10)
        T4x1=zeros(10,float)        
        for g in range(10):
            T4x1[g]=Fl.state(['p','s'],[z1["p"],s4x1[g]],fluid,Eh_)["T"]  
        plot(s44x,T44x,color='b',linewidth=3)
        plot(s4x1,T4x1,color='b',linewidth=3)
        


    text(z1["s"]+.05,z1["T"]-10.,'1',fontsize=16,color='b')
    text(z2["s"],z2["T"]+5.,'2',fontsize=16,color='b')
    text(z3["s"],z3["T"]+5.,'3',fontsize=16,color='b')
    text(z4["s"],z4["T"]-10.,'4',fontsize=16,color='b')

    plot(z1["s"],z1["T"],'bo',ms=9)    
    plot(z2["s"],z2["T"],'bo',ms=9)   
    plot(z3["s"],z3["T"],'bo',ms=9)   
    plot(z4["s"],z4["T"],'bo',ms=9)   
    
    if Eh_=="SI":
        xlabel('specific entropie [J/kg/K]',color='k',fontsize=18)
        ylabel('temperature [K]',color='k',fontsize=18)
    
     # Output unit correction
    if Eh_=="CBar" or Eh_=="CKPa":
        xlabel('specific entropie [kJ/kg/K]',color='k',fontsize=18)
        ylabel('temperatur [C]',color='k',fontsize=18)
     


    xticks(fontsize=14)
    yticks(fontsize=14)
    
    grid()
    
    show()
    return 
  
############################################################################################################
  
def Th(z1,z2,z3,z4,Tsink,Tsource,fluid,Eh):

    Eh_=Eh
    figure(figsize=(12,8))
    info=Fl.get_fluid_info(fluid,Eh_)

    
    #Isentroper Verdichterwirkungsgrad
    h2_s=Fl.state(['p','s'],[z2["p"],z1["s"]],fluid,Eh_)["h"]
    eta_s=(h2_s-z1["h"])/(z2["h"]-z1["h"])

    # Berechnung und plot der Siede- bzw. Taulinie
    T=linspace(z4["T"]-15.,info["T_crit"]-.11,200)
    h_siede=zeros(200,float)
    h_tau=zeros(200,float)
    
    for i in range(200):
        h_siede[i]=Fl.state(['T','x'],[T[i],0],fluid,Eh_)["h"]
        h_tau[i]=Fl.state(['T','x'],[T[i],1],fluid,Eh_)["h"]
    h_krit=Fl.state(['T','p'],[.99*info["T_crit"],.99*info["p_crit"]],fluid,Eh_)["h"]
    
    h=zeros(401,float)
    T_all=zeros(401,float)

    for z in range(401):
        if z<200:
            h[z]=h_siede[z]
            T_all[z]=T[z]
        elif z==200:
            h[z]=h_krit
            T_all[z]=info["T_crit"]
        else:
            h[z]=h_tau[400-z]
            T_all[z]=T[400-z]
    T_all[200]=.5*(T_all[199]+T_all[201])
    h[200]=.5*(h[199]+h[201])

    plot(h,T_all, color='k',linewidth=4.)
    
   
    # Verbindungen der Zustände
    ### von 1 nach 2
    p12=linspace(z1["p"],z2["p"],20)
    T12=zeros(20)
    h12=zeros(20)
    for i6 in range(20):
        h2_s=Fl.state(['p','s'],[p12[i6],z1["s"]],fluid,Eh_)["h"]
        h12[i6]=(h2_s-z1["h"])/eta_s+z1["h"]
        T12[i6]=Fl.state(['p','h'],[p12[i6],h12[i6]],fluid,Eh_)["T"]
    plot(h12,T12,color='b',linewidth=3)    
   
    ##### von 2 nach 3
    if z2["p"]>info["p_crit"]:
        T23=zeros(100,float)
        h23=linspace(z2["h"],z3["h"],100)
        for u in range(100):
            T23[u]=Fl.state(['p','h'],[z2["p"],h23[u]],fluid,Eh_)["T"]
        plot(h23,T23,color='b',linewidth=3)
    else:
        if z2["x"]==998 and z3["x"]==-998:
           
            h2x=Fl.state(['p','x'],[z2["p"],1],fluid,Eh_)["h"]
            h2xx=Fl.state(['p','x'],[z2["p"],0],fluid,Eh_)["h"]
            T2x=Fl.state(['p','x'],[z2["p"],0],fluid,Eh_)["T"]
            h22x=linspace(z2["h"],h2x,10)
            T22x=zeros(10,float)        
            for g in range(10):
                T22x[g]=Fl.state(['p','h'],[z2["p"],h22x[g]],fluid,Eh_)["T"]
            
            T2x2xx=zeros(20)
            h2x2xx=linspace(h2x,h2xx,20)
            for i3 in range(20):
                T2x2xx[i3]=Fl.state(['p','h'],[z2["p"],h2x2xx[i3]],fluid,Eh_)["T"]
            h2xx3=[h2xx,z3["h"]]
            T2xx3=[T2x,z3["T"]]
            plot(h22x,T22x,color='b',linewidth=3)   
            plot(h2x2xx,T2x2xx,color='b',linewidth=3)    
            plot(h2xx3,T2xx3,color='b',linewidth=3)  
        
        elif z2["x"]==998 and (z3["x"]<=1 and z3["x"]>=0):
        
            h2x=Fl.state(['p','x'],[z2["p"],1],fluid,Eh_)["h"]
            T2x=Fl.state(['p','x'],[z2["p"],1],fluid,Eh_)["T"]         
            h22x=linspace(z2["h"],h2x,10)
            T22x=zeros(10,float)        
            for g in range(10):
                T22x[g]=Fl.state(['p','h'],[z2["p"],h22x[g]],fluid,Eh_)["T"] 
            T2x3=zeros(20)
            h2x3=linspace(h2x,z3["h"],20)
            for i3 in range(20):
                T2x3[i3]=Fl.state(['p','h'],[z2["p"],h2x3[i3]],fluid,Eh_)["T"]

            plot(h22x,T22x,color='b',linewidth=3)
            plot(h2x3,T2x3,color='b',linewidth=3)  
            
        elif (z2["x"]<=1 and z2["x"]>=0) and z3["x"]==-998:
            zw1=Fl.state(['p','x'],[z2["p"],0],fluid,Eh_)
            h2xx,T2xx=zw1["h"],zw1["T"]
            
            T22xx=zeros(20)
            h22xx=linspace(z2["h"],h2xx,20)
            for i3 in range(20):
                T22xx[i3]=Fl.state(['p','h'],[z2["p"],h22xx[i3]],fluid,Eh_)["T"]
            
            h2xx3=[h2xx,z3["h"]]
            T2xx3=[T2xx,z3["T"]]
            plot(h22xx,T22xx,color='b',linewidth=3)    
            plot(h2xx3,T2xx3,color='b',linewidth=3)
        else:
            T23=zeros(20)
            h23=linspace(z2["h"],z3["h"],20)
            for i3 in range(20):
                T23[i3]=Fl.state(['p','h'],[z2["p"],h23[i3]],fluid,Eh_)["T"]

            plot(h23,T23,color='b',linewidth=3)

########### von 3 nach 4 #####################     
       
    p34=linspace(z3["p"],z4["p"],20)
    h34=zeros(20)+z3["h"]
    T34=zeros(20,float)
    for u2 in range(20):
        T34[u2]=Fl.state(['h','p'],[z3["h"],p34[u2]],fluid,Eh_)["T"]
    plot(h34,T34,color='b',linewidth=3)

######### von 4 nach 1 ####################    
    
    if (z1["x"]<=1 and z1["x"]>=0):
        h41=linspace(z4["h"],z1["h"],20)
        T41=zeros(20)
        for i4 in range(20):
            T41[i4]=Fl.state(['p','h'],[z1["p"],h41[i4]],fluid,Eh_)["T"]
        plot(h41,T41,color='b',linewidth=3)  
    elif z1["x"]==998:
        h4x=Fl.state(['p','x'],[z1["p"],1],fluid,Eh_)["h"]  
        
        h44x=linspace(z4["h"],h4x,20)
        T44x=zeros(20)
        for i4 in range(20):
            T44x[i4]=Fl.state(['p','h'],[z1["p"],h44x[i4]],fluid,Eh_)["T"]
        
        h4x1=linspace(h4x,z1["h"],10)
        T4x1=zeros(10,float)        
        for g in range(10):
            T4x1[g]=Fl.state(['p','h'],[z1["p"],h4x1[g]],fluid,Eh_)["T"]  
        plot(h44x,T44x,color='b',linewidth=3)
        plot(h4x1,T4x1,color='b',linewidth=3)
        

    #Wärmequelle / -semke
    plot([z1["h"],z4["h"]],Tsource,linewidth=2.5, color="g")
    plot([z3["h"],z2["h"]],Tsink,linewidth=2.5, color="g")
    

  
    text(z1["h"]+.05,z1["T"]-10.,'1',fontsize=16,color='b')
    text(z2["h"],z2["T"]+5.,'2',fontsize=16,color='b')
    text(z3["h"],z3["T"]+5.,'3',fontsize=16,color='b')
    text(z4["h"],z4["T"]-10.,'4',fontsize=16,color='b')

    plot(z1["h"],z1["T"],'bo',ms=9)    
    plot(z2["h"],z2["T"],'bo',ms=9)   
    plot(z3["h"],z3["T"],'bo',ms=9)   
    plot(z4["h"],z4["T"],'bo',ms=9)   
    
    if Eh_=="SI":
        xlabel('specific enthalpy [J/kg]',color='k',fontsize=18)
        ylabel('temperature [K]',color='k',fontsize=18)
    
     # Output unit correction
    if Eh_=="CBar" or Eh_=="CKPa":
        xlabel('specific enthalpy [kJ/kg]',color='k',fontsize=18)
        ylabel('temperature [C]',color='k',fontsize=18)
  
    
 

    xticks(fontsize=14)
    yticks(fontsize=14)
    
    grid()
    
    show()
    return    
  
    
if __name__=="__main__":
    
    fluid="CO2"
    Eh="CBar"
    dtk=273.15
    dp=1e5
    
    z1_x1=Fl.state(["T","x"],[0.,1.],fluid,Eh)
    z1=Fl.state(["T","p"],[10.,z1_x1["p"]],fluid,Eh)   
    #z2_x1=Fl.state(["T","x"],[35.+dtk,1.],fluid,Eh) 
    #z2=Fl.state(["p","s"],[z2_x1["p"],z1["s"]],fluid,Eh)
    #z3=Fl.state(["x","p"],[.2,z2_x1["p"]],fluid,Eh)
    z2=Fl.state(["p","s"],[100.,z1["s"]],fluid,Eh)
    z3=Fl.state(["T","p"],[20.,100.],fluid,Eh)
    
    z4=Fl.state(["p","h"],[z1["p"],z3["h"]],fluid,Eh)
    Ts(z1,z2,z3,z4,fluid,Eh)
    #Th(z1,z2,z3,z4,[45.,100.],[20.,20.],fluid,Eh)
 