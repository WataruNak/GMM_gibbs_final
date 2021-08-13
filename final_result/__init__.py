from otree.api import *


doc = """
Your app description
"""

def make_img_html_list(height, width):
    img_html_list = [
        "<img src = \"https://imgur.com/wqnOMfy.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/LHJYfxo.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/9Xa4VnX.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/D91W1KT.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/J35mb8e.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/IC9TPNn.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/cJQIb6k.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/2rj1L4f.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/CeGed6S.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/u28iEnb.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/N1rDlYe.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/4uFfzbw.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/ATEBW84.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/OUEAyTS.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/oLE2TWf.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/xiGpQvF.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/NnOAzoD.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/0wGJ58N.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/nitf5Sq.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/dwXrpvH.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/K8sGXHa.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/XejnHhh.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/yFw1I6M.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/iuGyxnS.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/zysvnS8.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/jv5EHuP.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/fqjlV3Y.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/2NYuf1e.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/jy5MPbW.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/7Rf9TKU.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/BgSfDLZ.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/3sfX7Mr.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/6R8GCoP.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/A5ju4zJ.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/QF9ee5p.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/vW5QaBq.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/NcY47LO.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/GDI9kz8.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/OmiMBXk.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/in0lSLH.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        ]
    return img_html_list
    
def make_name_html_list(height, width):
    img_html_list = [
        "<img src=\"https://imgur.com/a1HYfcA.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/xMBZ0Dg.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/Xh5Scyo.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/PBZ3YNV.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/dmiNF4h.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/RdWIiGo.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        ]
    return img_html_list


class Constants(BaseConstants):
    name_in_url = 'final_result'
    players_per_group = 2
    num_rounds = 1
    img_html_list = make_img_html_list(50, 50)
    name_html_list = make_name_html_list(50, 50)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class FinalResults(Page):
    @staticmethod
    def vars_for_template(player: Player):
        my_dict = {}
        others_dict = {}
        other_player = player.get_others_in_group()[0]
        for id in player.participant.stimuli_id_list:
            my_dict[Constants.img_html_list[id]] = player.patcitipant.img_category_list[id]
        for oid in other_player.participant.stimuli_id_list:
            others_dict[Constants.img_html_list[oid]] = other_player.patcitipant.img_category_list[oid]
        return {
            "final_round_num" : player.participant.final_round_num,
            "final_kappa": player.participant.final_kappa,
            "final_ari": player.participant.final_ari,
            "my_dict" : my_dict,
            "others_dict" : others_dict,
            "name_html_list" : Constants.name_html_list,
            "loghtml_list" : player.participant.loghtml_list,
        }



page_sequence = [FinalResults]
