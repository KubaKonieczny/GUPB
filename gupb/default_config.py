<<<<<<< HEAD
from gupb.controller import keyboard, random
from gupb.controller.camperbot.camperbot import CamperBotController
from gupb.controller.garek.garek import GarekController
=======
from gupb.controller import keyboard
from gupb.controller import random
from gupb.controller import kirby_learning, kirby

>>>>>>> kirby/kirby_ddqn_2

keyboard_controller = keyboard.KeyboardController()

CONFIGURATION = {
<<<<<<< HEAD
    "arenas": ["ordinary_chaos"],
    "controllers": [
        CamperBotController("Niki"),
        GarekController("Jarek"),
=======
    'arenas': [
        'archipelago',
        'dungeon',
        'fisher_island',
        'island',
        'isolated_shrine',
        'lone_sanctum',
        'mini',
        'ordinary_chaos',
        'wasteland',
    ],
    'controllers': [
        # keyboard_controller,
>>>>>>> kirby/kirby_ddqn_2
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Darius"),
        # kirby_learning.KirbyLearningController("KirbyLearning"),
        kirby.KirbyController("Kirby")

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
    'visualise': False,
    'show_sight': None,
    'runs_no': 10,  # kirby.ROUNDS_NO,
    'profiling_metrics': [],
}
>>>>>>> rouge/uzw-2025-lato-ReinforcedRogue
