## Frozen Lake Game using Q Learnig
Frozen Lake is a classic problem in the field of Reinforcement Learning, where an agent learns to navigate a grid-world environment by taking actions and receiving rewards. In the Frozen Lake problem, the agent must learn to move from the start state to the goal state while avoiding the holes in the ice. The agent has four possible actions at each state: moving up, down, left, or right. The rewards for each action are either +1 for reaching the goal or -1 for falling into a hole. The objective of the agent is to maximize the total reward by finding the optimal policy, which is a mapping from states to actions that the agent should take in each state.
Symbol	Meaning:

S	Starting point, safe

F	Frozen surface, safe

H	Hole, fall to your doom

G	Goal, where the frisbee is located

Used a q learning based strategy using a decaying epsilon parameter which controls exploration vs. exploitation.
The agent automatically learns the correct approach to reach the goal state without being explicitly programmed.
