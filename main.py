import time
import random


def Qualifying():
  global firstplace
  global secondplace
  global thirdplace
  global fourthplace
  global fifthplace
  global sixthplace
  global seventhplace
  global eighthplace
  global ninthplace
  global tenthplace
  global eleventhplace
  global twelthplace
  global thirteenthplace
  global fourteenthplace
  global fifteenthplace
  global sixteenthplace
  global seventeenthplace
  global eighteenthplace
  global nineteenthplace
  global twentieth
  
  drivers = ["Hamilton", "Bottas", "Verstappen", "Perez", "Norris", "Ricciardo", "Sainz", "Leclerc", "Tsunoda", "Gasly", "Stroll", "Vettel", "Giovinazzi", "Raikkonen", "Alonso", "Ocon", "Giovinazzi", "Latifi", "Schumacher", "Mazepin"]
  str(drivers)

  firstplace = (random.choices(drivers, weights=(30, 10, 30, 15, 5, 5, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), k=1)[0])

  
  drivers.remove(firstplace)
  secondplace = (random.choices(drivers, weights=(30, 35, 25, 3, 3, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), k=1)[0])
  drivers.remove(secondplace)
  thirdplace = (random.choices(drivers, weights=(40, 20, 15, 5, 5, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0), k=1)[0])
  drivers.remove(thirdplace)
  fourthplace = (random.choices(drivers, weights=(60, 15, 10, 5, 5, 3, 3, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0), k=1)[0])
  drivers.remove(fourthplace)
  fifthplace = (random.choices(drivers, weights=(20, 20, 10, 10, 10, 10, 5, 5, 2, 2, 2, 2, 1, 1, 0, 0), k=1)[0])
  drivers.remove(fifthplace)
  sixthplace = (random.choices(drivers, weights=(15, 15, 15, 15, 10, 10, 5, 5, 3, 3, 2, 1, 1, 0, 0), k=1)[0])
  drivers.remove(sixthplace)
  seventhplace = (random.choices(drivers, weights=(20, 10, 10, 10, 10, 10, 10, 10, 3, 3, 2, 1, 1, 0), k=1)[0])
  drivers.remove(seventhplace)
  eighthplace = (random.choices(drivers, weights=(15, 10, 10, 10, 10, 10, 10, 10, 3, 3, 3, 3, 3), k=1)[0])
  drivers.remove(eighthplace)
  ninthplace = (random.choices(drivers, weights=(15, 11, 10, 10, 10, 10, 10, 10, 4, 4, 3, 3), k=1)[0])
  drivers.remove(ninthplace)
  tenthplace = (random.choices(drivers, weights=(15, 13, 10, 10, 10, 10, 10, 12, 5, 4, 2), k=1)[0])
  drivers.remove(tenthplace)
  eleventhplace = (random.choices(drivers, weights=(17, 15, 12, 10, 10, 10, 10, 10, 6, 1), k=1)[0])
  drivers.remove(eleventhplace)
  twelthplace = (random.choices(drivers, weights=(20, 13, 12, 12, 11, 11, 11, 11, 0), k=1)[0])
  drivers.remove(twelthplace)
  thirteenthplace = (random.choices(drivers, weights=(20, 15, 15, 15, 15, 11, 10, 0), k=1)[0])
  drivers.remove(thirteenthplace)
  fourteenthplace = (random.choices(drivers, weights=(20, 20, 15, 15, 15, 15, 0), k=1)[0])
  drivers.remove(fourteenthplace)
  fifteenthplace = (random.choices(drivers, weights=(22, 20, 15, 15, 15, 15), k=1)[0])
  drivers.remove(fifteenthplace)
  sixteenthplace = (random.choices(drivers, weights=(30, 22, 20, 15, 15), k=1)[0])
  drivers.remove(sixteenthplace)
  seventeenthplace = (random.choices(drivers, weights=(50, 20, 20, 10), k=1)[0])
  drivers.remove(seventeenthplace)
  eighteenthplace = (random.choices(drivers, weights=(34, 33, 33), k=1)[0])
  drivers.remove(eighteenthplace)
  nineteenthplace = (random.choices(drivers, weights=(50, 50), k=1)[0])
  drivers.remove(nineteenthplace)

  print(firstplace)
  print(secondplace)
  print(thirdplace)
  print(fourthplace)
  print(fifthplace)
  print(sixthplace)
  print(seventhplace)
  print(eighthplace)
  print(ninthplace)
  print(tenthplace)
  print(eleventhplace)
  print(twelthplace)
  print(thirteenthplace)
  print(fourteenthplace)
  print(fifteenthplace)
  print(sixteenthplace)
  print(seventeenthplace)
  print(eighteenthplace)
  print(nineteenthplace)
  twentieth = drivers[0]
  print(twentieth)

  
  print("")
  news = [("News: ", firstplace, "runs away with it again!"), ("News: ", secondplace, "close to beating", firstplace), ("News: Shock podium for", thirdplace), ("News:", nineteenthplace, "crashes out in crazy GP!"), ("News: ", seventeenthplace, "had a shocking performace!" ), ("News:", seventhplace, "has uneventful GP."), ("News:", firstplace, "dominates the race!"), ("News:", fifthplace, "has a strong race!"), ("News: Super", firstplace, "beats", secondplace)]
  str(news)
  print(random.choice(news))

driverscores = {
  "Hamilton": 0,
  "Bottas": 0,
  "Verstappen": 0,
  "Perez": 0,
  "Norris": 0,
  "Ricciardo": 0,
  "Sainz": 0,
  "Leclerc": 0,
  "Stroll": 0,
  "Vettel": 0,
  "Tsunoda": 0,
  "Gasly": 0,
  "Stroll": 0,
  "Vettel": 0,
  "Giovinazzi": 0,
  "Raikkonen": 0,
  "Alonso": 0,
  "Ocon": 0,
  "Russell": 0,
  "Latifi": 0,
  "Schumacher": 0,
  "Mazepin": 0,
}


def addscore(driver, score):
  driverscores[driver] = driverscores[driver] + score

def mercedespoints():
  global mercscore
  mercdriver1 = driverscores.get("Hamilton")
  mercdriver2 = driverscores.get("Bottas")

  #mercscore = #mercdriver1 + mercdriver2

def redbullpoints():
  global redbullscore
  redbulldriver1 = driverscores.get("Verstappen")
  redbulldriver2 = driverscores.get("Perez")
  
 # redbullscore = #redbulldriver1 + redbulldriver2

def mclarenpoints():
  global mclarenscore
  mclarendriver1 = driverscores.get("Norris")
  mclarendriver2 = driverscores.get("Ricciardo")

  #mclarenscore = #mclarendriver1 + mclarendriver2

def astonmartinpoints():
  global astonscore
  astondriver1 = driverscores.get("Stroll")
  astondriver2 = driverscores.get("Vettel")

  #astonscore = #astondriver1 + astondriver2

def alphatauripoints():
  global atscore
  atdriver1 = driverscores.get("Tsunoda")
  atdriver2 = driverscores.get("Gasly")

  #atscore =# atdriver1 + atdriver2

def ferraripoints():
  global ferrariscore
  ferraridriver1 = driverscores.get("Sainz")
  ferraridriver2 = driverscores.get("Leclerc")

 # ferrariscore = #ferraridriver1 + ferraridriver2

def alpinepoints():
  global alpinescore
  alpinedriver1 = driverscores.get("Alonso")
  alpinedriver2 = driverscores.get("Ocon")
 # alpinescore = #alpinedriver1 + alpinedriver2

def alfaromeopoints():
  global alfascore
  alfadriver1 = driverscores.get("Giovinazzi")
  alfadriver2 = driverscores.get("Raikkonen")
  
 # alfascore = #alfadriver1 + alfadriver2

def williamspoints():
  global williamsscore
  williamsdriver1 = driverscores.get("Russell")
  williamsdriver2 = driverscores.get("Latifi")

 # williamsscore = #williamsdriver1 + williamsdriver2

def haaspoints():
  global haasscore
  haasdriver1 = driverscores.get("Schumacher")
  haasdriver2 = driverscores.get("Mazepin")

  #haasscore = #haasdriver1 + haasdriver2

def printconstructors():
  mercedespoints()
  redbullpoints()
  mclarenpoints()
  astonmartinpoints()
  alphatauripoints()
  ferraripoints()
  alfaromeopoints()
  williamspoints()
  haaspoints()
  alpinepoints()
  print("\033[96m Mercedes:", mercscore)
  print("\033[34m Red Bull:", redbullscore)
  print("\033[33m Mclaren:", mclarenscore)
  print("\033[91m Ferrari:", ferrariscore)
  print("\033[90m Alpha Tauri:", atscore)
  print("\033[32m Aston Martin:", astonscore)
  print("\033[31m Alfa Romeo:", alfascore)
  print("\033[36m Alpine:", alpinescore)
  print("\033[1;37;40m Williams:", williamsscore)
  print("\033[1;37;40m Haas:", haasscore)




def printscores():
  sorted(driverscores.values())
  driverscores_items = driverscores.items()
  for item in driverscores_items:
    print(item)

#START OF PROGRAM

time.sleep(1)

print("\033[1;37;40m Welcome to F1 Simulator 2021!")

time.sleep(2)

print("")
print("")

print("F1 Teams:\n")

print("\033[96m Mercedes \t\t\033[34m Red Bull")
print("")

print("\033[33m Mclaren \t\t\033[32m Aston Martin")
print("")

print("\033[90m Alpha Tauri \t\033[91m Ferrari")
print("")

print("\033[36m Alpine \t\t\033[31m Alfa Romeo")
print("")

print("\033[1;37;40m Williams \t\t\033[37m Haas")
print("")

print("")
time.sleep(5)

re.clear()

#START OF PROGRAM AFTER INTRO
time.sleep(1)
races = 1
teamselect = input("What team would you like to join? ")
print("")
print("You have joined", teamselect)
print("")
while races < 22:
  print("OPTION 1: Start Next Race \nOPTION 2: Explore History \nOPTION 3: Driver Standings \nOPTION 4: Constructor Standings\nOPTION 5: Simulate Fast \nOPTION 6: Update Logs")  #driver transfers coming soon
  
  print("")
 

  option = int(input("What would you like to do? "))
  print("")
 

  if option == 1:
    re.clear()
    print("Welcome to qualifying number", races)
    
    time.sleep(2)
    print("Qualifying is about to start!")
    print("")
    print("")
    time.sleep(1)
    print("Running Q1....")
    print("")
    print("DRIVERS OUT IN Q1")
    time.sleep(1.5)
    print("Race completed")
    print("")
    Qualifying()
    print("")
    time.sleep(5)
    addscore(firstplace, 25)
    addscore(secondplace, 18)
    addscore(thirdplace, 15)
    addscore(fourthplace, 12)
    addscore(fifthplace, 10)
    addscore(sixthplace, 8)
    addscore(seventhplace, 6)
    addscore(eighthplace, 4)
    addscore(ninthplace, 2)
    addscore(tenthplace, 1)
    file=open ("racehistory.txt", "a")
    file.write("")
    file.write("\nRace:\n\n")
    file.write("")
    file.write(firstplace + "\n")
    file.write(secondplace + "\n")
    file.write(thirdplace + "\n")
    file.write(fourthplace + "\n")
    file.write(fifthplace + "\n")
    file.write(sixthplace + "\n")
    file.write(seventhplace + "\n")
    file.write(eighthplace + "\n")
    file.write(ninthplace + "\n")
    file.write(tenthplace + "\n")
    file.write(eleventhplace + "\n")
    file.write(twelthplace + "\n")
    file.write(thirteenthplace + "\n")
    file.write(fourteenthplace + "\n")
    file.write(fifteenthplace + "\n")
    file.write(sixteenthplace + "\n")
    file.write(seventeenthplace + "\n")
    file.write(eighteenthplace + "\n")
    file.write(nineteenthplace + "\n")
    file.write(twentieth+ "\n\n")
    file.write("")
    file.write("-------------------------")
    file.close()
    races = races + 1
    
  elif option == 2:
    file=open ("racehistory.txt", "r")
    print (file.read () )
  elif option == 3:
    printscores()
    print("")
    time.sleep(5)
    input("Enter to go back to the menu. ")
  elif option == 4:
    
    printconstructors()
    print("")
  elif option == 5:
    Qualifying()
    addscore(firstplace, 25)
    addscore(secondplace, 18)
    addscore(thirdplace, 15)
    addscore(fourthplace, 12)
    addscore(fifthplace, 10)
    addscore(sixthplace, 8)
    addscore(seventhplace, 6)
    addscore(eighthplace, 4)
    addscore(ninthplace, 2)
    addscore(tenthplace, 1)
    races = races + 1
  elif option == 6:
    print("")
    print("UPDATE LOGS:")
    time.sleep(2)
    print("")
    print("Log 1: Wed 21 Apr 2021")
    print("")
    time.sleep(2)
    print("+New Update Logs System")
    time.sleep(3)
    print("+Red Bull pushed closer to Mercedes")
    time.sleep(3)
    print("+Team Strengths Overhaul:")
    time.sleep(1)
    print("+New Team Order- Mercedes(#), Red Bull(#), Mclaren(#), Ferrari(++), AlphaTauri(#), Aston Martin(--), Alfa Romeo(+), Alpine(-), Williams(#), Haas(#)")
    time.sleep(3)
    print("")

    

re.clear()

while True:
  print("")
  endingoption = int(input("OPTION 1: Season Review \nOPTION 2: End Game\nOPTION 3: Driver Standings \nOPTION 4: Constructor Standings \nOPTION 5: Update Logs"))
  if endingoption == 1:
    re.clear()
    print("Season Review:")
    print("")
    if teamselect == ("Mercedes"):
      print("This is the Mercedes season review!")
      print("")
      time.sleep(2)
      mercdriver1 = driverscores.get("Hamilton")
      mercdriver2 = driverscores.get("Bottas")

      mercscore = mercdriver1 + mercdriver2
      print("\033[96m Mercedes:", mercscore)
      print("")
      print("\033[96m Hamilton:", mercdriver1)
      print("\033[96m Hamilton:", mercdriver2)
      time.sleep(2)
      print("")
      print("Good job on overseeing the team!")
      print("")
      time.sleep(3)
      printconstructors()
      print("")
      print("The constructor standings are above!")
      time.sleep(2)
      print("")
      printscores()
      print("")
      time.sleep(5)
      quit()
    else:
      print("test")

      
    

  elif endingoption == 2:
    quit()
  elif endingoption == 3:
    printscores()
    print("")
    time.sleep(5)
    input("Enter to go back to the menu. ")
  elif endingoption == 4:
    printconstructors()
    print("")
    time.sleep(2)
  elif endingoption == 5:
    print("")
    print("UPDATE LOGS:")
    time.sleep(2)
    print("")
    print("Log 1: Wed 21 Apr 2021")
    print("")
    time.sleep(2)
    print("+New Update Logs System")
    time.sleep(3)
    print("+New Team Strengths")
    time.sleep(2)
    print("")
    print("Log 2: Thu 22 Apr 2021")
    print("")
    time.sleep(2)
    print("+Work started on F1 Simulator 2022")
    time.sleep(3)
    print("+Work on Qualifying and Race Events")
