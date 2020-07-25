import os

def is_fem(x):
    if x.endswith('a'):
        return True
    else:
        return False

def is_sing(x):
    if x.endswith('o') or x.endswith('a'):
        return True
    else:
        return False

def get_sing(x):
    z=[]
    if is_fem(x):
        for letter in x:
            z.append(letter)
        z[len(z)-1]='a'
        y=''.join(z)
    else:
        for letter in x:
            z.append(letter)
        z[len(z)-1]='o'
        y=''.join(z)

    if y.endswith('aa') or y.endswith('oo'):
        return y[:len(y)-1]
    else:
        return y

def get_imp(x):
    z=[]
    if is_sing(x):
        for letter in x:
            z.append(letter)
        z[len(z)-1]='a'
        y=''.join(z)
    else:
        for letter in x:
            z.append(letter)
        z[len(z)-1]='a'
        y=''.join(z)

    if y.endswith('aa'):
        return y[:len(y)-1]
    else:
        return y

def get_masch(x):
    z=[]
    if is_sing(x):
        for letter in x:
            z.append(letter)
        z[len(z)-1]='o'
        y=''.join(z)
    else:
        for letter in x:
            z.append(letter)
        z[len(z)-1]='o'
        y=''.join(z)

    if y.endswith('oo'):
        return y[:len(y)-1]
    else:
        return y


def read_database(path='db/raw_dataset.dat'):
    d={}; j=0
    for line in open(path).readlines():
        d[line.split(' - ')[0].rstrip()] = line.split(' - ')[1].split(', ')[:]
    return d

def read_skills(path='skills/'):
    d={}
    for filename in os.listdir(path):
        d[open(path+filename).read().split('\n')[0]] = open(path+filename).read()
    return d

class NeuralNetwork():
    def __init__(self):
        self.db = read_database('dataset/raw_db.txt')

    def standarize(self, x):
        z=[]
        y=x.split(' ')
        for e in y:
            z.append(get_masch(get_sing(e)))
        return z
        
    def run(self, x):
        x_ = self.standarize(x)
        print(x_)
        #xA = x_.split(' ')
        xA=x_
        for word in xA:
            for key in self.db:
                if word in self.db[key]:
                    return key
            #if not in database
            return 'notindataset'
            #self.learn(word)

def skill_template(args, model='printout'):
    src = open('models/'+model+'.txt').read()
    print(args)
    src=src.format(f=args[0], s=args[1])
    return src