from environs import Env
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str
    admin_id: int

@dataclass
class Config:
    tg_bot: TgBot

def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),  # ← ВНИМАНИЕ: здесь должно быть 'BOT_TOKEN', а не сам токен!
            admin_id=env.int('ADMIN_ID')  # ← Здесь 'ADMIN_ID'
        )
    )