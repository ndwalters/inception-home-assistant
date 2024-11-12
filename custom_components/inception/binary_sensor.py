"""Binary sensor platform for inception."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)

from .const import CONF_INPUTS
from .entity import InceptionEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import InceptionUpdateCoordinator
    from .data import InceptionConfigEntry

ENTITY_DESCRIPTIONS = (
    BinarySensorEntityDescription(
        key="inception",
        name="Inception Binary Sensor",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
)


def get_device_class(name: str) -> BinarySensorDeviceClass:
    """Define device class from device name."""
    device_classes = {
        "motion": BinarySensorDeviceClass.MOTION,
        "pir": BinarySensorDeviceClass.MOTION,
        "pe beam": BinarySensorDeviceClass.MOTION,
        "louvre": BinarySensorDeviceClass.WINDOW,
        "shock": BinarySensorDeviceClass.VIBRATION,
        "button": BinarySensorDeviceClass.CONNECTIVITY,
        "rex": BinarySensorDeviceClass.DOOR,
        "opening": BinarySensorDeviceClass.OPENING,
        "power": BinarySensorDeviceClass.POWER,
        "smoke": BinarySensorDeviceClass.SMOKE,
        "vibration": BinarySensorDeviceClass.VIBRATION,
        "cold": BinarySensorDeviceClass.COLD,
        "light": BinarySensorDeviceClass.LIGHT,
        "moisture": BinarySensorDeviceClass.MOISTURE,
        "break": BinarySensorDeviceClass.VIBRATION,
        "glass": BinarySensorDeviceClass.WINDOW,
        "side door": BinarySensorDeviceClass.DOOR,
        "hallway door": BinarySensorDeviceClass.DOOR,
        "garage": BinarySensorDeviceClass.GARAGE_DOOR,
        "gate": BinarySensorDeviceClass.DOOR,
        "window": BinarySensorDeviceClass.WINDOW,
        "door": BinarySensorDeviceClass.DOOR,
        "heat": BinarySensorDeviceClass.HEAT,
    }

    # Find the first matching device class or default to 'opening'
    return next(
        (device_classes[device] for device in device_classes if device in name.lower()),
        BinarySensorDeviceClass.OPENING,
    )


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: InceptionConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary_sensor platform."""
    inception_inputs = entry.data.get(CONF_INPUTS, [])

    entities = [
        InceptionBinarySensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=BinarySensorEntityDescription(
                key=inception_input.get("ID"),
                name=inception_input.get("Name", "Unknown Input"),
                device_class=get_device_class(inception_input.get("Name", "")),
            ),
        )
        for inception_input in inception_inputs
    ]

    async_add_entities(entities)


class InceptionBinarySensor(InceptionEntity, BinarySensorEntity):
    """inception binary_sensor class."""

    def __init__(
        self,
        coordinator: InceptionUpdateCoordinator,
        entity_description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary_sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def is_on(self) -> bool:
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"
