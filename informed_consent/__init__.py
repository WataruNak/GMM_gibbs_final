from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'informed_consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_accepted = models.BooleanField()


# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ["is_accepted"]

class Disagree(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.is_accepted == 0

class Agree(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.is_accepted == 1


page_sequence = [Consent, Disagree, Agree]
