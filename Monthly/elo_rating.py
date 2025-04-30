import math
coders = []

def add_coder(name, rank, rating):
    c = {
        'name': name,
        'rank': rank,
        'prev_rating': rating,
        'post_rating': 0,
        'rating_change': 0
    }
    coders.append(c)

def calculate_new_rating():
    n = len(coders)
    # K = 32 * (n - 1)  # Constant to multiply the change of Rating with
    # divisor = n * (n - 1) / 2
    for i in range(n):
        curr_rank = coders[i]['rank']
        curr_rating = coders[i]['prev_rating']
        # numerator = 0.0
        # S = (n - curr_rank) / divisor  # Actual Score
        # for j in range(n):
        #     if i != j:
        #         opponents_rating = coders[j]['prev_rating']
        #         numerator += 1 / (1.0 + 10 ** ((opponents_rating - curr_rating) / 400.0))

        # EA = numerator / divisor  # Expected Score

        coders[i]['rating_change'] = math.ceil((1800.0 / (curr_rank + 5)))
        coders[i]['post_rating'] = coders[i]['prev_rating'] + coders[i]['rating_change']