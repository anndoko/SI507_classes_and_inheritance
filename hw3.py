'''
SI 507 W18 homework 3: Classes and Inheritance

Your discussion section:
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
from random import randrange
class Explore_pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10
  def __init__(self, name="Coco"):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
        return "happy"
    elif self.hunger > self.hunger_threshold:
        return "hungry"
    else:
        return "bored"

  def __str__(self):
    state = "I'm " + self.name + '. '
    state += 'I feel ' + self.mood() + '. '
    if self.mood() == 'hungry':
      state += 'Feed me.'
    if self.mood() == 'bored':
      state += 'You can teach me new words.'
    return state
coco = Explore_pet()

#your code begins here . . .
coco.boredom = 10 # make coco feel bored
print(coco)

brian = Explore_pet("Brian") # create an instance
brian.hunger = 20 # make Brian hungry
print(brian)

'''
Task B
'''
#add your codes inside of the Pet class
class Pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10

  def __init__(self, name = "Coco", words_lst = ["hello"]):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)
    self.words = words_lst

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
        return "happy"
    elif self.hunger > self.hunger_threshold:
        return "hungry"
    else:
        return "bored"

  def __str__(self):
    state = "I'm " + self.name + '. '
    state += 'I feel ' + self.mood() + '. '
    if self.mood() == 'hungry':
      state += 'Feed me.'
    if self.mood() == 'bored':
      state += 'You can teach me new words.'
    return state

  def clock_tick(self):
    self.hunger += 2
    self.boredom += 2

  def say(self):
    print("I know how to say:")
    for word in self.words:
        print(word)

  def teach(self, word):
    self.words.append(word)
    if self.boredom < abs(boredom_decrement):
      self.boredom = 0
    self.boredom += boredom_decrement

  def feed(self):
    if self.hunger < abs(hunger_decrement):
      self.hunger = 0
    self.hunger += hunger_decrement

  def hi(self):
    random_num = randrange(len(self.words))
    return self.words[random_num]

'''
Task C
'''


def teaching_session(my_pet, new_words):
  #your code begins here . . .
  for word in new_words:
      my_pet.words.append(word)

      print(my_pet.hi())
      print(my_pet)

      if my_pet.mood == "hungry":
          my_pet.feed()

      my_pet.clock_tick()

# test
anndo = Pet("Anndo")
teaching_session(anndo, ['I am sleepy', 'You are the best','I love you, too'])

#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat
'''
#your code begins here . . .

'''
Task B: Poodle
'''
#your code begins here . . .
