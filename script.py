class Pokemon():
  def __init__(self,name,level,element_type, max_health, current_health, knocked_out):
    self.name=name
    self.level=level
    self.element_type=element_type
    self.max_health=max_health
    self.current_health=current_health
    self.knocked_out=knocked_out
  
  def __repr__(self):
    return "These are the stats for "+self.name


  #create method for losing health
  def lose_health(self, health_lost):
    self.health_lost=health_lost
    #subtract health lost
    self.current_health-=self.health_lost
    #if necessary, knock out pokemon
    if self.current_health<=0:
      self.current_health=0
      self.knocked_out=True
      return self.name+ " is knocked out! Current health = 0."
    else:
      return self.name+ "'s health is at "+str(self.current_health) +" out of "+ str(self.max_health) +"."

  #create method for gaining health
  def gain_health(self, health_gain):
    self.health_gain=health_gain
    if self.knocked_out is True:
      return self.name + " must be revived before it can gain health."

    #add health
    self.current_health+=self.health_gain
    if self.current_health>self.max_health:
      self.current_health=self.max_health
    return self.name+ "'s health is at "+str(self.current_health) +" out of "+ str(self.max_health) +"."

#create a function that revives a pokemon at half strength
  def revive(self):
    if self.knocked_out is False:
      return "Cannot revive "+self.name+ " as it is not knocked out!"
    else: 
      self.knocked_out=False
      self.current_health=int(self.max_health/2)
      return self.name+ " has been revived! Its health is at "+str(self.current_health) +" out of "+ str(self.max_health) +"."

  def full_revive(self):
    if self.knocked_out is False:
      return "Cannot revive "+self.name+ " as it is not knocked out!"
    else: 
      self.knocked_out=False
      self.current_health=self.max_health
      return self.name+ " has been completely revived! Its health is at "+str(self.current_health) +" out of "+ str(self.max_health) +"."

  #define attack method. Our pokemon only have 3 types- grass, fire, and water. If the attacking 
  def attack(self, other_pokemon):
    element_list=["water", "fire", "grass"]
    #make sure the attacking pokemon is not knocked out!
    if self.knocked_out is True:
      return self.name + " cannot attack when it is knocked out!"
    #make sure the other pokemon is not knocked out!
    elif other_pokemon.knocked_out is True:
      return "You can't beat a dead horse! "+other_pokemon.name + " is already knocked out!"
    elif self.element_type not in element_list or other_pokemon.element_type not in element_list:
      return "Not a valid Pokemon type"
    elif self.element_type==other_pokemon.element_type:
      damage=self.level
    #if self is grass vs fire 
    elif (self.element_type=="grass") and (other_pokemon.element_type=="fire"):
      damage=int(self.level/2)
    #if self is fire vs water
    elif (self.element_type=="fire") and (other_pokemon.element_type=="grass"):
      damage=int(self.level/2)
    #if self is water vs grass
    elif (self.element_type=="water") and (other_pokemon.element_type=="grass"):
      damage=int(self.level/2)
    else:
      damage=2*self.level
    if damage>=other_pokemon.current_health:
      damage=other_pokemon.current_health
      other_pokemon.lose_health(damage)
      other_pokemon.knocked_out=True
      return self.name + " attacked "+other_pokemon.name+ " and did "+str(damage)+ " damage, which knocked it out!"
    else:
      other_pokemon.lose_health(damage)
      return self.name + " attacked "+other_pokemon.name+ " and did "+str(damage)+ " damage! " +other_pokemon.name+ " now has a current health value of "+ str(other_pokemon.current_health)
      



#tests for the class methods of adding health, subtracting health, full and total revival
Kobra=Pokemon("Kobra",4,"fire",101,50,False)
#print(Kobra.lose_health(40))
#print(Kobra.gain_health(5))
#print(Kobra.gain_health(1000))
#print(Kobra.lose_health(200))
#print(Kobra.gain_health(10))
#print(Kobra.revive())
#print(Kobra.lose_health(200))
#print(Kobra.full_revive())

#test attack method. First create 4 pokemon of grass, fire, water and ghost type.
Kobra=Pokemon("Kobra",4,"fire",101,50,False)
Gengar=Pokemon("Gengar",50, "ghost", 100,100,False)
Oddish=Pokemon("Oddish", 9, "grass", 500,500, False  )
Vulpix=Pokemon("Vulpix", 22, "fire", 750,750,False)
Psyduck=Pokemon("Psyduck", 30, "water",99,99,False)
Mew=Pokemon("Mew",100,"water",1000,0,True)

#print(Mew.attack(Gengar))
#print(Gengar.attack(Mew))
#print(Mew.revive())
#print(Mew.attack(Gengar))
#print(Gengar.attack(Mew))
#print(Psyduck.attack(Mew))
#print(Mew.attack(Psyduck))
#print(Psyduck.attack(Oddish))
#print(Psyduck.attack(Vulpix))
#print(Oddish.attack(Psyduck))
#print(Oddish.attack(Vulpix))

#make a trainer class- trainer has a name, can have 6 pokemon(poke_team),can have several potions, and a current active pokemon (a number)
class Trainer():
  def __init__(self,name,poke_team,num_potion,current_pokemon=0):
    self.name=name
    self.poke_team=poke_team
    self.num_potion=num_potion
    self.current_pokemon=current_pokemon

  #make trainer methods for using potion, attack another trainer, and switch pokemon.
  def use_potion(self):
    if self.num_potion<=0:
      return self.name+ " does not have any potions to use"
    else:
      self.num_potion-=1
      #fix script if do not heal full 30 points
      cur_poke=self.poke_team[self.current_pokemon]
      health_gap=cur_poke.max_health-cur_poke.current_health
      if health_gap>=30:
        cur_poke.gain_health(30)
        
        return self.name + " used a potion on "+cur_poke.name + " and it gained 30 health. Current health is {health}.".format(health=cur_poke.current_health)
      else:
        cur_poke.gain_health(health_gap)
        return self.name + " used a potion on "+cur_poke.name + " and it gained {healthgain} health. Current health is {health}.".format(healthgain=str(health_gap),health=cur_poke.current_health)

  def switch_active(self, new_active):
    self.new_active=new_active
    #make sure the new pokemon is not knocked out
    if self.poke_team[self.new_active].knocked_out is True:
      return "{name} cannot switch to {new_poke} because it is knocked out!".format(name=self.name,new_poke=self.poke_team[self.new_active].name)
    else:
      self.current_pokemon=self.new_active
      new_poke=self.poke_team[self.current_pokemon]
      return "{name} switched active Pokemon! {new_poke} is now active!".format(name=self.name,new_poke=new_poke.name) 
  
  def attack(self,enemy):
    cur_poke=self.poke_team[self.current_pokemon]
    enemy_poke=enemy.poke_team[enemy.current_pokemon]
    #####need to make it so the ene
    cur_poke.attack(enemy_poke)
    if enemy_poke.knocked_out is True:
      return "{attacker}'s pokemon {poke_name} attacked {defender}'s pokemon {def_poke_name} and knocked it out! {defender} must choose a new active pokemon!".format(attacker=self.name, poke_name=cur_poke.name, defender=enemy.name,def_poke_name=enemy_poke.name) 
    else:
      return "{attacker}'s pokemon {poke_name} attacked {defender}'s pokemon {def_poke_name}! ".format(attacker=self.name, poke_name=cur_poke.name, defender=enemy.name,def_poke_name=enemy_poke.name) + cur_poke.attack(enemy_poke)

#define sample trainers and their pokemon
B_Kobra=Pokemon("Brock's Kobra",4,"fire",101,30,False)
B_Gengar=Pokemon("Brock's Gengar",50, "ghost", 100,100,False)
B_Oddish=Pokemon("Brock's Oddish", 9, "grass", 500,500, False  )
B_Vulpix=Pokemon("Brock's Vulpix", 22, "fire", 750,750,False)
B_Psyduck=Pokemon("Brock's Psyduck", 30, "water",99,99,False)
B_Mew=Pokemon("Brock's Mew",100,"water",1000,0,True)
brocks_team=[B_Kobra,B_Mew,B_Psyduck,B_Oddish,B_Gengar,B_Vulpix]
Brock=Trainer("Brock",brocks_team,5)  
ashs_team=[Oddish,Psyduck,Vulpix,Gengar,Kobra,Mew]
Ash=Trainer("Ash",ashs_team,0,3)

print(Ash.use_potion())
print(Brock.use_potion())
print(Brock.attack(Ash))
print(brocks_team[1].revive())
print(Brock.switch_active(1))

print(Ash.switch_active(1))
print(Brock.attack(Ash))
print(Ash.switch_active(2))
print(Brock.attack(Ash))