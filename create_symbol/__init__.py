from otree.api import *
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'create_symbol'
    players_per_group = 2
    num_rounds = 40


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    send_choice = models.StringField(
        initial="99",
        label="この画像を表す記号を選んで、「次へ」ボタンを押して下さい。選んだ記号が相手プレイヤーに提案されます。",
        choices=[
            ["1", "　　　　"],
            ["2", "　　　　"],
            ["3", "　　　　"],
            ["4", "　　　　"],
            ["5", "　　　　"],
            ["6", "　　　　"],
            ],
        widget = widgets.RadioSelectHorizontal,
    )
    rename_choice = models.StringField(
        initial="99",
        label="あなたが正解だと思う記号を選んで、「次へ」ボタンを押して下さい。",
        choices=[
            ["1", "　　　　"],
            ["2", "　　　　"],
            ["3", "　　　　"],
            ["4", "　　　　"],
            ["5", "　　　　"],
            ["6", "　　　　"],
            ],
        widget = widgets.RadioSelectHorizontal,
    )
    accept = models.IntegerField(
        initial=2,
        label="相手プレイヤーがつけた名前を受け入れますか？",
        choices=[
            [0, "受け入れず、違う名前をつける"],
            [1, "受け入れてその名前をつける"],
        ],
        widget = widgets.RadioSelect,
    )
    test_id = models.IntegerField()

    def role(self):
        if self.round_number % 2 == 1:
            if self.id_in_group % 2 == 1:
                return 'speaker'
            if self.id_in_group % 2 == 0:
                return 'listener'
        else:
            if self.id_in_group % 2 == 1:
                return 'listener'
            if self.id_in_group % 2 == 0:
                return 'speaker'

    
def rename_choice_error_message(player, value):
    if value == player.get_others_in_group()[0].send_choice:
        return '「話し手」が選んだものとは違う記号を選んでください'


def custom_export(players):
    yield [
        "session",
        "participant_code",
        "round_number",
        "id_in_group",
        "img_id",
        "send_choice",
        "accept",
        "rename_choice",
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.round_number,
            p.id_in_group,
            session.test_id_list,
            p.send_choice,
            p.accept,
            p.rename_choice
            ]



# PAGES
class Instruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class ShowRole(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            player.participant.img2name = {}
        return {
            "role" : player.role(),
            }


class Speaker(Page):
    form_model = 'player'
    form_fields = ["send_choice"]

    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'speaker'

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            player.session.test_id_list = []
            for n in range(Constants.num_rounds):
                player.session.test_id_list.append(n+1)
            random.shuffle(player.session.test_id_list)
        showed_img = "stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])
        return {
            "showed_img" : showed_img,
            "dict1" : player.participant.img2category,
            "dict2" : player.participant.img2name,
        }


class Listener(Page):
    form_model = 'player'
    form_fields = ["accept"]

    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'listener'

    @staticmethod
    def vars_for_template(player: Player):
        showed_img = "stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])
        other_players = player.get_others_in_group()
        return {
            "showed_img" : showed_img,
            "others_choice" : other_players[0].send_choice,
            "dict1" : player.participant.img2category,
            "dict2" : player.participant.img2name,
        }


class Accept(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.accept == 1
    
    @staticmethod
    def vars_for_template(player: Player):
        showed_img = "stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])
        other_players = player.get_others_in_group()
        return {
            "showed_img" : showed_img,
            "others_choice" : other_players[0].send_choice,
            "dict1" : player.participant.img2category,
            "dict2" : player.participant.img2name,
        }
 


class Reject(Page):
    form_model = 'player'
    form_fields = ["rename_choice"]

    @staticmethod
    def is_displayed(player: Player):
        return player.accept == 0
    
    @staticmethod
    def vars_for_template(player: Player):
        showed_img = "stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])
        other_players = player.get_others_in_group()
        return {
            "showed_img" : showed_img,
            "others_choice" : other_players[0].send_choice,
            "dict1" : player.participant.img2category,
            "dict2" : player.participant.img2name,
        }



class WaitForSpeaker(WaitPage):
    titel_text = "「話し手」の入力を待っています"
    body_text = "あなたは「聞き手」です。「話し手」が名前を決めるまでお待ち下さい。"
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'listener'


class WaitForListener(WaitPage):
    titel_text = "「聞き手」の入力を待っています"
    body_text = "「聞き手」があなたのつけた名前を受け入れるかどうかを決めています。入力があるまでお待ち下さい。"
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'speaker'


class EndOfRound(Page):
    @staticmethod
    def vars_for_template(player: Player):
        showed_img = "stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])
        player.test_id = player.session.test_id_list[player.round_number - 1]
        other_players = player.get_others_in_group()
        other_players = player.get_others_in_group()
        if player.role() == 'speaker':
            player.participant.img2name["stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])] = player.send_choice
        elif player.role() == 'listener':
            if player.accept == 1:
                player.participant.img2name["stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])] = other_players[0].send_choice
            else:
                player.participant.img2name["stimuli/cv2img{}.jpg".format(player.session.test_id_list[player.round_number - 1])] = player.rename_choice
        return {
            "role" : player.role(),
            "my_choice" : player.send_choice,
            "showed_img" : showed_img,
            "others_choice" : other_players[0].send_choice,
            "accept" : player.accept,
            "others_accept" : other_players[0].accept,
            'rename' : player.rename_choice,
            "others_rename" : other_players[0].rename_choice,
            "dict1" : player.participant.img2category,
            "dict2" : player.participant.img2name,
        }



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
            "dict1" : player.participant.img2category,
            "dict2" : player.participant.img2name,
        }


page_sequence = [
    Instruction,
    ShowRole,
    Speaker,
    WaitForSpeaker,
    Listener,
    Accept,
    Reject,
    WaitForListener,
    EndOfRound,
    ResultsWaitPage,
    Results
    ]
