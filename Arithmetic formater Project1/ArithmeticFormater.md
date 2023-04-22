# Arithmetic Formatter

### Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

## Situations that will return an error: (Constraints)

1. The limit is five, anything more will return: **Error: Too many problems.**
2. function will accept are addition and subtraction. **Error: Operator must be '+' or '-'.**
3. Each number (operand) should only contain digits. Otherwise, the function will return:
   **Error: Numbers must only contain digits.**
4. Each operand (aka number on each side of the operator) has a max of four digits in width.
   **Error: Numbers cannot be more than four digits.**

## RULES TO FOLLOW :

1. There should be a single space between the operator and the longest of the two operands,
   the operator will be on the same line as the second operand, both operands will be in the same order
   as provided (the first will be the top one and the second will be the bottom.)
2. Numbers should be right-aligned.
3. There should be four spaces between each problem.
4. There should be dashes at the bottom of each problem. The dashes should run along the entire length
   of each problem individually.
