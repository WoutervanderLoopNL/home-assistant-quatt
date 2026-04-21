"""DataUpdateCoordinator for the Quatt Home Battery hub."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry

from .const import LOGGER
from .coordinator import QuattDataUpdateCoordinator


class QuattHomeBatteryDataUpdateCoordinator(QuattDataUpdateCoordinator):
    """Coordinator for fetching home battery status from the remote API."""

    config_entry: ConfigEntry

    def get_value(self, value_path: str, default: Any | None = None) -> Any:
        """Retrieve a value by dot notation from the home battery response."""
        parts = value_path.split(".")
        current_node = self.data

        for part in parts:
            if current_node is None:
                return default
            if isinstance(current_node, dict) and part in current_node:
                current_node = current_node[part]
            else:
                LOGGER.debug("Could not find %s of %s", part, value_path)
                return default

        return current_node

    # The abstract "heatpump"-specific helpers don't apply to the home battery,
    # but they must be implemented for the base class.
    def heatpump_1_active(self) -> bool:
        """Home battery hub has no heatpumps."""
        return False

    def heatpump_2_active(self) -> bool:
        """Home battery hub has no heatpumps."""
        return False

    def all_electric_active(self) -> bool:
        """Home battery hub has no heatpumps."""
        return False

    def is_boiler_opentherm(self) -> bool:
        """Home battery hub has no boiler."""
        return False
