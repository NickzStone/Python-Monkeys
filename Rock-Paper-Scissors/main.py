class Item:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon


def battle(x, y):
    if x.weapon == 'Rock':
        if y.weapon == 'Rock':
            return 'Tie'
        if y.weapon == 'Paper':
            return 'Paper beats Rock, ' + y.name + ' wins!'
        if y.weapon == 'Scissors':
            return 'Rock beats Scissors, ' + x.name + ' wins!'
    if x.weapon == 'Paper':
        if y.weapon == 'Rock':
            return 'Paper beats Rock, ' + x.name + ' wins!'
        if y.weapon == 'Paper':
            return 'Tie'
        if y.weapon == 'Scissors':
            return 'Scissors beats Paper, ' + y.name + ' wins!'
    if x.weapon == 'Scissors':
        if y.weapon == 'Rock':
            return 'Rock beats Scissors, ' + y.name + ' wins!'
        if y.weapon == 'Paper':
            return 'Scissors beats Paper, ' + x.name + ' wins!'
        if y.weapon == 'Scissors':
            return 'Tie'


def main():
    a = Item('Robert', 'Rock')
    b = Item('Peter', 'Paper')
    c = Item('Steve', 'Scissors')

    print(a.name)
    print(a.weapon)

    print(battle(a, b))
    print(battle(b, c))
    print(battle(c, a))


if __name__ == "__main__":
    main()
