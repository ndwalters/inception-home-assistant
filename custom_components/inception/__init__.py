"""
Custom integration to integrate InnerRange Inception with Home Assistant.

For more details about this integration, please refer to
https://github.com/sebr/inception-home-assistant
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.const import CONF_HOST, CONF_TOKEN, Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.loader import async_get_loaded_integration

from custom_components.inception.const import DOMAIN

from .api import InceptionApiClient
from .coordinator import InceptionUpdateCoordinator
from .data import InceptionData

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import InceptionConfigEntry

PLATFORMS: list[Platform] = [
    # Platform.SENSOR,
    Platform.BINARY_SENSOR,
    # Platform.SWITCH,
]


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(
    hass: HomeAssistant,
    entry: InceptionConfigEntry,
) -> bool:
    """Set up this integration using UI."""
    coordinator = InceptionUpdateCoordinator(
        hass=hass,
    )
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    # entry.runtime_data = InceptionData(
    #     client=InceptionApiClient(
    #         token=entry.data[CONF_TOKEN],
    #         host=entry.data[CONF_HOST],
    #         session=async_get_clientsession(hass),
    #     ),
    #     integration=async_get_loaded_integration(hass, entry.domain),
    #     coordinator=coordinator,
    # )

    # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: InceptionConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(
    hass: HomeAssistant,
    entry: InceptionConfigEntry,
) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)