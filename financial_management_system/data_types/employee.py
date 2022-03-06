import dataclasses
import uuid
import typing


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

    @property
    def table_attributes(self) -> typing.List[typing.Any]:
        """ """
        return [
            self.first_name,
            self.last_name,
            self.city,
            self.state,
            self.zip_code,
            self.ssn,
            self.withholdings,
            self.salary,
        ]
