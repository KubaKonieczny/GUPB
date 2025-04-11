from gupb.controller import garek, keyboard, kirby, random, reinforced_rogue, rustler
from gupb.controller.bupg.bupg import BUPGController
from gupb.controller.camperbot.camperbot import CamperBotController
from gupb.controller.pirat import pirat

keyboard_controller = keyboard.KeyboardController()

CONFIGURATION = {
    "arenas": ["ordinary_chaos"],
    "controllers": [
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
        reinforced_rogue.ReinforcedRogueController(""),
    ],
    "start_balancing": False,
    "visualise": False,
    "show_sight": keyboard_controller,
    "runs_no": 100,
    "profiling_metrics": [],
}
