# Convert the environment to a ‘n’ room environment where n >= 2 

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
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass


# Vacuum Cleaner Agent
class VacuumAgent(Agent):
    def __init__(self):
        """Constructor"""
        self.environment = None
        self.last_move = None
        self.direction = "right"

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == "dirty":
            return "clean"
        index = self.environment.rooms.index(self.environment.currentRoom)
        n = len(self.environment.rooms)

        if index == 0:  # First room
            self.last_move = "right"
        elif index == n - 1:  # Last room
            self.last_move = "left"

        return self.last_move
            
        


# Two Room Vacuum Cleaner Environment
class NRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent,n):
        self.rooms = [Room(chr(65+i)) for i in range(n)]  # Create rooms A, B, C
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            index = self.rooms.index(self.currentRoom)
            if res == "clean":
                self.currentRoom.status = "clean"
            if res == "right":
                self.currentRoom = self.rooms[(index + 1)]
            elif res == "left":
                self.currentRoom = self.rooms[(index - 1)]
            

            self.displayAction()
            self.step += 1

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
    vcagent = VacuumAgent()
    env = NRoomVacuumCleanerEnvironment(vcagent,5)
    env.executeStep(10)
