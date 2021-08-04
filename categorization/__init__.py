from otree.api import *
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'categorization'
    players_per_group = 2
    num_rounds = 40


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_category = models.StringField(
        label = "この画像に当てはまると思われるカテゴリーを選択し、「次へ」ボタンを押してください。",
        choices = ['1', '2', '3', '4', '5', '6'],
        widget = widgets.RadioSelectHorizontal
    )
    stimuli_id = models.IntegerField()



def custom_export(players):
    yield [
        "session",
        "participant_code",
        "round_number",
        "id_in_group",
        "stimuli_id",
        "selected_category"]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.round_number,
            p.id_in_group,
            p.stimuli_id,
            p.selected_category,
            ]

# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitForOtherPlayer(WaitPage):
    titel_text = "相手プレイヤーを探しています。"
    body_text = "もう一人のプレイヤーが見つかるまで、お待ち下さい。"
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Categorize(Page):
    form_model = 'player'
    form_fields = ["selected_category"]

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            player.participant.img2category = {}
            player.participant.stimuli_id_list = []
            for n in range(Constants.num_rounds):
                player.participant.stimuli_id_list.append(n+1)
            random.shuffle(player.participant.stimuli_id_list)
        showed_img = "stimuli/cv2img{}.jpg".format(player.participant.stimuli_id_list[player.round_number - 1])
        player.stimuli_id = player.participant.stimuli_id_list[player.round_number - 1]
        return {
            "showed_img" : showed_img,
            "dict" : player.participant.img2category,
        }
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.img2category["stimuli/cv2img{}.jpg".format(player.participant.stimuli_id_list[player.round_number - 1])] = player.selected_category
   



class ResultsWaitPage(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "dict" : player.participant.img2category
        }


page_sequence = [Introduction, WaitForOtherPlayer, Categorize, ResultsWaitPage, Results]
