from typing import Literal

type Token = Literal["+", "*", "(", ")"] | int


def tokenize(s: str) -> list[Token]:
    tokens = list()
    while s:
        c, s = s[0], s[1:]
        match c:
            case " ":
                continue
            case "+" | "*" | "(" | ")":
                tokens.append(c)
            case _:
                number = c
                while s and s[0] in "0123456789":
                    number += s[0]
                    s = s[1:]
                tokens.append(int(number))
    return tokens


type Expr = int | tuple[Expr, Literal["+", "*"], Expr]


def evaluate(expr: Expr):
    match expr:
        case int(v):
            return v
        case lhs, "*", rhs:
            return evaluate(lhs) * evaluate(rhs)
        case lhs, "+", rhs:
            return evaluate(lhs) + evaluate(rhs)
        case _:
            assert False


def part1():
    def term(tokens: list[Token]) -> tuple[Expr, list[Token]]:
        match tokens:
            case ["(", *more_tokens]:
                inner, tokens = expr(more_tokens)
                token, *tokens = tokens
                assert token == ")"
                return inner, tokens
            case [int(v), *more_tokens]:
                return v, more_tokens
            case _:
                raise Exception(f"Expected term")

    def expr(tokens: list[Token]) -> tuple[Expr, list[Token]]:
        v, tokens = term(tokens)
        while tokens and tokens[0] in ("+", "*"):
            match tokens:
                case "*", *tokens:
                    rhs, tokens = term(tokens)
                    v = v, "*", rhs
                case "+", *tokens:
                    rhs, tokens = term(tokens)
                    v = v, "+", rhs
                case _:
                    assert False
        return v, tokens

    S = 0
    for line in open("input.txt"):
        parsed = expr(tokenize(line.strip()))
        S += evaluate(parsed[0])
    return S


def part2():
    def factor(tokens: list[Token]) -> tuple[Expr, list[Token]]:
        v, tokens = term(tokens)
        while tokens and tokens[0] == "+":
            tokens = tokens[1:]
            rhs, tokens = term(tokens)
            v = v, "+", rhs
        return v, tokens

    def term(tokens: list[Token]) -> tuple[Expr, list[Token]]:
        match tokens:
            case ["(", *more_tokens]:
                inner, tokens = expr(more_tokens)
                token, *tokens = tokens
                assert token == ")"
                return inner, tokens
            case [int(v), *more_tokens]:
                return v, more_tokens
            case _:
                raise Exception(f"Expected term")

    def expr(tokens: list[Token]) -> tuple[Expr, list[Token]]:
        v, tokens = factor(tokens)
        while tokens and tokens[0] == "*":
            tokens = tokens[1:]
            rhs, tokens = factor(tokens)
            v = v, "*", rhs
        return v, tokens

    S = 0
    for line in open("input.txt"):
        parsed = expr(tokenize(line.strip()))
        S += evaluate(parsed[0])
    return S


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
