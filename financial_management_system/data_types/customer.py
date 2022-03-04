import dataclasses
import uuid


@dataclasses.dataclass
class Customer:
    """ """

    name: str
    customer_id: str = dataclasses.field(default_factory=lambda: str(uuid.uuid4()))
