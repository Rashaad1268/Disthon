from __future__ import annotations

from datetime import datetime

from ..types.snowflake import Snowflake
from pydantic import BaseModel


class DiscordObject(BaseModel):

    id: Snowflake
    created_at: datetime

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.id.id >> 22
