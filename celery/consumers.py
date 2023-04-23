from worker import app
from engines import Algorithm 
# from tasks import func

class Consumer():
    agent = app.register_task(Algorithm())
    def __init__(self):
        print("* Consumer is instanced")
        # self.agent = Algorithm()
        
    def set(self):
        print("* CONSUMER SET")
        self.agent.set()

    def play(self):
        print("* CONSUMER play!")
        # self.agent.apply_async()
        self.agent.apply_async(args=({"a": 1, "b": 2, "c": 3}, {"aa": 11, "bb": 22, "cc": 33}, ))
        print("* CONSUMER done")


