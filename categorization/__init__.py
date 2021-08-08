from otree.api import *
import random

doc = """
https://qiita.com/naoki-funawatari/items/c78630b85f5f7fe21d19 drag_and_drop
https://www.otreehub.com/projects/otree-snippets/ otree sortable_example
https://qiita.com/AVELWP/items/536c797a63c081cf7bc0 sortable document ja
https://github.com/SortableJS/Sortable sortable git
https://qiita.com/t-iguchi/items/20dc31d5e004d7145634 js in django
"""


class Constants(BaseConstants):
    name_in_url = 'categorization'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    name_order = models.StringField(default="1,2,3,4,5,6")
    img0_cat = models.IntegerField(default=0)
    img1_cat = models.IntegerField(default=0)
    img2_cat = models.IntegerField(default=0)
    img3_cat = models.IntegerField(default=0)
    img4_cat = models.IntegerField(default=0)
    img5_cat = models.IntegerField(default=0)
    img6_cat = models.IntegerField(default=0)
    img7_cat = models.IntegerField(default=0)
    img8_cat = models.IntegerField(default=0)
    img9_cat = models.IntegerField(default=0)
    img10_cat = models.IntegerField(default=0)
    img11_cat = models.IntegerField(default=0)
    img12_cat = models.IntegerField(default=0)
    img13_cat = models.IntegerField(default=0)
    img14_cat = models.IntegerField(default=0)
    img15_cat = models.IntegerField(default=0)
    img16_cat = models.IntegerField(default=0)
    img17_cat = models.IntegerField(default=0)
    img18_cat = models.IntegerField(default=0)
    img19_cat = models.IntegerField(default=0)
    img20_cat = models.IntegerField(default=0)
    img21_cat = models.IntegerField(default=0)
    img22_cat = models.IntegerField(default=0)
    img23_cat = models.IntegerField(default=0)
    img24_cat = models.IntegerField(default=0)
    img25_cat = models.IntegerField(default=0)
    img26_cat = models.IntegerField(default=0)
    img27_cat = models.IntegerField(default=0)
    img28_cat = models.IntegerField(default=0)
    img29_cat = models.IntegerField(default=0)
    img30_cat = models.IntegerField(default=0)
    img31_cat = models.IntegerField(default=0)
    img32_cat = models.IntegerField(default=0)
    img33_cat = models.IntegerField(default=0)
    img34_cat = models.IntegerField(default=0)
    img35_cat = models.IntegerField(default=0)
    img36_cat = models.IntegerField(default=0)
    img37_cat = models.IntegerField(default=0)
    img38_cat = models.IntegerField(default=0)
    img39_cat = models.IntegerField(default=0)

    img_1st = models.IntegerField()
    img_2nd = models.IntegerField()
    img_3rd = models.IntegerField()
    img_4th = models.IntegerField()
    img_5th = models.IntegerField()
    img_6th = models.IntegerField()
    img_7th = models.IntegerField()
    img_8th = models.IntegerField()
    img_9th = models.IntegerField()
    img_10th = models.IntegerField()
    img_11th = models.IntegerField()
    img_12th = models.IntegerField()
    img_13th = models.IntegerField()
    img_14th = models.IntegerField()
    img_15th = models.IntegerField()
    img_16th = models.IntegerField()
    img_17th = models.IntegerField()
    img_18th = models.IntegerField()
    img_19th = models.IntegerField()
    img_20th = models.IntegerField()
    img_21st = models.IntegerField()
    img_22nd = models.IntegerField()
    img_23rd = models.IntegerField()
    img_24th = models.IntegerField()
    img_25th = models.IntegerField()
    img_26th = models.IntegerField()
    img_27th = models.IntegerField()
    img_28th = models.IntegerField()
    img_29th = models.IntegerField()
    img_30th = models.IntegerField()
    img_31st = models.IntegerField()
    img_32nd = models.IntegerField()
    img_33rd = models.IntegerField()
    img_34th = models.IntegerField()
    img_35th = models.IntegerField()
    img_36th = models.IntegerField()
    img_37th = models.IntegerField()
    img_38th = models.IntegerField()
    img_39th = models.IntegerField()
    img_40th = models.IntegerField()


def custom_export(players):
    yield [
        "session",
        "participant_code",
        "round_number",
        "id_in_group",
        "stimuli_id",
        "selected_category",
        ]
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

class Categorize(Page):
    form_model = 'player'
    form_fields = [
        "name_order",
        "img0_cat", "img1_cat", "img2_cat", "img3_cat", "img4_cat",
        "img5_cat", "img6_cat", "img7_cat", "img8_cat", "img9_cat",
        "img10_cat", "img11_cat", "img12_cat", "img13_cat", "img14_cat",
        "img15_cat", "img16_cat", "img17_cat", "img18_cat", "img19_cat",
        "img20_cat", "img21_cat", "img22_cat", "img23_cat", "img24_cat",
        "img25_cat", "img26_cat", "img27_cat", "img28_cat", "img29_cat",
        "img30_cat", "img31_cat", "img32_cat", "img33_cat", "img34_cat",
        "img35_cat", "img36_cat", "img37_cat", "img38_cat", "img39_cat",
        "img_1st", "img_2nd", "img_3rd", "img_4th", "img_5th",
        "img_6th", "img_7th", "img_8th", "img_9th", "img_10th",
        "img_11th", "img_12th", "img_13th", "img_14th", "img_15th",
        "img_16th", "img_17th", "img_18th", "img_19th", "img_20th",
        "img_21st", "img_22nd", "img_23rd", "img_24th", "img_25th",
        "img_26th", "img_27th", "img_28th", "img_29th", "img_30th",
        "img_31st", "img_32nd", "img_33rd", "img_34th", "img_35th",
        "img_36th", "img_37th", "img_38th", "img_39th", "img_40th",
    ]

    @staticmethod
    def vars_for_template(player: Player):
        player.participant.img2category = {}
        player.participant.stimuli_id_list = []
        player.participant.imgPathSeries = []
        for n in range(40):
            player.participant.stimuli_id_list.append(n+1)
        random.shuffle(player.participant.stimuli_id_list)
        for i in range(40):
            player.participant.img2category["stimuli/cv2img{}.jpg".format(player.participant.stimuli_id_list[i])] = 0
        for j in range(40):
            player.participant.imgPathSeries.append(list(player.participant.img2category.keys())[j])
        player.img_1st = player.participant.stimuli_id_list[0]
        player.img_2nd = player.participant.stimuli_id_list[1]
        player.img_3rd = player.participant.stimuli_id_list[2]
        player.img_4th = player.participant.stimuli_id_list[3]
        player.img_5th = player.participant.stimuli_id_list[4]
        player.img_6th = player.participant.stimuli_id_list[5]
        player.img_7th = player.participant.stimuli_id_list[6]
        player.img_8th = player.participant.stimuli_id_list[7]
        player.img_9th = player.participant.stimuli_id_list[8]
        player.img_10th = player.participant.stimuli_id_list[9]
        player.img_11th = player.participant.stimuli_id_list[10]
        player.img_12th = player.participant.stimuli_id_list[11]
        player.img_13th = player.participant.stimuli_id_list[12]
        player.img_14th = player.participant.stimuli_id_list[13]
        player.img_15th = player.participant.stimuli_id_list[14]
        player.img_16th = player.participant.stimuli_id_list[15]
        player.img_17th = player.participant.stimuli_id_list[16]
        player.img_18th = player.participant.stimuli_id_list[17]
        player.img_19th = player.participant.stimuli_id_list[18]
        player.img_20th = player.participant.stimuli_id_list[19]
        player.img_21st = player.participant.stimuli_id_list[20]
        player.img_22nd = player.participant.stimuli_id_list[21]
        player.img_23rd = player.participant.stimuli_id_list[22]
        player.img_24th = player.participant.stimuli_id_list[23]
        player.img_25th = player.participant.stimuli_id_list[24]
        player.img_26th = player.participant.stimuli_id_list[25]
        player.img_27th = player.participant.stimuli_id_list[26]
        player.img_28th = player.participant.stimuli_id_list[27]
        player.img_29th = player.participant.stimuli_id_list[28]
        player.img_30th = player.participant.stimuli_id_list[29]
        player.img_31st = player.participant.stimuli_id_list[30]
        player.img_32nd = player.participant.stimuli_id_list[31]
        player.img_33rd = player.participant.stimuli_id_list[32]
        player.img_34th = player.participant.stimuli_id_list[33]
        player.img_35th = player.participant.stimuli_id_list[34]
        player.img_36th = player.participant.stimuli_id_list[35]
        player.img_37th = player.participant.stimuli_id_list[36]
        player.img_38th = player.participant.stimuli_id_list[37]
        player.img_39th = player.participant.stimuli_id_list[38]
        player.img_40th = player.participant.stimuli_id_list[39]
        return {
            "name_order" : player.name_order,
            "dict" : player.participant.img2category,
            "img0" : player.participant.imgPathSeries[0],
            "img1" : player.participant.imgPathSeries[1],
            "img2" : player.participant.imgPathSeries[2],
            "img3" : player.participant.imgPathSeries[3],
            "img4" : player.participant.imgPathSeries[4],
            "img5" : player.participant.imgPathSeries[5],
            "img6" : player.participant.imgPathSeries[6],
            "img7" : player.participant.imgPathSeries[7],
            "img8" : player.participant.imgPathSeries[8],
            "img9" : player.participant.imgPathSeries[9],
            "img10" : player.participant.imgPathSeries[10],
            "img11" : player.participant.imgPathSeries[11],
            "img12" : player.participant.imgPathSeries[12],
            "img13" : player.participant.imgPathSeries[13],
            "img14" : player.participant.imgPathSeries[14],
            "img15" : player.participant.imgPathSeries[15],
            "img16" : player.participant.imgPathSeries[16],
            "img17" : player.participant.imgPathSeries[17],
            "img18" : player.participant.imgPathSeries[18],
            "img19" : player.participant.imgPathSeries[19],
            "img20" : player.participant.imgPathSeries[20],
            "img21" : player.participant.imgPathSeries[21],
            "img22" : player.participant.imgPathSeries[22],
            "img23" : player.participant.imgPathSeries[23],
            "img24" : player.participant.imgPathSeries[24],
            "img25" : player.participant.imgPathSeries[25],
            "img26" : player.participant.imgPathSeries[26],
            "img27" : player.participant.imgPathSeries[27],
            "img28" : player.participant.imgPathSeries[28],
            "img29" : player.participant.imgPathSeries[29],
            "img30" : player.participant.imgPathSeries[30],
            "img31" : player.participant.imgPathSeries[31],
            "img32" : player.participant.imgPathSeries[32],
            "img33" : player.participant.imgPathSeries[33],
            "img34" : player.participant.imgPathSeries[34],
            "img35" : player.participant.imgPathSeries[35],
            "img36" : player.participant.imgPathSeries[36],
            "img37" : player.participant.imgPathSeries[37],
            "img38" : player.participant.imgPathSeries[38],
            "img39" : player.participant.imgPathSeries[39],
            "img0_cat" : player.img0_cat, "img1_cat" : player.img1_cat, 
            "img2_cat" : player.img2_cat, "img3_cat" : player.img3_cat,
            "img4_cat" : player.img4_cat, "img5_cat" : player.img5_cat,
            "img6_cat" : player.img6_cat, "img7_cat" : player.img7_cat,
            "img8_cat" : player.img8_cat, "img9_cat" : player.img9_cat,
            "img10_cat" : player.img10_cat, "img11_cat" : player.img11_cat, 
            "img12_cat" : player.img12_cat, "img13_cat" : player.img13_cat,
            "img14_cat" : player.img14_cat, "img15_cat" : player.img15_cat,
            "img16_cat" : player.img16_cat, "img17_cat" : player.img17_cat,
            "img18_cat" : player.img18_cat, "img19_cat" : player.img19_cat,
            "img20_cat" : player.img20_cat, "img21_cat" : player.img21_cat,
            "img22_cat" : player.img22_cat, "img23_cat" : player.img23_cat,
            "img24_cat" : player.img24_cat, "img25_cat" : player.img25_cat,
            "img26_cat" : player.img26_cat, "img27_cat" : player.img27_cat,
            "img28_cat" : player.img28_cat, "img29_cat" : player.img29_cat,
            "img30_cat" : player.img30_cat, "img31_cat" : player.img31_cat,
            "img32_cat" : player.img32_cat, "img33_cat" : player.img33_cat,
            "img34_cat" : player.img34_cat, "img35_cat" : player.img35_cat,
            "img36_cat" : player.img36_cat, "img37_cat" : player.img37_cat,
            "img38_cat" : player.img38_cat, "img39_cat" : player.img39_cat,
        }
    
    @staticmethod
    def js_vars(player):
        return dict(
            id_order=player.participant.stimuli_id_list,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.img2category[player.participant.imgPathSeries[0]] = player.img0_cat
        player.participant.img2category[player.participant.imgPathSeries[1]] = player.img1_cat
        player.participant.img2category[player.participant.imgPathSeries[2]] = player.img2_cat
        player.participant.img2category[player.participant.imgPathSeries[3]] = player.img3_cat
        player.participant.img2category[player.participant.imgPathSeries[4]] = player.img4_cat
        player.participant.img2category[player.participant.imgPathSeries[5]] = player.img5_cat
        player.participant.img2category[player.participant.imgPathSeries[6]] = player.img6_cat
        player.participant.img2category[player.participant.imgPathSeries[7]] = player.img7_cat
        player.participant.img2category[player.participant.imgPathSeries[8]] = player.img8_cat
        player.participant.img2category[player.participant.imgPathSeries[9]] = player.img9_cat
        player.participant.img2category[player.participant.imgPathSeries[10]] = player.img10_cat
        player.participant.img2category[player.participant.imgPathSeries[11]] = player.img11_cat
        player.participant.img2category[player.participant.imgPathSeries[12]] = player.img12_cat
        player.participant.img2category[player.participant.imgPathSeries[13]] = player.img13_cat
        player.participant.img2category[player.participant.imgPathSeries[14]] = player.img14_cat
        player.participant.img2category[player.participant.imgPathSeries[15]] = player.img15_cat
        player.participant.img2category[player.participant.imgPathSeries[16]] = player.img16_cat
        player.participant.img2category[player.participant.imgPathSeries[17]] = player.img17_cat
        player.participant.img2category[player.participant.imgPathSeries[18]] = player.img18_cat
        player.participant.img2category[player.participant.imgPathSeries[19]] = player.img19_cat
        player.participant.img2category[player.participant.imgPathSeries[20]] = player.img20_cat
        player.participant.img2category[player.participant.imgPathSeries[21]] = player.img21_cat
        player.participant.img2category[player.participant.imgPathSeries[22]] = player.img22_cat
        player.participant.img2category[player.participant.imgPathSeries[23]] = player.img23_cat
        player.participant.img2category[player.participant.imgPathSeries[24]] = player.img24_cat
        player.participant.img2category[player.participant.imgPathSeries[25]] = player.img25_cat
        player.participant.img2category[player.participant.imgPathSeries[26]] = player.img26_cat
        player.participant.img2category[player.participant.imgPathSeries[27]] = player.img27_cat
        player.participant.img2category[player.participant.imgPathSeries[28]] = player.img28_cat
        player.participant.img2category[player.participant.imgPathSeries[29]] = player.img29_cat
        player.participant.img2category[player.participant.imgPathSeries[30]] = player.img30_cat
        player.participant.img2category[player.participant.imgPathSeries[31]] = player.img31_cat
        player.participant.img2category[player.participant.imgPathSeries[32]] = player.img32_cat
        player.participant.img2category[player.participant.imgPathSeries[33]] = player.img33_cat
        player.participant.img2category[player.participant.imgPathSeries[34]] = player.img34_cat
        player.participant.img2category[player.participant.imgPathSeries[35]] = player.img35_cat
        player.participant.img2category[player.participant.imgPathSeries[36]] = player.img36_cat
        player.participant.img2category[player.participant.imgPathSeries[37]] = player.img37_cat
        player.participant.img2category[player.participant.imgPathSeries[38]] = player.img38_cat
        player.participant.img2category[player.participant.imgPathSeries[39]] = player.img39_cat


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


page_sequence = [Introduction, Categorize, ResultsWaitPage, Results]
