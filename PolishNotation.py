class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        # thought process
        # lets have stack and if the token is not an operator then append in the stack
        # once the token is an operator then pop the last two elements from the operator
        # stack.pop = right token , again stack.pop = left token
        # perfrom left token operator right token
        # have a function based on the operator to pefrom 
        # add the result back into pop and continue the iteratign through loop
        # things to consider that the division between integres truncate to zero and not float values
        # and if the right token is 0 but said division by zero so i am assuming the inputs won't be in this format
        # the tokens array is an valid arithmetic experession
        # and also the calculatons represent a 32 bit integer
        # procceding with the logic


        operations = {
        "+": lambda left, right: left + right,
        "-": lambda left, right: left - right,
        "/": lambda left, right: int(left / right),
        "*": lambda left, right: left * right,
        }

        stack = []

        for token in tokens:
            if token in operations:
                right_token = stack.pop()
                left_token = stack.pop()
                stack.append(operations[token](left_token, right_token))
                print("operation performaed: ", stack)
            else:
                stack.append(int(token))
                print(stack)

        return stack.pop()