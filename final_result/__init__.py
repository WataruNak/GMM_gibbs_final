from otree.api import *


doc = """
Your app description
"""

def make_html_list(img_num, path_list, height, width):
    img_html_list = []
    for a in range(img_num):
        img_html_list.append(
            "<img src=\"{}\" height=\"{}px\" width=\"{}px\">".format(path_list[a], height, width)
        )
    return img_html_list


def custom_export(players):
    yield [
        "session",
        "participant_code",
        "id_in_group",
        "final_round_num",
        "final_kappa",
        "final_ari"
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.id_in_group,
            p.final_round_num,
            p.final_kappa,
            p.final_ari,
            ]


class Constants(BaseConstants):
    name_in_url = 'final_result'
    players_per_group = 2
    num_rounds = 1
    imgpath_list = [
        "https://imgur.com/wqnOMfy.jpg","https://imgur.com/LHJYfxo.jpg","https://imgur.com/9Xa4VnX.jpg","https://imgur.com/D91W1KT.jpg",
        "https://imgur.com/J35mb8e.jpg","https://imgur.com/IC9TPNn.jpg","https://imgur.com/cJQIb6k.jpg","https://imgur.com/2rj1L4f.jpg",
        "https://imgur.com/CeGed6S.jpg","https://imgur.com/u28iEnb.jpg","https://imgur.com/N1rDlYe.jpg","https://imgur.com/4uFfzbw.jpg",
        "https://imgur.com/ATEBW84.jpg","https://imgur.com/OUEAyTS.jpg","https://imgur.com/oLE2TWf.jpg","https://imgur.com/xiGpQvF.jpg",
        "https://imgur.com/NnOAzoD.jpg","https://imgur.com/0wGJ58N.jpg","https://imgur.com/nitf5Sq.jpg","https://imgur.com/dwXrpvH.jpg",
        "https://imgur.com/K8sGXHa.jpg","https://imgur.com/XejnHhh.jpg","https://imgur.com/yFw1I6M.jpg","https://imgur.com/iuGyxnS.jpg",
        "https://imgur.com/zysvnS8.jpg","https://imgur.com/jv5EHuP.jpg","https://imgur.com/fqjlV3Y.jpg","https://imgur.com/2NYuf1e.jpg",
        "https://imgur.com/jy5MPbW.jpg","https://imgur.com/7Rf9TKU.jpg","https://imgur.com/BgSfDLZ.jpg","https://imgur.com/3sfX7Mr.jpg",
        "https://imgur.com/6R8GCoP.jpg","https://imgur.com/A5ju4zJ.jpg","https://imgur.com/QF9ee5p.jpg","https://imgur.com/vW5QaBq.jpg",
        "https://imgur.com/NcY47LO.jpg","https://imgur.com/GDI9kz8.jpg","https://imgur.com/OmiMBXk.jpg","https://imgur.com/in0lSLH.jpg",
    ]
    namepath_list = [
        "https://imgur.com/a1HYfcA.png","https://imgur.com/xMBZ0Dg.png","https://imgur.com/Xh5Scyo.png",
        "https://imgur.com/PBZ3YNV.png","https://imgur.com/dmiNF4h.png","https://imgur.com/RdWIiGo.png",
        ]
    img_html_list = make_html_list(40, imgpath_list, 50, 50)
    name_html_list = make_html_list(6, namepath_list, 50, 50)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_round_num = models.IntegerField()
    final_kappa = models.FloatField()
    final_ari = models.FloatField()


# PAGES
class FinalResults(Page):
    @staticmethod
    def vars_for_template(player: Player):
        my_dict = {}
        others_dict = {}
        other_player = player.get_others_in_group()[0]
        for id in player.participant.stimuli_id_list:
            my_dict[Constants.img_html_list[id]] = player.participant.img_category_list[id]
        for oid in other_player.participant.stimuli_id_list:
            others_dict[Constants.img_html_list[oid]] = other_player.participant.img_category_list[oid]
        
        player.final_round_num = player.participant.final_round_num
        player.final_ari = player.participant.final_ari
        player.final_kappa = player.participant.final_kappa
        return {
            "final_round_num" : player.participant.final_round_num,
            "kappa": player.participant.final_kappa,
            "ari": player.participant.final_ari,
            "my_dict" : my_dict,
            "others_dict" : others_dict,
            "name0" : Constants.name_html_list[0],
            "name1" : Constants.name_html_list[1],
            "name2" : Constants.name_html_list[2],
            "name3" : Constants.name_html_list[3],
            "name4" : Constants.name_html_list[4],
            "name5" : Constants.name_html_list[5],
        }

page_sequence = [FinalResults]
