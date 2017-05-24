import random, string, functools

PHRASE = "In previous subsection it has been claimed that via the operations of selection, crossover, and mutation the GA will converge over successive generations towards the global (or near global) optium."
SIZE = 3000
CUTOFF = 0.85
MUTATION = 0.01
population = []

def fitness(s):
   x = 0
   for i in range(len(PHRASE)):
      if s[i] == PHRASE[i]:
         x += 1
   return x

def mutation(l):
   x = l
   random.shuffle(x)
   for i in range(int(MUTATION*SIZE)):
      for j in range(random.randint(1, len(PHRASE))):
         z = list(x[i])         
         z[random.randint(0, len(PHRASE)-1)] = random.choice(string.printable)
         x[i] = ''.join(z)
   return x

def cross(l):
   c1 = ''
   c2 = ''
   x = []
   for i in range(0, len(l), 2):
      for j in range(len(PHRASE)):
         if random.randint(0,1) == 1:
            c2 += l[i][j]
            c1 += l[i+1][j]
         else:
            c1 += l[i][j]
            c2 += l[i+1][j]
      x.append(c1)
      x.append(c2)
      c1 = c2 = ''
   return x

def compare(x, y):
      if fitness(x) < fitness(y):
         return -1
      else:
         return 0

def randomword(length):
   return ''.join(random.choice(string.printable) for i in range(length))

maxfit = 0
for i in range(SIZE):
    s = randomword(len(PHRASE))
    population.append(s)
    maxfit = max(maxfit, fitness(s))
population = sorted(population, key=functools.cmp_to_key(compare), reverse=True)

t = 1
while t < 200:
   print("Generation:", t)
   print("Most Fit:", population[0], "\nFitness:", maxfit)
   population = population[:int(CUTOFF*SIZE)]
   
   parents = population[:int(SIZE-CUTOFF*SIZE)]
   parents = mutation(cross(parents))
   
   population = mutation(population) + parents
   population = sorted(population, key=functools.cmp_to_key(compare), reverse=True)

   maxfit = 0
   for i in population:
      maxfit = max(maxfit, fitness(i))
   t += 1
