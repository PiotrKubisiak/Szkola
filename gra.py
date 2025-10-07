def constructMap(x, y):
    tab = []
    tab1 = []
    for yi in range (y):
        tab1.append(["[]"])

    for xi in range (x):
        tab.append(tab1)
    return tab

WIDTH = int(input("Podaj szerokość planszy "))
HEIGHT = int(input("Podaj wysokośc planszy "))

tab = constructMap (HEIGHT, WIDTH)
for x in tab:
    for y in x:
        print(y[0], end="")
    print()

class enemy:
    def __init__(self, HP, SpawnX, SpawnY):
        self.HP = HP
        self.SpawnX = SpawnX
        self.SpawnY = SpawnY

enemy = enemy(100, HEIGHT-1, WIDTH-1)
print(" Enemy:", enemy.x, enemy.y)
tab [enemy.x][enemy.y] = "[E]"
