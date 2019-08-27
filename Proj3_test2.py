# ----------------- Coin Estimator -----------------
# allow user to input total weight of each type of coin
# print out how many each type of wrapper they need
# print how many coins they have
# print estimated total value

# penny = 2.5 g, 50/roll
# nickel = 5.0 g, 40/roll
# dime = 2.268 g, 50/roll
# quarter = 5.67 g, 40/roll

from dataclasses import dataclass
from typing import Optional


@dataclass
class Coin:
    name: str
    gram_per_coin: float
    total_grams: Optional[float]
    value_per_coin: int

    # GEYBWEE WAS HEUH
    @property
    def num_coins(self):
        return self.total_grams  / self.gram_per_coin


penny = Coin(name="penny", gram_per_coin=2.5, value_per_coin=1, total_grams=None)
nickel = Coin(name="nickel", gram_per_coin=5.0, value_per_coin=5, total_grams=None)
dime = Coin(name="dime", gram_per_coin=2.268, value_per_coin=10, total_grams=None)
quarter = Coin(name="quarter", gram_per_coin=5.67, value_per_coin=25, total_grams=None)

# coins = [penny, nickel, dime, quarter]
coins = [quarter]
for coin in coins:
    user_input = input(f"How many grams of {coin.name} do you have?")
    coin.total_grams = float(user_input)
    print(f"You have this many {coin.name}")
    num_coins = coin.total_grams/coin.gram_per_coin
    print(num_coins)
    print(f"{coin.name} value is {num_coins*coin.value_per_coin}")
