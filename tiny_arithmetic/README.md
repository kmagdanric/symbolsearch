## Grammar Literal

```
Expr = Expr + Term
       | Expr - Term
       | Term

Term = Factor
       | Term * Factor
       | Term / Factor

Factor = ( Expr )
         | - Factor
         | Number
```

## Rules Reflected

- Multiply and Divide have precedence over Plus and Minus
- Parenthesis have precedence over everything
- negation works on factor (the whole expression, or number)
- All binary operators here are left-associative


