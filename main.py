
from fractions import Fraction

def compare(d1,d2): 
    """
    compares how often one die beats the next in sequence (with wins rated at 1 pt and draws rated at 1/2 pt)


    Parameters
    ----------
    d1 & d2 : iterables
        two dice involved in the comparison.  They do not need to be the same length.
        
    Returns
    -------
    TYPE
        The probability that d1 beats d2 
    """
    return Fraction(sum([Fraction(i>=j,1+(i==j)) for i in d1 for j in d2]),len(d1)*len(d2))


def compare_all(dice_list,rotation:int=1):
    """
    compares all the dice in a sequence against the next die (or the [rotation]-th next die) with wrap-around.

    Parameters
    ----------
    dice_list : iterable of iterables
        list of the dice involved
    rotation : int, optional
        The default is 1, i.e. compare each die to the next in line.  Increase to change how far down the list to compare the next die to.

    Returns
    -------
    list
        the fraction for each [i]-th die compared to the [i+rotation]-th die with wrap-around

    """
    return [compare(i,j) for i,j in zip(dice_list,dice_list[rotation:]+dice_list[:rotation])]


class Efron:
    """
    This generates a potentially infinite number of Efron dice. Each die beats the next with 2/3s probability

    Parameters
    ----------
    n : int 4 or greater, optional
        Controls how many Efron dice to produce. The default generates 4 dice which is Efron's original list

    Accessing the dice
    ------------------
    use either self.dice to see all the dice or self.get(i) to see the i-th die

    """
    def __init__(self,n:int=4):

        if n<4:
            raise ValueError('n must be greater than or equal to 4')
        
        self.dice = [(*[2*n-b]*b,*[4-b]*(6-b)) for b in [2,3,4]]+[
                     (*[2*n-5-a]*4,*[3+a]*2) for a in range(n-3)]
             
    def get(self,i):
        return self.dice[i]

   

class MultiplayerDice:
    """
        
    This generates (n) Multiplayer dice.  Each i-th die beats the next n//2 dice with wraparound 5/9s of the time.

    Parameters
    ----------
    n : odd int
        Controls how many Multiplayer dice to produce.
        
    Accessing the dice
    ------------------
    use either self.dice to see all the dice or self.get(i) to see the i-th die
    """
    def __init__(self,n:int):

        if not n%2: raise ValueError('n must be odd')
        self.dice = [(n-i, (n//2-i)%n+n+1, 2*i%n+2*n+1) for i in range(n)]

    def get(self,i):
        return self.dice[i]



