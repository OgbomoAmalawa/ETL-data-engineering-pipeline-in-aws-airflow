from collections.abc import Iterator

from ._pygit2 import Branch, Commit, Oid
from .enums import BranchType
from .repository import BaseRepository

class Branches:
    local: Branches
    remote: Branches
    def __init__(self, repository: BaseRepository, flag: BranchType = ..., commit: Commit | Oid | None = None) -> None: ...
    def __getitem__(self, name: str) -> Branch: ...
    def get(self, key: str) -> Branch | None: ...
    def __iter__(self) -> Iterator[str]: ...
    def create(self, name: str, commit: Commit, force: bool = False) -> Branch: ...
    def delete(self, name: str) -> None: ...
    def with_commit(self, commit: Commit | Oid | None) -> Branches: ...
    def __contains__(self, name: str) -> bool: ...
