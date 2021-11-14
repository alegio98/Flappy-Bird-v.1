#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-   per compilare fn + F5
import pygame
import random

pygame.init()

sfondo = pygame.image.load('/home/alessandro/Scrivania/Gioco Python/sfondo.png')
uccello = pygame.image.load('/home/alessandro/Scrivania/Gioco Python/uccello.png')
base = pygame.image.load('/home/alessandro/Scrivania/Gioco Python/base.png')
gameover = pygame.image.load('/home/alessandro/Scrivania/Gioco Python/gameover.png')
tubo_giu = pygame.image.load('/home/alessandro/Scrivania/Gioco Python/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True) ##imagine da specchiare flip verticale messo a true mentre rotazione orizzontale messa a False

SCHERMO = pygame.display.set_mode((288,512)) #variabile schermo
FPS = 50  #frame per second
vel_avanzamento=3
#font = pygame.font.SysFont('Segoe UI', 50 , bold=True)

class tubi_classe:
   def __init__(self):
      self.x= 300
      self.y= random.randint(-75,150)
   def avanza_e_disegna(self):
      self.x -= vel_avanzamento
      SCHERMO.blit(tubo_giu, (self.x,self.y+210))
      SCHERMO.blit(tubo_su, (self.x,self.y-210))
   def collisione(self , uccello , uccellox , uccelloy): #fra uccello e tubi , se vi sarà una collisione allora siamo dei loser
      tolleranza = 5
      uccello_lato_dx = uccellox+ uccello.get_width() - tolleranza  #per avere la posizione del lato destro dell'immagine ci sommo la posizione dell'immagine + la sua lunghezza
      uccello_lato_sx = uccellox + tolleranza
      tubi_lato_dx = self.x + tubo_giu.get_width()
      tubi_lato_sx = self.x
      uccello_lato_giu = uccelloy + uccello.get_height()-tolleranza
      uccello_lato_su = uccelloy + tolleranza
      tubi_lato_su= self.y+110
      tubi_lato_giu= self.y+210
      if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
         if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
            hai_perso()
   def fra_i_tubi(self,uccello, uccellox):
         tolleranza = 5
         uccello_lato_dx = uccellox+ uccello.get_width() - tolleranza  #per avere la posizione del lato destro dell'immagine ci sommo la posizione dell'immagine + la sua lunghezza
         uccello_lato_sx = uccellox + tolleranza
         tubi_lato_dx = self.x + tubo_giu.get_width()
         tubi_lato_sx = self.x
         if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            return True



def disegna_oggetti():
   SCHERMO.blit(sfondo,(0,0))
   SCHERMO.blit(uccello,(uccellox,uccelloy))
   SCHERMO.blit(base,(basex,400))
   for t in tubi:   #disegno ogni tubo contenuto nella lista tubi
      t.avanza_e_disegna()
#   punti_render = FONT.render(str(punti),1,(255,255,255)) #stringa da convertire in immagine , 1 = antialiasing , colore in rgb
#   SCHERMO.blit(punti_render, (144,0))

def aggiorna():   #aggiornare lo schermo
   pygame.display.update()
   pygame.time.Clock().tick(FPS)

def hai_perso():
   SCHERMO.blit(gameover,(50,180))
   aggiorna()
   ricominciamo= False
   while not ricominciamo:
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            inizializza()
            ricominciamo= True
         if event.type== pygame.QUIT:
            pygame.quit()



def inizializza():
   global uccellox , uccelloy , uccellovely , basex
   global tubi
   uccellox , uccelloy = 60, 150
   uccellovely = 0
   basex=0
   tubi=[]
   tubi.append(tubi_classe())  #cosi ho creato un tubo e aggiunto alla lista tubi
   fra_i_tubi= False
inizializza()

while True:
    basex -= vel_avanzamento
    if basex < -45: basex = 0  #scorre verso sinistra la base
    uccellovely +=1
    uccelloy += uccellovely
    for event in pygame.event.get():
      if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):  # con la funzione pygame.event.get() possiamo leggere tutti gli eventi che si verificano se l'evento(dato dalla variabile type è uguale a pygame.KEYDOWN significa che è stato generato da una pressione sulla tastiera e inoltre se l'evento  dato dalla freccetta in su  allora l'uccello deve dare una botta con le ali)
         uccellovely= -10
      if(event.type == pygame.QUIT):   # se clicco chiudi l'app si chiude
         pygame.quit()
      if uccelloy > 380:
         hai_perso()
    if tubi[-1].x < 150: tubi.append(tubi_classe())  #quando utlimo tubo raggiunge l'uccello allora crea un altro tubo , posizione x del tubo controllata
    for t in tubi:
       t.collisione(uccello, uccellox , uccelloy)
    disegna_oggetti()
    aggiorna()
