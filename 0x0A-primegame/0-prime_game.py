#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(rounds, nums):
    """Determines the winner of a prime game session with `rounds` rounds.
    
    Args:
        rounds (int): The number of rounds.
        nums (list): List of integers representing the upper limit for each round.
    
    Returns:
        str: The winner ('Maria' or 'Ben') or None if there is no winner.
    """
    if rounds < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    # Generate prime numbers up to the maximum number in `nums`.
    max_num = max(nums)
    is_prime = [True for _ in range(max_num + 1)]
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Sieve of Eratosthenes to find all primes up to max_num.
    for num in range(2, int(max_num ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, max_num + 1, num):
                is_prime[multiple] = False

    # Determine the number of primes up to each number in nums for each round.
    for upper_limit in nums:
        prime_count = sum(is_prime[2:upper_limit + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None

    return 'Maria' if maria_wins > ben_wins else 'Ben'

