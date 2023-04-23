from celery import Task, shared_task
import time 
import argparse

class Algorithm(Task):
    def __init__(self):
        super().__init__()
        print("foo is instanced")
        self._vars = argparse.Namespace()
        self.a = 0
        self.b = 0
                
    def set(self):
        print("*** set")
        self._vars.a = 10
        self._vars.b = 10
        self.a = -10
        self.b = -10
        
    def train(self):
        self.set()
        for idx in range(3):
            print(idx, self.a, self.b)
            print(self._vars.a, self._vars.b)
            time.sleep(1)
        return "DONE"
    
    def run(self, *args, **kwargs):
        print("RUN")
        print(args)
        print(kwargs)
        # self.set()
        return self.train()
    
# class foo():
#     def __init__(self):
#         print("foo is instanced")
#         self.abc = 0
        
#     def set(self):
#         print("*** SET")
        
#     def train(self, x, y):
#         print("*** TRAIN")
#         for idx in range(3):
#             print(idx)
#             time.sleep(1)
#         return x + y
