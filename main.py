import os
import sys
import time
import hylib as hl
path = 'dataset/'

class IA():
    def __init__(self):
        #leggi dataset e skills, poi crea un'istanza della rete neurale
        self.db = hl.read_database(path+'raw_db.txt')
        self.skills = hl.read_skills()
        self.nn = hl.NeuralNetwork()
        print('[*] hy initialized.')
        #esegui il ciclo vitale
        self.run()

    def do(self, x, y=''):
        '''
        do func()
        -----
        Parameters:
        
        self - this instance, automatic
        x    - stimolo standarizzato
        y    - stimolo originale

        Returns:

        Nothing.

        ----
        how it works:
        se possibile esegui la skill denominata "#" + %stimolo all'imperativo%
        se non viene trovata significa che non esiste, quindi:
            crea la skill chiamata skill_%last_value+1%.py e dai come possibili
            risposte quelle che l'utente da.
        '''
        try:
            exec(self.skills['#'+x])
        except:
            #mk the skill
            i=0
            #ottieni il nome del nuovo file
            for filename in os.listdir('skills/'):
                i+=1
            self.name = 'skill_'+str(i+1)+'.py'
            f = open('skills/'+self.name, 'w+')
            #gli argomenti da passare al file
            #sono composti da 
            arg=[x, input('come devo rispondere? ').split()]
            f.write(hl.skill_template(model='printout', args=arg))
            f.close()
    
    def run(self):
        #aspetta finchè non ottieni lo stimolo
        x=input('>> ')
        #standarizza lo stimolo
        x_ = self.nn.run(x)
        if not x_ == 'notindataset':
            #esegui un'azione per rispondere allo stimolo
            self.do(hl.get_imp(x_), x_)
            time.sleep(1)
            #self.skills['#'+x] = open('skills/'+self.name).read()
        else:
            y=input('cosa è ogni parola?\n>>')
            a=[]; y_=''
            for z in y.split():
                a.append(''.join(self.nn.standarize(z)))
            y_=' '.join(a)
            for i in y.split():
                self.db[i]=x.split()
            print(self.db)
            f=open('dataset/raw_db.txt', 'a+')
            for i in y.split():
                f.write(i+' - '+', '.join(x.split()))
            f.close()
            #refresh dataset
            self.db = hl.read_database()

def main():
    hy = IA()
    hy.run()

if __name__ == '__main__':
    main()
