from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
    BotToken: str


@dataclass
class Config:
    tg_bot: TgBot



def load_env(path: str = ".env") -> Config:

    env: Env = Env()
    env.read_env(path=path)

    return Config(
        tg_bot=TgBot(
            BotToken=env("BOT_TOKEN")
            )
    )