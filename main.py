# main.py
from RPS_game import play, quincy, mrugesh, abbey, kris
from RPS import player

# Example: play 1000 games vs each opponent
print("Playing against Quincy...")
play(player, quincy, 1000)

print("\nPlaying against Mrugesh...")
play(player, mrugesh, 1000)

print("\nPlaying against Abbey...")
play(player, abbey, 1000)

print("\nPlaying against Kris...")
play(player, kris, 1000)

# Uncomment below to run FCC unit tests automatically
# import test_module
