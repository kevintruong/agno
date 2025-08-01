from abc import ABC, abstractmethod
from typing import List, Literal, Optional

from agno.storage.session import Session


class Storage(ABC):
    def __init__(self, mode: Optional[Literal["agent", "team", "workflow", "workflow_v2"]] = "agent"):
        self._mode: Literal["agent", "team", "workflow", "workflow_v2"] = "agent" if mode is None else mode

    @property
    def mode(self) -> Literal["agent", "team", "workflow", "workflow_v2"]:
        """Get the mode of the storage."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional[Literal["agent", "team", "workflow", "workflow_v2"]]) -> None:
        """Set the mode of the storage."""
        self._mode = "agent" if value is None else value

    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self, session_id: str, user_id: Optional[str] = None) -> Optional[Session]:
        raise NotImplementedError

    @abstractmethod
    def get_all_session_ids(self, user_id: Optional[str] = None, entity_id: Optional[str] = None) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def get_all_sessions(self, user_id: Optional[str] = None, entity_id: Optional[str] = None) -> List[Session]:
        raise NotImplementedError

    @abstractmethod
    def get_recent_sessions(
        self,
        user_id: Optional[str] = None,
        entity_id: Optional[str] = None,
        limit: Optional[int] = 2,
    ) -> List[Session]:
        raise NotImplementedError

    @abstractmethod
    def upsert(self, session: Session) -> Optional[Session]:
        raise NotImplementedError

    @abstractmethod
    def delete_session(self, session_id: Optional[str] = None):
        raise NotImplementedError

    @abstractmethod
    def drop(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def upgrade_schema(self) -> None:
        raise NotImplementedError
