from gupb.controller import keyboard, garek, kirby
from gupb.controller import random
from gupb.controller.camperbot.camperbot import CamperBotController
from gupb.controller.pirat import pirat
from gupb.controller.bupg.bupg import BUPGController

keyboard_controller = keyboard.KeyboardController()

CONFIGURATION = {
    'arenas': [
        'ordinary_chaos'
    ],
    'controllers': [
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Darius"),
        garek.GarekController(""),
        CamperBotController(""),
        kirby.KirbyController("Kirby"),
        pirat.PiratController("Pirat"),
        BUPGController("")

    ],
    'start_balancing': False,
    'visualise': False,
    'show_sight': keyboard_controller,
    'runs_no': 50,
    'profiling_metrics': [],
}
