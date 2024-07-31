from enum import Enum

class TokenDuration(Enum):
    ACCESS_TOKEN_EXPIRATION = 10 * 60   # 10 minutes
    REFRESH_TOKEN_EXPIRATION = 24 * 60 * 60  # 24 hours
