from src.game_state import GameState


env = GameState()

while not env.game_over:
    legal_actions = env.get_legal_actions()
    action = agent.select_action(env.to_observation(), legal_actions)
    obs, reward, done, info = env.step(action)
    agent.learn(reward, obs)
