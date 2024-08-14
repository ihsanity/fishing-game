import math
import random
from enum import Enum


starting_gold = 100

# Today Data (global variables)
current_gold = 100
generated_fish_size, list_fish_by_size = [], []
generated_fish_color, list_fish_by_color = [], []
today_earnings = 0

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

# nested array containing the price range for each fish size and color
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

# function to generate fish data based on the total number of fish, the number of fish variety, and the deviation
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

# function to get the percentage of each item in a list of integers
def get_percentage_from_int_list(list):
    result = []
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    for i in range(len(list)):
        result.append(round(list[i] * 100 / sum))    
    return result

# generate fish data for a new day
def generate_day():
    global current_gold, generated_fish_size, generated_fish_color, list_fish_by_size, list_fish_by_color
    current_gold = starting_gold
    total_fish = random.randint(*fish_count_range)
    generated_fish_size, list_fish_by_size = generate_fish_data(total_fish, len(pole_prices), occurrence_deviation)
    generated_fish_color, list_fish_by_color = generate_fish_data(total_fish, len(bait_prices), occurrence_deviation)
    random.shuffle(list_fish_by_color)

# calculate fishing result for the day given the day data and the bought fishing items
def simulate_fishing_day(fishlist_by_size, fishlist_by_color, pole, bait_list):
    global today_earnings
    catchable_fish_list = []
    for i in range(len(fishlist_by_size)):
        if fishlist_by_size[i] == pole:
            fish = Fish(fishlist_by_size[i], fishlist_by_color[i])
            catchable_fish_list.append(fish)

    today_earnings = 0
    caught_fish_color = []
    for fish in catchable_fish_list:
        if bait_list[fish.color] > 0:
            bait_list[fish.color] -= 1
            today_earnings += fish.price 
            caught_fish_color.append(fish.color)
    
    return caught_fish_color
