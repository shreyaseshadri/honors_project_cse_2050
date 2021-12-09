import names, random, sys
from Contestant import Contestant, ContestantSet
from GamePlay import GamePlay

class RunGame: 
    def __init__(self): 
        self._game = GamePlay()
    
    def start_game(self): 
        #print("Welcome to the Game. Below are the Contestants\n")
        people = (self._game.display_people())
        return people
        #self.continue_game()            
    
    def continue_game(self, initial_guess): 
        count_correct = 0 
        correct = False
        #gather user input for guess of pairs
        initial_guess = str(initial_guess)
        guess = initial_guess.split(',')
        self._game.initial_check(guess)

        #check if guess of pairs is equal to true pairs
        for p in self._game._guess_pairs: 
            for q in self._game._pairs: 
                if (p[0] == q[0] and p[1] == q[1]) or (p[0] == q[1] and p[1] == q[0]) or (p[1] == q[0] and p[0] == q[1]): 
                    count_correct += 1
              
        if count_correct + 1 == len(self._game._pairs): 
            correct = True
        
        return (count_correct, correct)
        
    
    def end_game(self): 
        print('You won!!')
        sys.exit()

if __name__ == '__main__': 
    g = RunGame()
    g.start_game()