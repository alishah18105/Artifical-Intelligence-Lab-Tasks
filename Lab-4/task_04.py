# Score your agent, -1 points for moving from a room, +25 points to clean a room 
# that is dirty, and -10 points if a room is dirty. The scoring will take place after every 1 
# second 

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
            
        


# N Room Vacuum Cleaner Environment
class NRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent,n):
        self.rooms = [Room(chr(65+i)) for i in range(n)]  # Create rooms A, B, C
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""
        self.score = 0

    def executeStep(self):
        while True:
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            index = self.rooms.index(self.currentRoom)
            if res == "clean":
                if self.currentRoom.status == "dirty":
                    self.score += 25
                self.currentRoom.status = "clean"
            if res == "right" and index < len(self.rooms) - 1:
                self.currentRoom = self.rooms[(index + 1)]
                self.score -= 1
            elif res == "left" and index > 0:
                self.currentRoom = self.rooms[(index - 1)]
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
    vcagent = VacuumAgent()
    env = NRoomVacuumCleanerEnvironment(vcagent,3)
    env.executeStep()
