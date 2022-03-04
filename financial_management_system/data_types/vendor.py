import dataclasses
import uuid


@dataclasses.dataclass
class Vendor:
    """Represents the state of one of our vendors"""

    name: str
    vendor_id: int = 0

    vendor_id: str = dataclasses.field(default_factory=lambda: str(uuid.uuid4()))
