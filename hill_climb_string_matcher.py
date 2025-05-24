# --------------------------------------------------------------------------------
# Name:        Hill Climb String Matcher
# Description: A simple implementation of the Hill Climbing algorithm to evolve
#              a random string into a user-defined target string.
#
# Author:      Ioannis Mastoras
# Created:     16 March 2020
# Updated:     May 2025
#
# Requirements: Python Standard Library (random, string)
# --------------------------------------------------------------------------------

import random
import string

# List of all printable ASCII characters (letters, digits, punctuation, whitespace, etc.)
CHARACTER_POOL = list(string.printable)


def generate_random_solution(target_str):
    """Generates a random list of characters with the same length as the target."""
    return [random.choice(CHARACTER_POOL) for _ in range(len(target_str))]


def calculate_score(candidate, target):
    """Returns the number of characters that don't match the target (lower is better)."""
    return sum(1 for i in range(len(candidate)) if candidate[i] != target[i])


def mutate(solution):
    """Randomly changes one character in the solution."""
    index_to_mutate = random.randint(0, len(solution) - 1)
    solution[index_to_mutate] = random.choice(CHARACTER_POOL)
    return solution


def hill_climb(target):
    """Main hill climbing logic to evolve a random string to match the target."""
    best = generate_random_solution(target)
    best_score = calculate_score(best, target)

    evaluated = 0
    accepted = 0

    while best_score > 0:
        if evaluated % 500 == 0:
            print(f"Evaluations: {evaluated} | Best score: {best_score} | Solution: {''.join(best)}")

        candidate = best[:]
        mutate(candidate)
        candidate_score = calculate_score(candidate, target)

        if candidate_score < best_score:
            best = candidate
            best_score = candidate_score
            accepted += 1

        evaluated += 1

    print("\n✅ Target matched!")
    print(f"Evaluations: {evaluated} | Best score: {best_score} | Solution: {''.join(best)}")
    print(f"Number of Solutions Evaluated: {evaluated}")
    print(f"Number of Solutions Accepted: {accepted}")


def main():
    while True:
        user_input = input("\n🎯 Enter target string: ")
        if not user_input.strip():
            print("Please enter a valid string.")
            continue

        target = list(user_input)
        hill_climb(target)

        try:
            continue_input = int(input("\n🔁 Continue? (1 = yes, 0 = no): "))
            if continue_input == 0:
                break
        except ValueError:
            print("Invalid input. Exiting.")
            break


if __name__ == "__main__":
    main()
