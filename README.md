# pong
The game pong, written in Python3 using the pygame SDL wrapper

There is one issue with the game so far which I have not resolved.
When you change the size of the game, the position of the paddles
and ball loose their place on screen, meaning they are not where
they should be.

The plan is to fix this later by fixing x and y position as a
number between 0 and 1 and then multiply that with the screens
size. That way, the position is always kept somewhat in the
same place.

You move the paddles with the W, S and UP and Down keys.
