from task import Task


class Core:
    def __init__(self):
        self.is_running = False
        self.running_task = None


class Machine:
    def __init__(self, id, core_number):
        self.id = id
        self.core_number = core_number
        self.cores = [Core() for _ in range(1, core_number + 1)]
        self.is_vacant = True
        self.is_reserved = -1
        self.reserve_job = None

    def assign_task(self, task: Task):
        for core in self.cores:
            if not core.is_running:
                core.running_task = task
                core.is_running = True

    def reset(self):
        self.is_vacant = True
        for core in self.cores:
            core.running_task = None
            core.is_running = False
