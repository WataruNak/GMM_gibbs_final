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
        "final_c_kappa,",
        "final_ip_kappa",
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
            p.final_c_kappa,
            p.final_ip_kappa,
            p.final_ari,
            ]


class Constants(BaseConstants):
    name_in_url = 'final_result'
    players_per_group = 2
    num_rounds = 1
    imgpath_list = [
        "https://imgur.com/gubdkt0.jpg","https://imgur.com/BteivhO.jpg","https://imgur.com/otWcXp5.jpg","https://imgur.com/BwZcuBw.jpg",
        "https://imgur.com/fZRcZg0.jpg","https://imgur.com/HxGqKu1.jpg","https://imgur.com/3oIIr67.jpg","https://imgur.com/qRuBkRm.jpg",
        "https://imgur.com/tDUCcFe.jpg","https://imgur.com/5LnW1cL.jpg","https://imgur.com/B8sx0kD.jpg","https://imgur.com/g8Cmjez.jpg",
        "https://imgur.com/iP5SV7e.jpg","https://imgur.com/XAbgTOc.jpg","https://imgur.com/px8BCcT.jpg","https://imgur.com/WLOcyhk.jpg",
        "https://imgur.com/st6BOzf.jpg","https://imgur.com/2GknAAv.jpg","https://imgur.com/nMGFQ9S.jpg","https://imgur.com/5Tnbba6.jpg",
        "https://imgur.com/UAQ4IxZ.jpg","https://imgur.com/u30m8NG.jpg","https://imgur.com/Ad0CDOW.jpg","https://imgur.com/UdNELcS.jpg",
        "https://imgur.com/OvSCL1C.jpg","https://imgur.com/Let0gsJ.jpg","https://imgur.com/XDmWi91.jpg","https://imgur.com/faOrbC9.jpg",
        "https://imgur.com/Kll1v00.jpg","https://imgur.com/04EJwCc.jpg","https://imgur.com/C3aTj09.jpg","https://imgur.com/79bmUFm.jpg",
        "https://imgur.com/gk2Yjar.jpg","https://imgur.com/6OCJPMi.jpg","https://imgur.com/8cV6OEF.jpg","https://imgur.com/VcviHH3.jpg",
        "https://imgur.com/iD3xLvL.jpg","https://imgur.com/CK9wKWO.jpg","https://imgur.com/6F2Phvt.jpg","https://imgur.com/xQ65RB7.jpg"
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
    final_c_kappa = models.FloatField()
    final_ip_kappa = models.FloatField()
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
        player.final_c_kappa = player.participant.final_c_kappa
        player.final_ip_kappa = player.participant.final_ip_kappa
        return {
            "final_round_num" : player.participant.final_round_num,
            "c_kappa": player.participant.final_c_kappa,
            "ip_kappa": player.participant.final_ip_kappa,
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
