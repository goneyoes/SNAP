import random
class Card:
    def __init__(self, name, cost, power, action=None, outer_action=None):
        self.name = name
        self.cost = cost
        self.power = power
        self.action = action
        self.outer_action = outer_action

NICO= Card("Nico M",1,2, None, NicoLogic)
def NicoLogic:n = random.randrange(len(NicoA))
    NICO.action = n
    NicoA.pop(n)
def cc: self.card.loction.pop(self.card)
    drawcard
    drawcard
def Lo: None
def move: #Nightmare Fuel
def Dem: self.card.power = 6
def Nico2: last_card.power = last_card.power*2
def add2: self.card.power = self.card.power + 2
def Nclone: HAND.append(self.card)
'''
In the actual game, each location has a special ability chosen from a HUGE pool of locations
Lo is actyally very powerful becuase some of these location abilities can make combos not function correctly, and Lo
has the ability to reroll a location. However, for our purposes we are removing the location aspect for several reasons
#1 its really hard to code
#2 with good play, these locations should have a less than 2% impact on the total winrate, which is just not worth the effort
#3 the opponent has the ability to play specfic cards which will GUARANTEE a combo will not work, which is something to worry about
#4 the purpose of this simulation is "in a vaccuum" so it wouldn't even make sense
'''

CARNAGE = Card("Carnage",2,2, Cdestroy)
def Cdestroy(): 
MAGIK = Card("Magik",3,2, Turn7)
def Turn7(): TURNCOUNT=7
VENOM = Card("Venom",3,3,Vdestroy)
def Vdestroy(): 
SHURI = Card("Shuri", 4,3, None, doubler)
def doubler(): self.card.power = self.card.power*2
STICK = Card("Stick",4,3, None, lend)
def lend():  self.card.power = self.card.power + STICK.power
ABS = Card("Absorbing Man",4,5, None, Acopy)
def Acopy(): self.location.pop(ABS)   self.location.append
#add last_card to this location and set its power to ABS's power
SSPIDERMAN = Card("SSpiderman",4,7, SScopy)#"Add this card's power to your lowest cost card here and use its action again, then remove this card")
def SScopy():
BP = Card("Black Panther",5,5, Panther2)
def Panther2(): self.power = self.power*2
NIMROD = Card("Nimrod",5,6)
#Card doesn't have a method???
ZOLA = Card("Arnim Zola",6,0, Zclone)
def Zclone(): i = random.randrange(len(self.Location))
removed_card = cards.pop(i)
#Zola, SSpiderman, ABS, and both destroys need work
    
TASKMASTER = Card("Taskmaster",6,0, tasks)
def tasks(): self.power = last_card.power

DECK = [NICO, CARNAGE, MAGIK, VENOM, SHURI, STICK, ABS, SSPIDERMAN, BP, NIMROD, ZOLA, TASKMASTER]
HAND = []
L1 = []
L2 = []
L3 = []
Playlist = []
last_card = Playlist[-1]
TURN = 1
TURNCOUNT = 6
def playstart

def playcard(self, card, location):
    energy -= self.card.energy
     if energy<0
        print("energy error")
        return
    Playlist.append(self.card): 
    self.location.append(self.card)
    if len(self.location)>4
        print("Location error")
        return
    if last_card = SHURI:
    if last_card = STICK:
    if last_card = NICO:
    #print locations
    
# location part should require an input and failsafe    
    
        
def turnstart(self,number):
    drawcard
    energy = TURN
    
    if TURN>TURNCOUNT:
        endcon=1
        
def endturn
    
def drawcard():
    i = random.randrange(len(DECK))
    HAND.append(i)
    DECK.pop(i)
    if HAND#contains Nico, run NicoLogic
    # also deck order is not fixed, it should shuffle at gamestart
'''
technically hand cannot contain more than 7 cards, so drawcard should fail in that case
however, for this type of deck, it is basically impossible to hit that number becuase you can always
strategically burn a cardplay to avoid this scenaio. A smart burned card is always possible and shoudl never
affect the actual combo probabilty. This is not coded in becuase you need human esque logic to know which cards to burn
'''
def gamestart(self)
    endcon=0
    TURNCOUNT=6
    TURN = 1
    DECK = [NICO, CARNAGE, MAGIK, VENOM, SHURI, STICK, ABS, SSPIDERMAN, BP, NIMROD, ZOLA, TASKMASTER]
    drawcard
    drawcard
    drawcard
    del L1[:]
    del L2[:]
    del L3[:]
    NicoA = [cc, Lo, move, Dem, add2, Nclone, Panther2]
    turnstart
    
"""while endcon=0
    gamestart
"""

print(Playlist)
print #locations and powers

def SnapSim
    games += 1
    gamestart
'''
    If Nico has cc AND Hand contains carnage, shuri, or magik(and maybe stick) play Nico(if in hand)
    If Nico has Nico2 AND (DECK or Hand) has Absorbing man and zola and SSpriderman play Nico(if in hand)
    else endturn(1)
    
    If Nico, Absorbing man, zola, and SSpiderman are in HAND
    then play carnage. if unable to play carnage, endturn
    If Nico has cc AND Hand contains carnage, shuri, or magik(and maybe stick) play Nico(if in hand)
    If hand contains Venom AND Nimrod(and not magik or stick) and Nico has Dem, play Nico(if in hand)
    If Nico has Lo, Add2, Nico2, or Nclone, Play nico(if in hand)
    (this option should be secondary to the very first if)
    if Nico has move AND Magik or Shuri are in hand(this is so incredibly complicated i might just make move have no ability due to venom/arnim zola shennigans)
    else endturn(2)
    
    If Nico has Nico2, play Nico
    If Nico has cc AND (the deck still has all the good cards) AND carnage is in hand, play Nico AND carnage
    If Nico has cc AND (the deck still has all the good cards) AND magik is in hand, play Nico
    If magik is in hand, play magik(unless Venom and shuri and nimrod are in hand)
    If unable to play magik, play Venom(unless carnage is in hand without shuri)
    If unable to play magik or venom, AND Nico is in hand with(
    
'''