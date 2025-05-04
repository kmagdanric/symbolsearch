from pydantic import BaseModel


class Term(BaseModel):
    value: int

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Term({self.value})"
