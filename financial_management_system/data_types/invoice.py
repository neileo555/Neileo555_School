import dataclasses
import datetime
import uuid


@dataclasses.dataclass
class Invoice:
    """Represents a single receipt of a customer transaction

    We sell goods and services for money
    """

    date: datetime.date
    total: float
    customer_id: int
    description: str = ""

    invoice_id: str = dataclasses.field(default_factory=lambda: str(uuid.uuid4()))
