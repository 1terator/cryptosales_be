import hashlib
import hmac
import typing
from urllib.parse import unquote, parse_qs


def get_telegram_bot_secret_key(token: str, msg: str = "WebAppData") -> str:
    return hmac.new(token.encode(), msg.encode(), digestmod=hashlib.sha256).hexdigest()


def parse_telegram_app_init_data(init_data: str) -> typing.Dict:
    return {k: v[0] for k, v in parse_qs(init_data).items()}


def validate_telegram_app_data(data_check_string: str, token: str) -> bool:
    secret_key, hash_ = get_telegram_bot_secret_key(token), parse_telegram_app_init_data(data_check_string)["hash"]
    data_check_string = sorted(
        [chunk.split("=") for chunk in unquote(data_check_string).split("&") if chunk[:len("hash=")] != "hash="],
        key=lambda x: x[0]
    )
    data_check_string = "\n".join([f"{rec[0]}={rec[1]}" for rec in data_check_string])
    calculated_hash = hmac.new(secret_key.encode(), data_check_string.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(hash_, calculated_hash)
