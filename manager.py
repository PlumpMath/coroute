class Manager:
    tasks=[]
    def schedule_task(self, task):
        self.tasks.append(task)
    def unschedule_task(self, task):
        self.tasks.remove(task)
    def run(self):
        while True:
             try:
                 for taskid in range(len(self.tasks)):
                     try:
                         self.tasks[taskid].next()
                     except StopIteration:
                         self.unschedule_task(self.tasks[taskid])
                     except IndexError:
                         raise
             except IndexError:
                 pass
