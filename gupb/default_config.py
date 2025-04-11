<<<<<<< HEAD
<<<<<<< HEAD
from gupb.controller import keyboard, random
from gupb.controller.camperbot.camperbot import CamperBotController
from gupb.controller.garek.garek import GarekController
=======
from gupb.controller import keyboard
from gupb.controller import random
from gupb.controller import kirby_learning, kirby

>>>>>>> kirby/kirby_ddqn_2
=======
from gupb.controller import keyboard, garek, kirby, rustler, reinforced_rogue
from gupb.controller import random
from gupb.controller.camperbot.camperbot import CamperBotController
from gupb.controller.pirat import pirat
from gupb.controller.bupg.bupg import BUPGController
>>>>>>> garekbot/test-all-bots

keyboard_controller = keyboard.KeyboardController()

CONFIGURATION = {
<<<<<<< HEAD
    "arenas": ["ordinary_chaos"],
    "controllers": [
        CamperBotController("Niki"),
        GarekController("Jarek"),
=======
    'arenas': [
        'ordinary_chaos'
    ],
    'controllers': [
<<<<<<< HEAD
        # keyboard_controller,
>>>>>>> kirby/kirby_ddqn_2
=======
>>>>>>> garekbot/test-all-bots
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Darius"),
        garek.GarekController(""),
        CamperBotController(""),
        kirby.KirbyController("Kirby"),
        pirat.PiratController("Pirat"),
        BUPGController(""),
        rustler.Rustler(""),
        reinforced_rogue.ReinforcedRogueController("")

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
    'show_sight': keyboard_controller,
    'runs_no': 50,
    'profiling_metrics': [],
}
>>>>>>> rouge/uzw-2025-lato-ReinforcedRogue
