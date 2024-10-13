class Postfija:
    def __init__(self, expresion_infija: str):
        self.expresion_infija = expresion_infija
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
        }
        self.associativity = {
            '+': 'L',
            '-': 'L',
            '*': 'L',
            '/': 'L',
            '^': 'R',
        }

    def infija(self) -> str:
        # Retorna la expresión infija original separada por espacios
        return ' '.join(self.tokenize(self.expresion_infija))

    def postfija(self) -> str:
        output = []
        stack = []
        tokens = self.tokenize(self.expresion_infija)

        for token in tokens:
            if token.isnumeric():
                output.append(token)
            elif token in self.precedence:
                while (stack and stack[-1] != '(' and
                    (self.precedence[stack[-1]] > self.precedence[token] or
                        (self.precedence[stack[-1]] == self.precedence[token] and self.associativity[token] == 'L'))):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Eliminar el '(' de la pila

        while stack:
            output.append(stack.pop())

        return ' '.join(output)

    def eval_expr_aritm(self) -> float:
        stack = []
        postfix_expr = self.postfija().split()

        for token in postfix_expr:
            if token.isnumeric():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = self.perform_operation(a, b, token)
                stack.append(result)

        return stack[0]

    def perform_operation(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        elif operator == '^':
            return a ** b
        else:
            raise ValueError(f"Operador desconocido: {operator}")

    def tokenize(self, expression):
        tokens = []
        current_number = ''

        for char in expression:
            if char.isdigit():
                current_number += char  # Agregar dígitos al número actual
            else:
                if current_number:
                    tokens.append(current_number)  # Añadir número completo a los tokens
                    current_number = ''
                if char in self.precedence or char in '()':
                    tokens.append(char)

        if current_number:
            tokens.append(current_number)  
        return tokens

# Ejemplo de uso
if __name__ == '__main__':
    expr = "12 + 5 * ( 2 - 8 )"
    converter = Postfija(expr)
    print(f"Expresión Infija: {converter.infija()}")
    print(f"Expresión Postfija: {converter.postfija()}")
    result = converter.eval_expr_aritm()
    print(f"Resultado: {result}")
    expr = "122 + 5 * ( 2 - 8 )"
    converter = Postfija(expr)
    print(f"Expresión Infija: {converter.infija()}")
    print(f"Expresión Postfija: {converter.postfija()}")
    result = converter.eval_expr_aritm()
    print(f"Resultado: {result}")