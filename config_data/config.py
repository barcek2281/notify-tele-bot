from dataclasses import dataclass

from environs import Env

@dataclass
class TgBotConfig:
    BotToken: str


@dataclass
class DataBaseConfig:
    Uri: str
    Login: str
    Password: str
    Port: str


@dataclass
class LogConfig:
    Level: str
    Format: str


@dataclass
class Config:
    tg_bot: TgBotConfig
    log_config: LogConfig
    db_config: DataBaseConfig



def load_env(path: str = ".env") -> Config:

    env: Env = Env()
    env.read_env(path=path)

    return Config(
        tg_bot=TgBotConfig(
            BotToken=env("BOT_TOKEN")
            ),
        log_config=LogConfig(
            Level=env("LOG_LEVEL"),
            Format=env("LOG_FORMAT")
        ),
        db_config=DataBaseConfig(
            Uri=env("DB_URI"),
            Login=env("DB_LOGIN"),
            Password=env("DB_PASSWORD"),
            Port=env("DB_PORT")
        )
    )