"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # self.brick_spacing = brick_spacing
        # self.brick_offset = brick_offset
        # self.brick_rows = brick_rows
        # self.brick_height = brick_height
        self.ball_radius = ball_radius
        self.paddle_width = paddle_width
        self.paddle_offset = paddle_offset
        self.paddle_height = paddle_height
        self.__dx = 0
        self.__dy = 0

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=self.window_width/2-paddle_width/2,
                            y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window_width/2-ball_radius, y=self.window_height/2-ball_radius)

        # Draw bricks
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for j in range(brick_rows):
            for i in range(brick_cols):
                self.brick_i = GRect(brick_width, brick_height)
                self.brick_i.filled = True
                self.brick_i.color = color[j // 2]
                self.brick_i.fill_color = color[j // 2]
                self.window.add(self.brick_i, x=i*(brick_width + brick_spacing),
                                y=brick_offset+j*(brick_spacing+brick_height))

        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)

    def start(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
        # if self.ball.x == self.window_width/2-self.ball_radius and self.ball.y == self.window_height/2-self.ball_radius:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def paddle_move(self, mouse):
        if mouse.x > self.window_width-self.paddle_width/2:
            self.paddle.x = self.window_width-self.paddle_width
        elif mouse.x < self.paddle_width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle_width/2
            self.paddle.y = self.window_height - self.paddle_offset - self.paddle_height

    def restart(self):
        self.window.add(self.ball, x=self.window_width/2-self.ball_radius, y=self.window_height/2-self.ball_radius)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def collision(self):
        # ball touches top edge of window
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        # ball touches two sides of window
        elif self.ball.x <= 0 or self.ball.x+2*self.ball_radius >= self.window_width:
            self.__dx = -self.__dx
        # ball touches paddle
        elif self.window.get_object_at(self.ball.x+self.ball_radius, self.ball.y+2*self.ball_radius+1):
            self.__dy = -self.__dy
        # ball touches bricks -> bounce & remove bricks
        else:
            if self.ball.y < self.window_height/2:  # avoid removing paddle
                # top and bottom
                if self.window.get_object_at(self.ball.x+self.ball_radius, self.ball.y-1) or \
                        self.window.get_object_at(self.ball.x+self.ball_radius, self.ball.y+2*self.ball_radius+1):
                    self.window.remove(self.window.get_object_at(self.ball.x+self.ball_radius, self.ball.y-1))
                    self.window.remove(self.window.get_object_at(self.ball.x+self.ball_radius, self.ball.y+2*self.ball_radius+1))
                    self.__dy = -self.__dy
                # left and right
                if self.window.get_object_at(self.ball.x-1, self.ball.y+self.ball_radius) or \
                        self.window.get_object_at(self.ball.x+2*self.ball_radius+1, self.ball.y+self.ball_radius):
                    self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
                    self.window.remove(self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y))
                    self.__dx = -self.__dx
