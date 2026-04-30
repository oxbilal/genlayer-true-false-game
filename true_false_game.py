# v0.2.16
# { "Depends": "py-genlayer:latest" }

from genlayer import *

class TrueFalseGame(gl.Contract):
    statement: str
    correct_answer: str
    last_answer: str
    result: str
    score: u256

    def __init__(self):
        self.statement = "GenLayer uses AI and blockchain consensus"
        self.correct_answer = "true"
        self.last_answer = ""
        self.result = "No answer yet"
        self.score = 0

    @gl.public.write
    def play(self, answer: str) -> None:
        self.last_answer = answer
        if answer.lower().strip() == self.correct_answer:
            self.result = "Correct!"
            self.score = 1
        else:
            self.result = "Wrong, try again"
            self.score = 0

    @gl.public.view
    def get_game(self) -> str:
        return f"Statement: {self.statement} | Last answer: {self.last_answer} | Result: {self.result} | Score: {self.score}"
