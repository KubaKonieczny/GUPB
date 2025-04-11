from gupb.controller import keyboard, random
from gupb.controller.camperbot.camperbot import CamperBotController
from gupb.controller.garek.garek import GarekController

keyboard_controller = keyboard.KeyboardController()

CONFIGURATION = {
    "arenas": ["ordinary_chaos"],
    "controllers": [
        CamperBotController("Niki"),
        GarekController("Jarek"),
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Darius"),
    ],
<<<<<<< HEAD
    "start_balancing": False,
    "visualise": False,
    "show_sight": keyboard_controller,
    "runs_no": 100,
    "profiling_metrics": [],
}
=======
    'start_balancing': False,
    'visualise': True,
    'show_sight': keyboard_controller,
    'runs_no': 1,
    'profiling_metrics': [],
}
>>>>>>> rouge/uzw-2025-lato-ReinforcedRogue
