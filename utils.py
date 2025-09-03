import time
import random

def ascii_art():
    """Simple ASCII art function"""
    art = r'''
  _      _  __      ____                   _   
 | |    (_)/ _|    / __ \                 | |  
 | |     _| |_ ___| |  | | _   _  ___  ___| |__
 | |    | |  _/ _ \ |  | | | | | |/ _ \/ __| __|
 | |____| | ||  __/ |__| | | |_| |  __/\__ \ |_ 
 |______|_|_| \___|\____/\ \____| \___||___/\__|            

    '''
    print(art)

stages = [
    ("Undergrad", "Dove into engineering and learned to debug more than just code.."),
    ("Masters",  "Explored robotics at University of Maryland, learning how to bring skynet to life, through caffeinated late nights."),
    ("Research", "Started research at Oakridge National Lab: Played with LIDAR data, and VLMs and learnt to do research the right way from a wonderful team."),
    ("Now", "Current dungeon: Started PhD, trying to socialize and be more active. Difficulty: Hasn't escalated yet.")
]

plot_twists = [
    "Grinding games as a kid == secret training for debugging at 3 a.m.",
    "Speed-running game bosses == practice for conference/workshop deadlines.",
    "Realizes open-world exploration in games was the first step toward mapping real-world cities with ADAS datasets.",
    "Collecting loot == just early dataset wrangling.",
    "Rolling in Jiu Jitsu == just like debugging — you suffer, get stuck, but eventually find the escape."
]

def slow_print(text, delay=0.02):
    """Funtion for printing text slowly"""
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print() 


def my_adventure():
    ascii_art()
    slow_print("Welcome to My LifeQuest: The Polymath Path!\n")
    for stage, description in stages:
        input(f"\nPress ENTER to travel to {stage}...")
        slow_print(f"\n {stage}: {description}")
        if random.random() < 0.9: # to ensure some plot twist appears
            twist = random.choice(plot_twists)
            slow_print(f"\n Random lessons from gaming/life: {twist}")

    slow_print("\nFinal Boss: Can Bala truly become a polymath?")
    slow_print("Answer: Still grinding XP...")


if __name__ == "__main__":
    my_adventure()