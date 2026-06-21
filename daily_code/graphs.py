mport matplotlib.pyplot as plt
"""
play=["Ronaldo","Messi","Mbappe","Haaland","Neymar.jr"]
goals = [5,7,6,4,5]

plt.bar(play,goals)
plt.title("Fifa Goals")
plt.xlabel("Players")
plt.ylabel("Goals")
plt.show()
"""

matches =[1,2,3,4,5]
goals = [2,1,3,0,4]
plt.plot(matches,goals)
plt.show()

plt.pie([40,35,25],labels=["Messi","Mane","Neil"])