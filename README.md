# pong
The game pong, written in Python3 using the pygame SDL wrapper

You move the paddles with the W, S and UP and Down keys.
You start the the ball with space.


## TODO

Since, the game currently, doesn't get any harder as time goes by,
the idea is to increase the velocity of the ball the longer
the two players are able to keep the ball going forth and back.

I made the game with the idea that the game would be resizable.
For this reason, no sprite or coordinate is written directly as
number of pixels. Everything is relative to the screen size and
ratios. This means, that making the game resizable at this point
in time should be relatively easy. One just need to pick up on
the event and trigger all the sprites in the game to change size
and position according to the new screen size.
