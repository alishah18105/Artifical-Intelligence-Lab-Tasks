#Run the two room vacuum cleaner agent program and understand it. Convert the program to a 
# Three room environment.

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

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == "dirty":
            return "clean"
        elif self.environment.currentRoom.location == "A":
            self.last_move = "right"
            return self.last_move
        
        elif self.environment.currentRoom.location == "B" and self.last_move == "right":
            self.last_move = "right"
            return self.last_move
        
        elif self.environment.currentRoom.location == "B" and self.last_move == "left":
            self.last_move = "left"
            return self.last_move
        
        elif self.environment.currentRoom.location == "C":
            self.last_move = "left"
            return self.last_move
        
        


# Three Room Vacuum Cleaner Environment
class ThreeRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.r1 = Room("A", "dirty")
        self.r2 = Room("B", "dirty")
        self.r3 = Room("C", "dirty")
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == "clean":
                self.currentRoom.status = "clean"
            elif res == "right" and self.currentRoom.location == "A":
                self.currentRoom = self.r2
            elif res == "right" and self.currentRoom.location == "B":
                self.currentRoom = self.r3
            elif res == "left" and self.currentRoom.location == "C":
                self.currentRoom = self.r2
            elif res == "left" and self.currentRoom.location == "B":
                self.currentRoom = self.r1

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
    env = ThreeRoomVacuumCleanerEnvironment(vcagent)
    env.executeStep(10)
