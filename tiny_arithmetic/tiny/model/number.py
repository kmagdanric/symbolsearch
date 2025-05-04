from pydantic import BaseModel


class Number(BaseModel):
    value: int

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Number({self.value})"
