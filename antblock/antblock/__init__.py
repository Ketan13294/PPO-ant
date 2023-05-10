from gym.envs.registration import make, register, registry, spec

register(
    id="antblock",
    entry_point="antblock.envs:AntBlockEnv",
    max_episode_steps=2000,
)