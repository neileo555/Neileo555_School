import datetime
import uuid
import dataclasses


@dataclasses.dataclass
class PurchaseOrder:
    """Represents the state of a single transaction with a vendor.

    We buy goods and services with money.
    """

    date: datetime.date
    total: float
    vendor_id: int
    description: str = ""

    purchase_order_id: str = dataclasses.field(default_factory=lambda: str(uuid.uuid4()))
