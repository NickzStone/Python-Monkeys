import random
import sys


def get_goal_string(goal_range):
    """
    get_goal_string prompts the user for a string and checks
    that all characters in this string are within the range
    of accepted ASCII values defined by goal_range. Exits
    program with an error message if characters outside
    the accepted range are given.

    :param goal_range: the range of accepted ASCII values represented
    as a list of integers
    :return: the goal string given by the user
    """

    goal = str(input("Give a goal string: "))
    checker = [ord(c) for c in goal]

    if len([i for i in checker if i not in goal_range]) > 0:
        sys.exit('Error: Entered Illegal Character!')
    else:
        return goal


def generate_string(goal, goal_range):
    """
    generate_string generates a stream of random characters
    within the accepted range of ASCII values until the
    string generated at random matches the goal string.

    :param goal: the string to match by generating characters
    :param goal_range: the accepted range of ASCII values to generate
    random characters from
    :return: The final generated string and number of characters
    generated before successfully matching the goal string
    """
    temp = ''
    counter = 0

    for i in range(len(goal)):
        x = ''
        while x != goal[i]:
            x = chr(random.choice(goal_range))
            counter += 1
        temp = temp + x

    return 'Found: ' + temp + '\n' + 'In ' + str(counter) + ' keystrokes!'


def main():
    merged_range = list(range(32, 91)) + list(range(97, 123))  # Range of accepted ASCII characters
    goal_string = get_goal_string(merged_range)
    print(generate_string(goal_string, merged_range))


if __name__ == '__main__':
    main()
