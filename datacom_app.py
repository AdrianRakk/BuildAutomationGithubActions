import time
import random


class DatacomApplication:

    def __init__(self, role):
        self._role = role # Role applied for
        self._positions = ["Cloud Engineer", "DevOps Engineer", "Software Developer"] # Available IT positions

    def checkRole(self):
        # Check whether the role is available
        for position in self._positions:
            if position.lower() == self._role.lower(): # Convert both strings to lower case
                return True # The role is available
        
        return False # The role is not available

    def checkHired(self):

        # Check first whether the position is available
        if self.checkRole():
            is_hired = random.choice([True, False]) # Generate a random true or false variable
        else:
            is_hired = False

        if is_hired:
            print("Woohoo! I got hired!")
        else:
            print("Oh no! I will try again!")

    def applyToDatacom(self):
        print("Applying for a job at Datacom...")
        time.sleep(1)

        print("Filling out the application form...")
        time.sleep(1)

        print("Writing a development workflow for GitHub Actions to impress them...")
        time.sleep(1)

        print("Submitting the application...")
        time.sleep(1)
