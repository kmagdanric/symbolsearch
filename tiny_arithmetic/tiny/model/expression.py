from pydantic import BaseModel


class Expression(BaseModel):
    value: int

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Expression({self.value})"
