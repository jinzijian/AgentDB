class Task:
    def __init__(self, name, description, plan_memory=None, parent=None, level=0):
        self.name = name
        self.description = description
        self.parent = parent
        self.level = level
        self.act_memory = None
        self.context_memory = None
        self.plan_memory = []

        if plan_memory:
            self.init_subtasks(plan_memory)

    def init_subtasks(self, plan_memory):
        for subtask_info in plan_memory:
            subtask = self.add_subtask(subtask_info['name'], subtask_info['description'])
            if 'plan_memory' in subtask_info:  # Check if there is further nesting
                subtask.init_subtasks(subtask_info['plan_memory'])

    def add_act_memory(self, act_memory):
        self.act_memory = act_memory
    
    def add_context_memory(self, context_memory):
        self.context_memory = context_memory

    def add_subtask(self, name, description):
        subtask = Task(name, description, parent=self, level=self.level + 1)
        self.plan_memory.append(subtask)
        return subtask

    def find_parent(self):
        return self.parent

    def __str__(self):
        ret = "\t" * self.level + repr(self.name) + " : " + repr(self.description) + " [Level: " + str(self.level) + "]" + "\n"
        for subtask in self.plan_memory:
            ret += subtask.__str__()
        return ret

if __name__ == "__main__":
    # Initialize the root task with nested subtasks
    initial_plan_memory = [
        {
            'name': 'Subtask1', 
            'description': 'Sub1Description',
            'plan_memory': [
                {
                    'name': 'Subtask1_1', 
                    'description': 'Sub1_1Description',
                    'plan_memory': [
                        {'name': 'Subtask1_1_1', 'description': 'Sub1_1_1Description'}
                    ]
                },
                {'name': 'Subtask1_2', 'description': 'Sub1_2Description'}
            ]
        },
        {'name': 'Subtask2', 'description': 'Sub2Description'}
    ]
    root_task = Task('RootTask', 'RootDescription', plan_memory=initial_plan_memory)

    # Print the entire task hierarchy
    print(root_task)
