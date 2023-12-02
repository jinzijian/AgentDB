from task import Task
def refine_plan(task: Task) -> Task:
    """
    更新给定子任务的爲任务的plan_memory，并为新的子任务正确设置爲节点。

    参数:
    task (Task): 要更新其爲任务的子任务。

    返回:
    Task: 经过更新后的根任务。
    """
    # 确认有爲任务存在
    if not task.parent:
        return None  # 如果没有爲任务，返回None或原始任务

    # 创建新的子任务列表，为每个新任务指定爲节点
    new_plan_memory = [
        Task('NewSubtask1', 'NewDescription1', parent=task.parent, level=task.level),
        Task('NewSubtask2', 'NewDescription2', parent=task.parent, level=task.level)
    ]

    # 更新爲任务的plan_memory
    task.parent.plan_memory = new_plan_memory

    # 寻找并返回根任务
    root_task = task.parent
    while root_task.parent is not None:
        root_task = root_task.parent
    return root_task

# 用法示例
if __name__ == "__main__":
    # 创建一个任务结构
    root_task = Task('RootTask', 'RootDescription')
    subtask = root_task.add_subtask('Subtask1', 'Sub1Description')
    subsubtask = subtask.add_subtask('Subtask1_1', 'Sub1_1Description')

    # 打印初始任务结构
    print("初始任务结构:")
    print(root_task)

    # 应用 refine_plan 函数
    new_plan_memory = [
        Task('NewSubtask1', 'NewDescription1'),
        Task('NewSubtask2', 'NewDescription2')
    ]

    # 假设 refine_plan 函数会更新父任务的 plan_memory
    refined_task = refine_plan(subsubtask)
    
    # 打印更新后的任务结构
    print("\n更新后的任务结构:")
    print(refined_task)