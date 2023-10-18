import random


def generate_teams(participants):
    # Shuffle the participants randomly
    random.shuffle(participants)

    # Check if restricted pairs are together
    stacked_teams = [("Ned J.", "Tanner G."), ("Ned J.", "Eric E."), ("Tanner G.", "Eric E.")]
    while any((participants[i] in pair and participants[i + 1] in pair) for i in range(0, len(participants), 2) for pair
              in stacked_teams):
        random.shuffle(participants)

    # Pair each person with a partner
    teams = [(participants[i], participants[i + 1]) for i in range(0, len(participants), 2)]

    return teams


# Read names from the file
with open('PickleballNames.txt', 'r') as file:
    participants = [line.strip() for line in file]

# Check if there's an odd number of participants
if len(participants) % 2 != 0:
    print("There's an odd number of participants. Hadden has volunteered to not participate.")
    participants.remove("Hadden W.")


teams = generate_teams(participants)

for i, team in enumerate(teams, 1):
    print(f"Team {i}: {team[0]} and {team[1]}\n")
