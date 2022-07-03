import pygame
import random
from enum import Enum
from collections import namedtuple

# numpy
import numpy as np

import os
os.chdir(r'01-Reinforcement Learning\01-Snake Game AI')

# initalize pygame module
pygame.init()

font = pygame.font.Font('arial.ttf', 25)

Point = namedtuple('Point', 'x, y')

# Todo for AI
# reset function - Agent should be able to reset the game
# reward - Implement a reward system
# play(action) -> direction | Change the play function
# game_iteration - keep track of the game
# is_collision - change check if collision


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
BLOCK_SIZE = 20
SPEED = 20

# rgb Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # 1 init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()
        

    def reset(self):
        # 2 init game state
        self.direction = Direction.RIGHT
        # 3 init snake body position
        self.head = Point(self.w/2, self.h/2) # Place at the center
        self.snake = [self.head, 
                    Point(self.head.x-BLOCK_SIZE, self.head.y),
                    Point(self.head.x-(2*BLOCK_SIZE), self.head.y)] # Place two body initially starting from first left of center(which is position of snake head); therefore 3 blocks (1 head, 2 body)
        # 4 init score
        self.score = 0
        # 5 init food
        self.food = None
        self._place_food() # Helper || Randomize food position within the display
        self.frame_iteration = 0
        
        
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE # won't go far below 0, and go above self.w
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE # won't go far below 0, and go above self.y
        self.food = Point(x, y)
        # Check if the _place_food position is as the same as snake position then run the self.place_food() randomize position again.
        if self.food in self.snake:
            self._place_food()
        
    # Instances of Steps: Current | one at a time
    def play_step(self, action):
        self.frame_iteration += 1
        # 1st get user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 2. move based on user input above
        self._move(action) # update the head
        self.snake.insert(0, self.head) # update snake body based on self.head position
        
        # 3. check if game over
        reward = 0
        game_over = False
        if self._is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score
            
        # 4. place new food or just move
        
        # If head position is as the same as food position
        # Food object became the Head object
        if self.head == self.food:
            # Add score
            self.score += 1
            reward = 10
            # run _place_food() randomize food position
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return reward, game_over, self.score
    
    def _is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # hits boundary
        # if self head exceeds to the width number = out of bounds
        # if self head exceeds to the height number = out of bounds
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        # if self head has been the same position as snake index [1] onwards || snake index[0] is head
        if pt in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self):
        # First
        self.display.fill(BLACK)
        
        # Second
        for pt in self.snake:
            # Highlight of snake body
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            # base of snake body
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        # Third
        # Food
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, WHITE)
        
        # Fourth
        self.display.blit(text, [0, 0])
        # Fifth
        pygame.display.flip()
        
    def _move(self, action):
        # [straight, right, left] - Action
        
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)
        
        if np.array_equal(action,[1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action,[0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn | r -> d -> l -> u
        else: # [0,0,1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn | r -> u -> l -> d
        
        
        self.direction = new_dir
        
        
        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)
            

