__author__ = "Alon B.R."

import json

from os.path import join as join_path

settings_path: tuple = ("data", "settings.json")


def read_settings() -> dict:
    data: dict = dict()

    with open(join_path(*settings_path), "r") as f:
        content = f.read()
        data = json.loads(content)

    return data


settings = read_settings()

TITLE: str = settings["title"]
WIDTH: int = settings["width"]
HEIGHT: int = settings["height"]
BG_COLOR: tuple = tuple(settings["bg color"])
SHOW_PARTICLE_CIRCLE: bool = settings["show particle circle"]
PARTICLE_CIRCLE_RADIUS: float | int = settings["particle circle radius"]
SHOW_RAYS: bool = settings["show rays"]
SHOW_RAY_DIRECTION: bool = settings["show ray direction"]
RAY_DIRECTION_THICKNESS: int = settings["ray direction thickness"]
RAY_DIRECTION_LENGTH_MULTIPLIER: float = settings["ray direction length multiplier"]
