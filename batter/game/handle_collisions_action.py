import sys
import time
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        '''class constructor

        attributes:
            score (int): number of brick hit
        
        '''
        self.score = 0
        

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        # marquee.set_text("")
        for brick in bricks:
            velo = ball.get_velocity()
            if ball.get_position().equals(brick.get_position()):

                if brick.get_text() != ' ':
                    ball.set_velocity(velo.reverse())
                    brick.set_text(' ')
                    self.score += 1
                # x = velo[0]
                # y = velo[1]
                # new_direction =  Point(x, y)
        x = paddle.get_position().get_x()
        y = paddle.get_position().get_y()
        for _ in range(11):
            pos = Point(x, y)
            if ball.get_position().equals(pos):
                ball.set_velocity(velo.reverse())
            x += 1

        #this will cause the ball to reflect off the left and right borders
        for i in range(constants.MAX_Y):
            left = Point(constants.MAX_X - 1,i)
            right = Point(1,i)

            if ball.get_position().equals(right) or ball.get_position().equals(left):
                ball.set_velocity(velo.reverse(True))

        #this will handle collision with the top and bottom of the screen      
        for i in range(constants.MAX_X):
            top = Point(i,1)
            bottom = Point(i,constants.MAX_Y - 1)
            if ball.get_position().equals(top):
                ball.set_velocity(velo.reverse())
            elif ball.get_position().equals(bottom):
                sys.exit(f'Game Over \nScore: {self.score}')
