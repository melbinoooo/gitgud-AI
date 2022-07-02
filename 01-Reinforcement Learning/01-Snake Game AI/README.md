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

<br>
</br>


# Mechanics:

- [ ]  Rewards
    - eat food: +10
    - game over: -10
    - else: 0

- [ ]  Action (determines the next move)
    - [1,0,0] keep-straight
    - [0,1,0] true-right-turn
    - [0,0,1] true-left-turn

- [ ]  **State** (Telling the 'snake' the information about the 'environment/game' or rules) // Calculations
    - **11 Values** (for this enviroment/game)
    - boolean values (True/False)
      -  [
      -  (1)danger straight, (2)danger right, (3)danger left,
      -  
      -  (4)direction left, (5)direction right,
      -  (6)direction up, (7)direction down,
      -  
      -  (8)food left, (9)food right,
      -  (10)food up, (11)food down,
      -  ]
      -  
         -  Sample Actions based on State
            -  if there is no danger nearby (collision, corner of enviroment)
            -  [0,0,0] - Take Action
            -  if there is a food at the right [left,right,up,down]
            -  [0,1,0,0] - Take Action



<br>
</br>

# Framework:

- [ ]  **Model** Feed forward Neural Net
    - has 3 layers
      - Input
        - size: based on number(values) of states (in this project, we have 11 states)
      - Hidden
        - size: based on our computation requirements
      - Output
        - 3 output: in order to predict the action (maybe probability values(<1(0.90,0.60...)) or an max integer value to set an action based number which is e.g. [0,1,0,0] - go right)

![Framework](01-Information-Images/Framework.PNG?raw=true)


<br>
</br>

# **Deep Q Learning**: (Q-Value = Quality of Action)

- [ ]  **Training Framework** 
    - [0] Initialize the Q Value (a.k.a the model)
    - **Training Loop Starts here:** 
    - [1] Choose Action (model.predict(state))
      - or a random move, if the Q Value is low or the training is at the beginning.
    - [2] Perform the Winning Action
    - [3] Measure Reward
      - Based on the reward system, we update the Q Value
    - [4] Update Q Value (+train Model)
      - Add a **loss function or determinant to start over** (low score, collisions, etc), to continue the training loop.

- [ ]  **Loss Function: Bellman Equation** 
    - Initialize the Q Value (a.k.a the model)
    - Qnew(s,a) **=** Q(s,a) **+** α [R(s', a') **+** γ maxQ'(s′,a′) **−** Q(s,a)]
      - 
      - Qnew(s,a) = New Resulting Value for the state and the action.
      - Q(s,a) = Current Q Value
      - α = Learning Rate
      - R(s', a') = Reward for taking (made) this* action at (made)this* state value
      - γ = Discount Rate
      - maxQ'(s′,a′) **−** Q(s,a) = Maximum Expected Future Reward given the **new** (**s**) *a.k.a state* and all possible (**a**) *a.k.a action* of that new specific state.

- [ ]  **Simplification: Bellman Equation** 
    - Updating the Q Value
      - Q = model.predict(state[0]) 
      - Qnew = R + γ (maxQ(state[1])) 
    - Loss Function
      - loss = (Qnew - Q)²
        - *Mean Squared Error*


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