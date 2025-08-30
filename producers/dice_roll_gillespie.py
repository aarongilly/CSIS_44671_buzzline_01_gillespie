"""
dice_roll_gillespie.py

Generate some values simulating rolls of pairs of dice. 
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.

    It doesn't need any outside information, so the parentheses are empty.
    It returns an integer, so we specify that in the function signature.

    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented.

    Define a local variable to hold the value of the environment variable
    os.getenv() is a function that fetches the value of an environment variable
    os.getenv() always returns a string 
    We convert the return value to an integer using the built-in Python int() function
    To use handy functions like this, import the os module 
    from the Python Standard Library (see above).
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating dice roll values
NUM_DICE: int = 2
NUM_SIDES: int = 6 

#####################################
# Define a function to generate dice roll values
#####################################


def generate_messages():
    """
    Generate a stream of dice roll values.

    This function uses a generator, which yields one buzz at a time.
    Generators are memory-efficient because they produce items on the fly
    rather than creating a full list in memory.

    Because this function uses a while True loop, it will run continuously 
    until we close the window or hit CTRL c (CMD c on Mac/Linux).
    """
    while True:
        rolls: list = [
            random.randint(1, NUM_SIDES) for _ in range(NUM_DICE)
        ]
        total: int = sum(rolls)
        yield f"Rolled {rolls} for a total of {total}"


def set_dice_sides(sides: int) -> None:
    """
    Set the number of sides on the dice.

    This function modifies the global variable NUM_SIDES.
    It takes an integer argument 'sides' and returns None.
    """
    global NUM_SIDES
    NUM_SIDES = sides
    logger.info(f"Number of sides on the dice set to {NUM_SIDES}.")

def set_num_dice(num: int) -> None:
    """
    Set the number of dice to roll.

    This function modifies the global variable NUM_DICE.
    It takes an integer argument 'num' and returns None.
    """
    global NUM_DICE
    NUM_DICE = num
    logger.info(f"Number of dice to roll set to {NUM_DICE}.")

#####################################
# Define main() function to run this producer.
#####################################

def main() -> None:
    """
    Main entry point for this producer.

    It doesn't need any outside information, so the parentheses are empty.
    It doesn't return anything, so we say the return type is None.   
    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented. 
    This is a multiline docstring - a special type of comment 
    that explains what the function does.
    """

    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    # Assign the return value to a variable called interval_secs
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        # Use the time module to pause execution for a specified number of seconds
        # The time.sleep() function takes a single argument: the number of seconds to pause
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()
