# Convert the agent to a reflex based agent with a model. Afterwards take the sensors 
# away from the agents i.e. now the agent cannot perceive anything. Does your agent still 
# work? if so then why?

# Yes, the agent still works.
# This is because the model gives it memory of past states, so even without sensors it can
# keep track of which rooms need cleaning and where it should move next.


# Environment base class
from abc import ABC, abstractmethod


class Environment(ABC):
    """Abstract Environment class"""

    @abstractmethod
    def __init__(self, n):
        self.n = n

    @abstractmethod
    def executeStep(self, n=1):
        raise NotImplementedError("Action must be defined!")

    @abstractmethod
    def executeAll(self):
        raise NotImplementedError("Action must be defined!")

    def delay(self, n=100):
        self.delay = n


# Room class
class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status


# Abstract Agent
class Agent(ABC):
    """Abstract Agent"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def act(self):
        pass


# Vacuum Cleaner Agent with Model
class VacuumAgent(Agent):
    def __init__(self, n):
        """Constructor"""
        # Apna internal model (dictionary of rooms)
        self.model = {chr(65 + i): "dirty" for i in range(n)}  
        self.current_index = 0
        self.last_move = "right"

    def act(self):
        # Current room name
        current_room = chr(65 + self.current_index)

        # Agar room dirty hai to clean karo
        if self.model[current_room] == "dirty":
            self.model[current_room] = "clean"
            return "clean"

        # Warna move karo
        if self.current_index == 0:  # first room
            self.last_move = "right"
        elif self.current_index == len(self.model) - 1:  # last room
            self.last_move = "left"

        if self.last_move == "right":
            self.current_index += 1
        else:
            self.current_index -= 1

        return self.last_move


# N Room Vacuum Cleaner Environment
class NRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent, n):
        self.rooms = [Room(chr(65+i)) for i in range(n)]  
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""
        self.score = 0

    def executeStep(self):
        while True:
            self.displayPerception()
            res = self.agent.act()  
            self.action = res

            index = self.rooms.index(self.currentRoom)
            if res == "clean":
                if self.currentRoom.status == "dirty":
                    self.score += 25
                self.currentRoom.status = "clean"
            elif res == "right" and index < len(self.rooms) - 1:
                self.currentRoom = self.rooms[index + 1]
                self.score -= 1
            elif res == "left" and index > 0:
                self.currentRoom = self.rooms[index - 1]
                self.score -= 1

            for room in self.rooms:
                if room.status == "dirty":
                    self.score -= 10

            self.displayAction()
            print(f"Score after step {self.step}: {self.score}\n")
            self.step += 1

            if all(room.status == "clean" for room in self.rooms):
                print("All rooms are clean. Agent stops.")
                print(f"Final Score: {self.score}")
                return

    def executeAll(self):
        raise NotImplementedError("Action must be defined!")

    def displayPerception(self):
        print(
            "Perception at step %d is [%s, %s]"
            % (self.step, self.currentRoom.status, self.currentRoom.location)
        )

    def displayAction(self):
        print(
            "------- Action taken at step %d is [%s]" % (self.step, self.action)
        )

    def delay(self, n=100):
        self.delay = n


# Test Program
if __name__ == "__main__":
    vcagent = VacuumAgent(3)  
    env = NRoomVacuumCleanerEnvironment(vcagent, 3)
    env.executeStep()
