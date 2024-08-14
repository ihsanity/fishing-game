import sys
import math
import random
from enum import Enum


starting_gold = 100

class FishSize(Enum):
    Small = 0
    Medium = 1
    Big = 2

class FishColor(Enum):
    Red = 0
    Blue = 1
    Green = 2

class Fish:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.price = random.randint(*fish_price_matrix[size][color])

# Prices specifications

pole_prices = {
    FishSize.Small: 5,
    FishSize.Medium: 10,
    FishSize.Big: 15
}

bait_prices = {
    FishColor.Red: 1,
    FishColor.Blue: 2,
    FishColor.Green: 3,
}

pole_names = ["Small Fishing Pole", "Medium Fishing Pole", "Big Fishing Pole"]
color_names = ["Red", "Blue", "Green"]
bait_color_prices = [1, 2, 3]

fish_price_matrix = [
    [[1, 5],   [3, 5],   [5, 5]],   # Small
    [[5, 10],  [8, 10],  [10, 10]], # Medium
    [[10, 15], [13, 15], [15, 15]]  # Big
    # Red,     Blue,      Green
]

# Number of fish that appears each day, modifiable
# Best to keep the number low, due to how cheap the baits are, especially using bigger poles
fish_count_range = [12, 20]

# Determine how deviated the number of occurences from a balanced distribution
# e.g. in a 18 fish environment, the worst scenario will be [4, 4, 10]
# amount can't be lower than 4 (18/3 - 2) where 3 is the fish variety and 2 is the occurrence_deviation
# applies to both fish size and colors
occurrence_deviation = 2


# function to generate a sequence containing {count} number of items with a sum of {total}
def randomize_amount(total, count):
    remaining_sum = total
    result = []
    for _ in range(count-1):
        amount = random.randint(0, remaining_sum)
        remaining_sum = remaining_sum - amount
        result.append(amount)
    result.append(remaining_sum)
    return result

def generate_fish_data(total, count, deviation):
    min_value = math.floor(total / count) - deviation
    undistributed = total - (min_value * count)
    to_be_distributed = randomize_amount(undistributed, count)
    distributed_fish_data = [value + min_value for value in to_be_distributed]

    fish_list = []
    for i in range(len(distributed_fish_data)):
        for _ in range(distributed_fish_data[i]):
            fish_list.append(i)

    return distributed_fish_data, fish_list

def get_percentage_from_int_list(list):
    result = []
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    for i in range(len(list) - 1):
        result.append(round(list[i] * 100 / sum))
    return result

def simulate_fishing_day(fishlist_by_size, fishlist_by_color, pole, bait_list):
    pass    


if __name__ == "__main__":
    total_fish = random.randint(*fish_count_range)
    generated_fish_size, list_fish_by_size = generate_fish_data(total_fish, len(pole_prices), occurrence_deviation)
    generated_fish_color, list_fish_by_color = generate_fish_data(total_fish, len(bait_prices), occurrence_deviation)

    print(generated_fish_size)
    print(generated_fish_color)
    random.shuffle(list_fish_by_color)
    print(list_fish_by_size)
    print(list_fish_by_color)

    pole_choice = int(sys.argv[1])

    catchable_fish_list = []
    for i in range(total_fish):
        if list_fish_by_size[i] == pole_choice:
            fish = Fish(list_fish_by_size[i], list_fish_by_color[i])
            catchable_fish_list.append(fish)

    today_bait_list = [2, 3, 1]


    print(pole_prices[FishSize(pole_choice)])
    
    current_gold = starting_gold - pole_prices[FishSize(pole_choice)] - 11
    today_earnings = 0
    for fish in catchable_fish_list:
        print("Fish color : " + FishColor(fish.color).name + ", price : " + str(fish.price))
        if today_bait_list[fish.color] > 0:
            today_bait_list[fish.color] -= 1
            print("CAUGHT!")
            today_earnings += fish.price
    print("today_earnings : ", today_earnings)
    if current_gold + today_earnings > starting_gold:
        print("YOU WIN!")
    elif current_gold + today_earnings == starting_gold:
        print("TIE...")
    else:
        print("YOU LOSE...")
