Snake Game AI

---
# The Idea:

Understand how Reinforcement Learning works in ML (Machine Learning).

<br>
</br>

# The Goal:

1. Learn the Basics of Pytorch
2. Build an Agent
3. Basics of Reinforcement Learning
4. Learn Deep Learning Algorithm

Deep Q Learning - Extends the Reinforcement Learning by using Deep Neural Network to predict the actions.



<br>
</br>

# Targets:

- [ ]  Learn the Theory
    - RL teaches the 'Agent' how to behave in a set environment based on how good it is performing.
- [ ]  Build the Enviroment
    - ...
- [ ]  Build the Agent
    - ...
- [ ]  Build the Model
    - ...


# Framework:

- [ ]  **Agent**
    - environment // game
    - model
  - *Training*
    - state = get_state(environment)
    - action = get_move(state):
      - model.predict()
    - reward, game_over, score = game.play_step(action)
    - new_state = get_state(environment)
    - remember
    - model.train()

- [ ]  **Environment // Game (Pygame)**
    - play_step(action)
      - reward, game_over, score

- [ ]  **Model (Pytorch)**
    - Linear_QNet (DQN)
      - model.predict(state)
        - action




# Mechanics:

- [ ]  Rewards
    - eat food: +10
    - game over: -10
    - elseL 0

- [ ]  Action (determines the next move)
    - [1,0,0]: keep-straight
    - [0,1,0]: true-right-turn
    - [0,0,1]: true-left-turn

- [ ]  State (Telling the 'snake' the information about the 'environment/game' or rules) // Calculations
    - 11 Values (for this enviroment/game)
      -  [
      -  danger straight, danger right, danger left,
      -  
      -  direction left, direction right,
      -  direction up, direction down,
      -  
      -  food left, food right,
      -  food up, food down,
      -  ]
      -  
         -  Sample Actions based on State
            -  if there is no danger nearby (collision, corner of enviroment)
            -  [0,0,0]: Take Action
            -  if there is a food at the right [left,right,up,down]
            -  [0,1,0,0]: Take Action


![alt text](01-Information-Images/Framework.PN?raw=true)

<br>
</br>
<br>
</br>
<p>
  <a href="https://www.linkedin.com/in/binoootuliao/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
  </a> &nbsp; 
  <a href="https://github.com/melbinoooo" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
  </a>
</p>