from gupb.controller import keyboard, random
from gupb.controller.camperbot.camperbot import CamperBotController
from gupb.controller import garek

keyboard_controller = keyboard.KeyboardController()

CONFIGURATION = {
    "arenas": ["ordinary_chaos"],
    "controllers": [
        CamperBotController("Niki"),
        garek.GarekController("Jarek"),
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Darius"),
    ],
    "start_balancing": False,
    "visualise": False,
    "show_sight": keyboard_controller,
    "runs_no": 100,
    "profiling_metrics": [],
}
