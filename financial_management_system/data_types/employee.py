import dataclasses
import uuid


@dataclasses.dataclass
class Employee:
    """ """

    first_name: str
    last_name: str
    city: str
    state: str
    zip_code: str
    ssn: str
    withholdings: float
    salary: float

    employee_id: str = dataclasses.field(default_factory=lambda: str(uuid.uuid4()))
