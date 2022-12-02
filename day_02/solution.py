from enum import Enum, auto
from dataclasses import dataclass
from typing import Iterator


def get_input_str() -> str:
    with open("input.txt", "r") as f:
        input_str = f.read()
    return input_str


class Shape(Enum):
    ROCK = auto()
    PAPPER = auto()
    SCISSORS = auto()


OPPONENT_SHAPES = {"A": Shape.ROCK, "B": Shape.PAPPER, "C": Shape.SCISSORS}
PLAYER_SHAPES = {"X": Shape.ROCK, "Y": Shape.PAPPER, "Z": Shape.SCISSORS}

SHAPE_SCORES = {Shape.ROCK: 1, Shape.PAPPER: 2, Shape.SCISSORS: 3}


# Rock wins vs Scissors, Paper wins vs Rock, Scissor wins vs Papper
RULES_WINS_VERSUS = {
    Shape.ROCK: Shape.SCISSORS,
    Shape.PAPPER: Shape.ROCK,
    Shape.SCISSORS: Shape.PAPPER,
}

# Scissors loose vs Rock, Rock loose vs Papper, Papper loose vs Scissor
RULES_LOOSE_VERSUS = {b: a for a, b in RULES_WINS_VERSUS.items()}


class RoundOutcome(Enum):
    WIN = auto()
    LOSS = auto()
    DRAW = auto()


@dataclass
class Round:
    player_shape: Shape
    opponent_shape: Shape


OUTCOME_SCORES = {RoundOutcome.WIN: 6, RoundOutcome.LOSS: 0, RoundOutcome.DRAW: 3}


def get_round_outcome(round: Round) -> RoundOutcome:
    if round.opponent_shape == round.player_shape:
        return RoundOutcome.DRAW
    if round.opponent_shape == RULES_WINS_VERSUS[round.player_shape]:
        return RoundOutcome.WIN
    return RoundOutcome.LOSS


def get_round_score(round: Round) -> int:
    outcoume = get_round_outcome(round)
    return SHAPE_SCORES[round.player_shape] + OUTCOME_SCORES[outcoume]


def get_rounds() -> Iterator[Round]:
    input_str = get_input_str()
    rounds = input_str.split("\n")
    for round in rounds:
        opponent_str, player_str = round.split(" ")
        yield Round(
            player_shape=PLAYER_SHAPES[player_str],
            opponent_shape=OPPONENT_SHAPES[opponent_str],
        )


def part_one():
    return sum(get_round_score(round) for round in get_rounds())


EXPECTED_OUTCOMES = {
    "X": RoundOutcome.LOSS,
    "Y": RoundOutcome.DRAW,
    "Z": RoundOutcome.WIN,
}


def get_play_for_outcome(opponnent_shape: Shape, expected_outcome: RoundOutcome):
    if expected_outcome == RoundOutcome.DRAW:
        return opponnent_shape
    if expected_outcome == RoundOutcome.WIN:
        return RULES_LOOSE_VERSUS[opponnent_shape]
    if expected_outcome == RoundOutcome.LOSS:
        return RULES_WINS_VERSUS[opponnent_shape]


def get_modified_rounds() -> Iterator[Round]:
    input_str = get_input_str()
    rounds = input_str.split("\n")
    for round in rounds:
        opponent_str, player_str = round.split(" ")
        opponnent_shape = OPPONENT_SHAPES[opponent_str]
        expected_outcome = EXPECTED_OUTCOMES[player_str]
        player_shape = get_play_for_outcome(opponnent_shape, expected_outcome)
        yield Round(player_shape=player_shape, opponent_shape=opponnent_shape)


def part_two():
    return sum(get_round_score(round) for round in get_modified_rounds())


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
