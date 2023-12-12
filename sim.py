import game
import numpy as np
SIM_TIME=1000
WIDTH_X=500
HEIGHT_Y=500

def simulate_environment(test_env: game.Environment) -> None:
    print(test_env.env.shape)

test_env = game.Environment(HEIGHT_Y,WIDTH_X)
simulate_environment(test_env)