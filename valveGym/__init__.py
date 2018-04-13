from gym.envs.registration import register

register(
    id='valve-v0',
    entry_point='valveGym.envs:ValveEnv',
)
