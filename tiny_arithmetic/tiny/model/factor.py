from pydantic import BaseModel


class Factor(BaseModel):
    value: int

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Factor({self.value})"
