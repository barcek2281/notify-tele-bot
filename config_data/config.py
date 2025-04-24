from dataclasses import dataclass

from environs import Env

@dataclass
class Config:
    BotToken: str

def load_env(path: str = ".env") -> Config:

    env: Env = Env()
    env.read_env(path=path)

    return Config(
        BotToken=env("BOT_TOKEN")
    )