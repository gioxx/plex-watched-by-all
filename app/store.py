from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Set, Tuple, List, Optional
import time

@dataclass
class Cache:
    """
    In-memory cache for computed results.
    """
    last_refresh_ts: float = 0.0
    users: Dict[str, str] = field(default_factory=dict)  # user_id -> friendly_name

    # If empty, all users are considered. Otherwise only these user_ids.
    selected_user_ids: Set[str] = field(default_factory=set)

    # Completion map: (user_id, rating_key) -> True
    completed: Set[Tuple[str, str]] = field(default_factory=set)

    # Movie keys seen in history
    movies: Set[str] = field(default_factory=set)

    # Show keys seen in history (grandparent/show rating key)
    shows: Set[str] = field(default_factory=set)

    # Plex episode list per show
    show_episodes: Dict[str, List[str]] = field(default_factory=dict)

    # Precomputed results
    movies_by_all: List[str] = field(default_factory=list)   # rating keys
    shows_by_all: List[str] = field(default_factory=list)    # show rating keys

    def is_stale(self, refresh_minutes: int) -> bool:
        if self.last_refresh_ts <= 0:
            return True
        return (time.time() - self.last_refresh_ts) > (refresh_minutes * 60)