# AgentDB
A Database Framework for Lifelong Learning and Cognitive System Transition of AI Agents
# Motivation

## 灵感来源

1. **Lifelong Memory Management**：现有模型通常是无状态的，但人类的决策和行为受到过去经历的影响，引入lifelong记忆管理为AI Agent提供了持续学习和经验积累的可能。
2. **System1 → System2 → System1**
    - 通过学习，复杂的任务可以逐渐变得直觉化，模拟从System2（逻辑思考）到System1（本能反应）的转变过程，从而提升处理复杂任务的效率和准确性。
    - 人类在学习新技能时，通常需要先熟练掌握子技能，再逐步学习和掌握高级技能。由于人的注意力和学习能力是有限的，不能同时学习和掌握多个技能，这也反映了System1到System2再到System1的转变过程，即通过重复练习和应用，将初学时需要逻辑思考的技能转变为熟练后的本能反应。

## 目前 AI Agent 存在的问题

**宏观问题：可用性不高，复杂任务执行的不好**

**具体原因**：

1. **上下文长度有限制**：导致长篇信息的处理不足。
2. context lost in the middle：中间部分容易被忽略，缺乏重要信息的识别和保留。
3. **缺乏对运行时记忆的整理和归纳**：使得历史信息利用不足，缺乏周期性的评估和整理机制。
4. **ToT (Tree of Thoughts) 类型方法存在重复问题处理不佳**：需要一种机制来识别和记住先前解决过的问题和解决方案，避免重复处理。

## 解决思路

设计一个专用于AI Agent的DB Framework，通过融合RAG技术，结合现有基于React、Reflexion等方法的AI Agent框架，以实现以下目标：

1. **长期记忆管理与知识结构维护**
    1. **经验积累**：通过长期记忆管理，模型能够在处理不同任务时积累和保留经验，形成一个“经验库”。
    2. **数据库框架设计**：实现一个特定的数据库框架，用于存储和管理模型在不同任务和时间点上获得的知识和经验。
    3. **周期性记忆整理**：开发一种机制，能够周期性地评估、整理和归纳运行记忆，以保持模型的知识结构清晰。
    4. **信息利用效率提升**：通过上述措施，提高模型的信息利用效率，使其能够更有效地利用过往的知识和经验进行决策和任务处理。
2. **使Agent具备状态记忆功能**，让其在处理任务时能够依据过往经验做出更为准确和高效的决策，实现类似人类通过记忆和经验不断优化决策能力的效果。通过状态记忆的实现，Agent能够像人类一样，利用累积的知识和经验，在面对新任务或问题时做出更为合理和高效的响应。
3. **开发新的上下文管理机制，通过设计能够识别和保留重要上下文的算法，同时排除不重要的信息。**

# 核心方法 & 创新

### 算法流程

分层 RAG： 更新 Memory 时，分层存储 & 整合不同的信息

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/674bb51f-71c8-4684-b941-0f6f75174bad/d80796e1-402f-4f4f-bd0b-5bb3dbb71c73/Untitled.png)

### Potential Risk

- 总结出来的知识不够 General
    - For example，床下有手电筒让机器人去找，knowledge 应该是床下也可以藏东西，而不是手电筒在床下（更改 context 会失效）

# Task

| Math | https://github.com/hendrycks/math |
| --- | --- |
| Decision Making | https://alfworld.github.io/ |
| Hotpot Qa | https://hotpotqa.github.io/ |
| StrategyQA | https://allenai.org/data/strategyqa |
| BamboogleQA | https://docs.google.com/spreadsheets/d/1-mJ7-ad_GLac_J_5AS2cV2nqmyLU2Pym8Q_mHmbE15A/edit?usp=sharing |
| Math GSM8K | https://paperswithcode.com/dataset/gsm8k |
| NarrativeQA |  |

# 工程设计

1. 数据结构
    1. 树形结构, task里套task(plan里其实是list of subtask)
    2. 
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/674bb51f-71c8-4684-b941-0f6f75174bad/59bc4700-03d2-4525-9911-7a120244d160/Untitled.png)
    
2. 基础能力
    1. 连接Vector DB
    2. 调用LLM(外部传入)
    3. 存
    4. 取
3. 数据库能力
    1. Update Memory
        1. 给一段新的memory和之前数据库里召回的top k做比较
        2. 比较后LLM自己判断是否需要创建还是合并还是删除修改)
    2. RAG能力
        1. 从数据库中选择和当前task相关的内容
    3. init task(main_task, plan): 一个task和plan进来, 从plan里生成subtask, 生成树形的数据结构 task里套subtask
4. Agent memory能力
    1. find_similar_task(task)(返回topk similar task 里面包含 plan ,act, context memory)
    2. refine_react(task, act_context, 改进函数)
        1. 召回rag相关内容, 召回parent task的plan memory
        2. 输入是task(main, sub均可以)
        3. 如果有相关rag内容, 则对比分析(覆盖)
        4. 对当前轮次的context做处理挑重点放入下一轮react(覆盖)
    3. refine_current_task_plan(TASK, ACT)
    4. refine_parent_task_plan(task, act_context)
        1. 若多次执行不成功最后判定失败
        2. 寻找parent task
        3. 更改parent task得plan(需要覆盖) 并重复执行
5. Framework侧适配(如何自动同步且打通  手动写入 显式提供接口)
    1. act 内容自动存入act_memory
    2. plan内容存入plan_memory
