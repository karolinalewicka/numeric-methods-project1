import random


def random_guess(number):
    counter = 0
    while random.randint(1, 1000) != number:
        counter += 1
    return counter + 1

def narrowing_guess(number):
    counter = 0
    lower_bound = 1
    upper_bound = 1000
    while True:
        random_number = random.randint(lower_bound, upper_bound)
        if random_number == number:
            break
        if random_number < number:
            lower_bound = random_number + 1
        else:
            upper_bound = random_number - 1
        counter += 1
    return counter + 1
    

def binary_guess(number):
    counter = 0
    lower_bound = 1
    upper_bound = 1000
    while True:
        mid = (lower_bound + upper_bound) // 2
        if number == mid:
            break
        elif number < mid:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
        counter += 1
    return counter + 1


def main():
    print(f'Random done in {random_guess(666)} steps.')
    print(f'Narrowing done in {narrowing_guess(666)} steps.')
    print(f'Binary done in {binary_guess(666)} steps.')
    print(f'Binary done in {binary_guess(500)} steps.')


if __name__ == "__main__":
    main()