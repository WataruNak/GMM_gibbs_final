from otree.api import *
import random

doc = """
from random import choices
from ssl import OP_NO_COMPRESSION
from matplotlib import widgets
from GMM_gibbs_final.categorization_mid import Introduction

SPQ-B
OCI
PHQ-9
STAI
 状態不安の逆転項目: 1, 2, 5, 8, 10, 11, 15, 16, 19, 20
 特性不安の逆転項目: 1, 6, 7, 10, 13, 16, 19
AQ
 1か2なら1点 : 2, 4, 5, 6, 7, 9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41, 42, 43, 45, 46
 残りは3か4なら1点
ASRS
AUDIT
EAT-26
DSM-5 level1
SES
background

keycode 1st:
"ab074827",
"cd586926",
"ef275501",
"gh754320"
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaires'
    players_per_group = None
    num_rounds = 1

    keycode_list = [
        "dgq7650fg",
        "dmx6922je",
        "wwl3107dq",
        "pso5025cc"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #SPQ-B
    L_1 = models.IntegerField(
        label="この項目では「はい」と回答してください",
        choices = [
            [0, "はい"],
            [1, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_1 = models.IntegerField(
        label="他人は私のことを、少し変わった突飛な人だと思っている",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_2 = models.IntegerField(
        label="姿は見えないが、私のまわりに人がいると感じたり、見えない力が存在すると感じたりしたことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_3 = models.IntegerField(
        label="私の変な癖や習慣について、人にいろいろ言われる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_4 = models.IntegerField(
        label="私が考えていることを、他の人にわかられてしまうと確信したことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_5 = models.IntegerField(
        label="ありふれた物や出来事が、私のための特別な合図であるらしいと気づいたことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_6 = models.IntegerField(
        label="私のことをとても変人だと思っている人もいる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_7 = models.IntegerField(
        label="友達と一緒の時でも、用心しないといけないと感じることがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_8 = models.IntegerField(
        label="私の話はとらえどころがなくてわかりにくいと思っている人もいる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_9 = models.IntegerField(
        label="他人が言ったりしたりすることの中に、脅しや嫌がらせが隠されていると感じることがしばしばある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_10 = models.IntegerField(
        label="買い物をしているとき、他の人たちが私に注意を向けているような気がする",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_11 = models.IntegerField(
        label="知らない人たちと話をしなければならない時には、とても居心地が悪い",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_12 = models.IntegerField(
        label="占星術・未来予知・UFO・ESP(超感覚的知覚)・第六感などを体験したことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_13 = models.IntegerField(
        label="ときどき、人とは違う言葉の使い方をすることがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_14 = models.IntegerField(
        label="自分のことについて、他人に教えすぎないのが一番よいと思う",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_15 = models.IntegerField(
        label="社交の場では、あまり目立たないようにしている方である",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_16 = models.IntegerField(
        label="ふだんなら気づかないような遠くの物音を聞いて、びっくりしたことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_17 = models.IntegerField(
        label="話している時、相手と目を合わせないようにしがちである",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_18 = models.IntegerField(
        label="他の人とは親しくなれないと感じる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_19 = models.IntegerField(
        label="私はふつうとは違う、変わった人間である",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_20 = models.IntegerField(
        label="言いたいことを人に明確に伝えるのは、私には難しい",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_21 = models.IntegerField(
        label="よく知らない人たちに話しかけるのはとても緊張する",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_22 = models.IntegerField(
        label="感情を表に出さない方である",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    
    #OCI
    oci_1 = models.IntegerField(
        label="自分の意思に反して不快な考えが頭の中にうかび、私はその考えをとりのぞくことができない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_2 = models.IntegerField(
        label="身体から出る分泌物 (汗、唾液、血液、尿など) に接触すると、自分の衣服が汚染されるかもしれない、何かしら自分の害になるかもしれないと私は思う",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_3 = models.IntegerField(
        label="はじめから理解していたとしても、何度か繰り返し言ってもらうよう、私は他人に頼む",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_4 = models.IntegerField(
        label="私は強迫的に洗ったりきれいにしたりする",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_5 = models.IntegerField(
        label="自分が何か間違ったことをしなかったか確認するため、過去の出来事や会話、行動を、私は頭の中で思い返さなければならない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_6 = models.IntegerField(
        label="私は邪魔になるほどたくさんのものを溜めてきた",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_7 = models.IntegerField(
        label="私は必要以上頻繁に物事を確認する",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_8 = models.IntegerField(
        label="病気や汚染を恐れるため、私は公衆トイレの使用を避けている",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_9 = models.IntegerField(
        label="ドア、窓、引き出しなどを、私は繰り返し確認する",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_10 = models.IntegerField(
        label="ガス栓や水道の蛇口を閉めた後、電気のスイッチを消した後で、私は繰り返し確認する",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_11 = models.IntegerField(
        label="私は必要でないものを収集する",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_12 = models.IntegerField(
        label="知らず知らずに誰かを傷つけてしまった、という考えが浮かぶ",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_13 = models.IntegerField(
        label="自分自身や他人を傷つけたいのかもしれない、という考えが浮かぶ",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_14 = models.IntegerField(
        label="物がきちんと整理されていないと、私は取り乱す",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_15 = models.IntegerField(
        label="私は特定の順序で服を着たり、脱いだり、自分の身体を洗ったりしなければならない気がする",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_16 = models.IntegerField(
        label="何かをしているときに、私は数を数えなければならない気がする",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_17 = models.IntegerField(
        label="恥ずかしいことや有害なことを衝動的にやってしまうのではないかと、私は心配している",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_18 = models.IntegerField(
        label="いやな考えや気持ちを中和するため、私は祈らなければならない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_19 = models.IntegerField(
        label="記入した用紙や文書などを私は確認し続ける",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_20 = models.IntegerField(
        label="万が一コントロールを失ったときのことを考え、ナイフやはさみ、その他のとがったものを見ると、私は動揺してしまう",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_21 = models.IntegerField(
        label="私は清潔であることを過剰に気にかける",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_22 = models.IntegerField(
        label="見知らぬ人や、特定の人が触ったと分かっているものに触れるのは難しい",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_23 = models.IntegerField(
        label="私は特定の順序で物を並べなければならない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_24 = models.IntegerField(
        label="私は何度も何度も同じ事を繰り返すため、仕事に遅れが生じる",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_25 = models.IntegerField(
        label="私は特定の数字を繰り返さなければならない気がする",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_26 = models.IntegerField(
        label="何かを注意深くやった後でも、それがまだ終わっていないような気がする",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_27 = models.IntegerField(
        label="私はゴミ箱や汚いものに触るのが難しい",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_28 = models.IntegerField(
        label="私は、自分自身の考えをコントロールすることが難しい",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_29 = models.IntegerField(
        label="何度も何度もしっくりくるまで、私は物事を繰り返さなければならない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_30 = models.IntegerField(
        label="自分の意思に反し頭のなかに入ってくる不快な考えに、私はうろたえてしまう",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_31 = models.IntegerField(
        label="寝る前、決まったことを決まったやり方で、私はやらなければならない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_32 = models.IntegerField(
        label="誰にも危害を与えていないことを確認するために、私は元の場所に戻ることがある",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_33 = models.IntegerField(
        label="しばしば嫌な考えが浮かび、私はそれを取り除くことが難しい",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_34 = models.IntegerField(
        label="後になって必要になるかもしれないと思い、私は物を捨てないようにしている",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_35 = models.IntegerField(
        label="自分で物事を整えたやり方を他人に変えられると、私はたまらなく感じる",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_36 = models.IntegerField(
        label="悪い考え、感情、行動をすっかり消し去るため、決まった言葉やフレーズを、私は頭の中で繰り返さなければならない気がする",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_37 = models.IntegerField(
        label="何かを自分がし終えた後にも、本当にやったのかという疑念が続いて止まない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_38 = models.IntegerField(
        label="汚れた気がするというだけの理由で、私はときどき、自分自身を洗ったりきれいにしたりしなければならない",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_39 = models.IntegerField(
        label="私はよい数字と悪い数字があると感じる",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_40 = models.IntegerField(
        label="火事を起こしかねないものは何でも、私は繰り返し確認する",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_41 = models.IntegerField(
        label="何かを注意深くやったときでも、まだしっくりこない気がする",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    oci_42 = models.IntegerField(
        label="私は必要以上なほど頻繁に、もしくは長く手を洗う",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    
    #PHQ-9
    phq_9_1 = models.IntegerField(
        label="物事に対してほとんど興味がない、または楽しめない",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_2 = models.IntegerField(
        label="気分が落ち込む、憂うつになる、または絶望的な気持ちになる",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_3 = models.IntegerField(
        label="寝付きが悪い、途中で目がさめる、または逆に眠り過ぎる",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_4 = models.IntegerField(
        label="疲れた感じがする、または気力がない",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_5 = models.IntegerField(
        label="あまり食欲がない、または食べ過ぎる",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_6 = models.IntegerField(
        label="自分はダメな人間だ、人生の敗北者だと気に病む、または自分自身あるいは家族に申し訳がないと感じる",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_7 = models.IntegerField(
        label="新聞を読む、またはテレビを見ることなどに集中することが難しい",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_8 = models.IntegerField(
        label="他人が気づくぐらいに動きや話し方が遅くなる、あるいは反対に、そわそわしたり、落ちつかず、ふだんよりも動き回ることがある",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    phq_9_9 = models.IntegerField(
        label="死んだ方がましだ、あるいは自分を何らかの方法で傷つけようと思ったことがある",
        choices = [0, 1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    
    #STAI X-I(state)
    stai_s_1 = models.IntegerField(
        label="平静である。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_2 = models.IntegerField(
        label="安心している。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_3 = models.IntegerField(
        label="固くなっている。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_4 = models.IntegerField(
        label="後悔している。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_5 = models.IntegerField(
        label="ホッとしている。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_6 = models.IntegerField(
        label="動転している。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_7 = models.IntegerField(
        label="まずいことが起こりそうで心配である。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_8 = models.IntegerField(
        label="ゆったりとした気持ちである。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_9 = models.IntegerField(
        label="不安である。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_10 = models.IntegerField(
        label="気分がよい。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_11 = models.IntegerField(
        label="自信がある。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_12 = models.IntegerField(
        label="ピリピリしている。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_13 = models.IntegerField(
        label="イライラしている。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_14 = models.IntegerField(
        label="緊張している。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_15 = models.IntegerField(
        label="リラックスしている。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_16 = models.IntegerField(
        label="満足している。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_17 = models.IntegerField(
        label="心配している。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_18 = models.IntegerField(
        label="ひどく興奮し，ろうばいしている。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_19 = models.IntegerField(
        label="ウキウキしている。 ",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_s_20 = models.IntegerField(
        label="楽しい。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    
    #STAI X-II(trait)
    stai_t_1 = models.IntegerField(
        label="楽しい。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_2 = models.IntegerField(
        label="疲れやすい。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_3 = models.IntegerField(
        label="泣きだしたくなる。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_4 = models.IntegerField(
        label="ほかの人と同じくらい幸せであったならと思う。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_5 = models.IntegerField(
        label="すぐに決心がつかず迷いやすい。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_6 = models.IntegerField(
        label="ゆったりした気持ちである。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_7 = models.IntegerField(
        label="平静・沈着で落ち着いている。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_8 = models.IntegerField(
        label="困難なことが重なると圧倒されてしまう。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_9 = models.IntegerField(
        label="実際に大したこともないが気になって仕方がない。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_10 = models.IntegerField(
        label="幸せである。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_11 = models.IntegerField(
        label="物事を難しく考える傾向がある。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_12 = models.IntegerField(
        label="自信が欠如している。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_13 = models.IntegerField(
        label="安心している。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_14 = models.IntegerField(
        label="やっかいなことは避けて通ろうとする。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_15 = models.IntegerField(
        label="憂うつである。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_16 = models.IntegerField(
        label="満足している。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_17 = models.IntegerField(
        label="些細なことに思いわずらう。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_18 = models.IntegerField(
        label="ひどくがっかりしたときには気分転換ができない。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_19 = models.IntegerField(
        label="物に動じないほうである。",
        choices = [
            [4, "1"],
            [3, "2"],
            [2, "3"],
            [1, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    stai_t_20 = models.IntegerField(
        label="身近な問題を考えるとひどく緊張し混乱する。",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    
    #AQ
    aq_1 = models.IntegerField(
        label="何かをするときには、一人でするよりも他の人といっしょにする方が好きだ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_2 = models.IntegerField(
        label="同じやりかたを何度もくりかえし用いることが好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_3 = models.IntegerField(
        label="何かを想像するとき、映像（イメージ）を簡単に思い浮かべることができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_4 = models.IntegerField(
        label="ほかのことがぜんぜん気にならなくなる（目に入らなくなる）くらい、何かに没頭してしまうことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_5 = models.IntegerField(
        label="他の人が気がつかないような小さい物音に気がつくことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_6 = models.IntegerField(
        label="車のナンバーや時刻表の数字などの一連の数字や、特に意味のない情報に注目する（こだわる）ことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_7 = models.IntegerField(
        label="自分ではていねいに話したつもりでも、話し方が失礼だと周囲の人から言われることがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_8 = models.IntegerField(
        label="小説などの物語を読んでいるとき、登場人物がどのような人か（外見など）について簡単にイメージすることができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_9 = models.IntegerField(
        label="日付についてのこだわりがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_10 = models.IntegerField(
        label="パーティや会合などで、いろいろな人の会話についていくことが簡単にできる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_11 = models.IntegerField(
        label="自分がおかれている社会的な状況（自分の立場）がすぐにわかる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_12 = models.IntegerField(
        label="ほかの人は気がつかないような細かいことに、すぐに気づくことが多い。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_13 = models.IntegerField(
        label="パーティなどよりも、図書館に行く方が好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_14 = models.IntegerField(
        label="作り話には、すぐに気がつく（すぐわかる）。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_15 = models.IntegerField(
        label="モノよりも人間の方に魅力を感じる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_16 = models.IntegerField(
        label="それをそうすることができないとひどく混乱して（パニックになって）しまうほど、何かに強い興味を持つことがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_17 = models.IntegerField(
        label="他の人と、雑談などのような社交的な会話を楽しむことができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_18 = models.IntegerField(
        label="自分が話をしているときには、なかなか他の人に横から口をはさませない。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_19 = models.IntegerField(
        label="数字に対するこだわりがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_20 = models.IntegerField(
        label="小説などを読んだり、テレビでドラマなどを観ているとき、登場人物の意図をよく理解できないことがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_21 = models.IntegerField(
        label="小説のようなフィクションを読むのは、あまり好きではない。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_22 = models.IntegerField(
        label="新しい友人を作ることは、むずかしい。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_23 = models.IntegerField(
        label="いつでも、ものごとの中に何らかのパターン（型や決まりなど）のようなものに気づく。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_24 = models.IntegerField(
        label="博物館に行くよりも、劇場に行く方が好きだ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_25 = models.IntegerField(
        label="自分の目標が妨害されても、混乱することはない。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_26 = models.IntegerField(
        label="会話をどのように進めたらいいのか、わからなくなってしまうことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_27 = models.IntegerField(
        label="誰かと話をしているときに、相手の話の‘言外の意味’を理解することは容易である。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_28 = models.IntegerField(
        label="細部よりも全体像に注意が向くことが多い。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_29 = models.IntegerField(
        label="電話番号をおぼえるのは苦手だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_30 = models.IntegerField(
        label="状況（部屋の様子やものなど）や人間の外見（服装や髪型）などが、いつもとちょっと違っているくらいでは、すぐには気がつかないことが多い。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_31 = models.IntegerField(
        label="自分の話を聞いている相手が退屈しているときには、どのように話をすればいいかわかっている。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_32 = models.IntegerField(
        label="同時に２つ以上のことをするのは、かんたんである。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_33 = models.IntegerField(
        label="電話で話をしているとき、自分が話をするタイミングがわからないことがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_34 = models.IntegerField(
        label="自分から進んで何かをすることは楽しい。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_35 = models.IntegerField(
        label="冗談がわからないことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_36 = models.IntegerField(
        label="相手の顔を見れば、その人が考えていることや感じていることがわかる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_37 = models.IntegerField(
        label="じゃまが入って何かを中断されても、すぐにそれまでやっていたことに戻ることができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_38 = models.IntegerField(
        label="人と雑談のような社交的な会話をすることが得意だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_39 = models.IntegerField(
        label="同じことを何度も繰り返していると、周囲の人からよく言われる。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_40 = models.IntegerField(
        label="子どものころ、友達といっしょに、よく‘○○ごっこ’（ごっこ遊び）をして遊んでいた。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_41 = models.IntegerField(
        label="特定の種類のものについての（車について、鳥について、植物についてのような）情報を集めることが好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_42 = models.IntegerField(
        label="あること（もの）を、他の人がどのように感じるかを想像するのは苦手だ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_43 = models.IntegerField(
        label="自分がすることはどんなことでも慎重に計画するのが好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_44 = models.IntegerField(
        label="社交的な場面（機会）は楽しい。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_45 = models.IntegerField(
        label="他の人の考え（意図）を理解することは苦手だ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_46 = models.IntegerField(
        label="新しい場面（状況）に不安を感じる。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_47 = models.IntegerField(
        label="初対面の人と会うことは楽しい。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_48 = models.IntegerField(
        label="社交的である。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_49 = models.IntegerField(
        label="人の誕生日をおぼえるのは苦手だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_50 = models.IntegerField(
        label="子どもと‘○○ごっこ’をして遊ぶのがとても得意だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    
    #ASRS
    asrs_1 = models.IntegerField(
        label="つまらない、あるいは難しい仕事をする際に、不注意な間違いをすることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_2 = models.IntegerField(
        label="長時間座っていなければならない時に、手足をそわそわと動かしたり、もぞもぞしたりすることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_3 = models.IntegerField(
        label="つまらない、あるいは単調な作業をする際に、注意を集中し続けることが、困難なことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_4 = models.IntegerField(
        label="会議などの着席していなければいけない状況で、席を離れてしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_5 = models.IntegerField(
        label="直接話しかけられているにもかかわらず、話に注意を払うことが困難なことはどれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_6 = models.IntegerField(
        label="落ち着かない、あるいはソワソワした感じが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_7 = models.IntegerField(
        label="物事を行うにあたって、難所は乗り越えたのに、詰めが甘くて仕上げるのが困難だったことが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_8 = models.IntegerField(
        label="時間に余裕があっても、一息ついたり、ゆったりとくつろぐことが困難なことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    L_2 = models.IntegerField(
        label="この項目では「4」と回答してください。",
        choices = [
            [1, "0"],
            [1, "1"],
            [1, "2"],
            [1, "3"],
            [0, "4"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_9 = models.IntegerField(
        label="計画性を要する作業を行う際に、作業を順序だてるのが困難だったことが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_10 = models.IntegerField(
        label="まるで何かに駆り立てられるかのように過度に活動的になったり、何かせずにいられなくなることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_11 = models.IntegerField(
        label="じっくりと考える必要のある課題に取り掛かるのを避けたり、遅らせたりすることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_12 = models.IntegerField(
        label="社交的な場面でしゃべりすぎてしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_13 = models.IntegerField(
        label="家や職場に物を置き忘れたり、物をどこに置いたかわからなくなって探すのに苦労したことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_14 = models.IntegerField(
        label="会話を交わしている相手が話し終える前に会話をさえぎってしまったことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_15 = models.IntegerField(
        label="外からの刺激や雑音で気が散ってしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_16 = models.IntegerField(
        label="順番待ちしなければいけない場合に、順番を待つことが困難なことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_17 = models.IntegerField(
        label="約束や、しなければいけない用事を忘れたことが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_18 = models.IntegerField(
        label="忙しくしている人の邪魔をしてしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    
    #AUDIT
    audit_1 = models.IntegerField(
        label="アルコール含有飲料をどのくらいの頻度で飲みますか?",
        choices = [
            [0, "飲まない"],
            [1, "1ヶ月に1度以下"],
            [2, "1ヶ月に2〜4度"],
            [3, "1週に2〜3度"],
            [4, "1週に4度以上"]
        ],
        widget=widgets.RadioSelect
    )
    audit_2 = models.IntegerField(
        label="飲酒するときは通常どのぐらいの量をのみますか?(1単位=純アルコール9〜12g)　ただし、日本酒1合=2単位、ビール大瓶1本=2.5単位、ウイスキー水割りダブル1杯=2単位、焼酎お湯割り1杯=1単位、ワイングラス1杯=1.5単位、梅酒小コップ1杯=1単位",
        choices = [
            [0, "1〜2単位"],
            [1, "3〜4単位"],
            [2, "5〜6単位"],
            [3, "7〜9単位"],
            [4, "10単位以上"]
        ],
        widget=widgets.RadioSelect
    )
    audit_3 = models.IntegerField(
        label="1度に6単位以上飲酒することがどのくらいの頻度でありますか?",
        choices = [
            [0, "ない"],
            [1, "1ヶ月に1度未満"],
            [2, "1ヶ月に1度"],
            [3, "1週に1度"],
            [4, "毎日あるいはほとんど毎日"]
        ],
        widget=widgets.RadioSelect
    )
    audit_4 = models.IntegerField(
        label="飲み始めると止まらなくなったことがどのくらいの頻度でありましたか?",
        choices = [
            [0, "ない"],
            [1, "1ヶ月に1度未満"],
            [2, "1ヶ月に1度"],
            [3, "1週に1度"],
            [4, "毎日あるいはほとんど毎日"]
        ],
        widget=widgets.RadioSelect
    )
    audit_5 = models.IntegerField(
        label="普通だと行えることが、飲酒していたためにできなかったことがどのくらいの頻度でありましたか?",
        choices = [
            [0, "ない"],
            [1, "1ヶ月に1度未満"],
            [2, "1ヶ月に1度"],
            [3, "1週に1度"],
            [4, "毎日あるいはほとんど毎日"]
        ],
        widget=widgets.RadioSelect
    )
    audit_6 = models.IntegerField(
        label="深酒の後、体調を整えるために、朝、迎え酒をしなければいけなかったことがどのくらいの頻度でありましたか?",
        choices = [
            [0, "ない"],
            [1, "1ヶ月に1度未満"],
            [2, "1ヶ月に1度"],
            [3, "1週に1度"],
            [4, "毎日あるいはほとんど毎日"]
        ],
        widget=widgets.RadioSelect
    )
    audit_7 = models.IntegerField(
        label="飲酒後、罪悪感や自責の念にかられたことが、どのくらいの頻度でありましたか?",
        choices = [
            [0, "ない"],
            [1, "1ヶ月に1度未満"],
            [2, "1ヶ月に1度"],
            [3, "1週に1度"],
            [4, "毎日あるいはほとんど毎日"]
        ],
        widget=widgets.RadioSelect
    )
    audit_8 = models.IntegerField(
        label="飲酒のために、前の日の夜の出来事を思い出せなかったことがどのくらいの頻度でありましたか?",
        choices = [
            [0, "ない"],
            [1, "1ヶ月に1度未満"],
            [2, "1ヶ月に1度"],
            [3, "1週に1度"],
            [4, "毎日あるいはほとんど毎日"]
        ],
        widget=widgets.RadioSelect
    )
    audit_9 = models.IntegerField(
        label="飲酒のために、あなた自身や他の誰かが怪我をしたことがありますか?",
        choices = [
            [0, "ない"],
            [2, "あるが、過去1年にはなし"],
            [4, "過去1年間にあり"]
        ],
        widget=widgets.RadioSelect
    )
    audit_10 = models.IntegerField(
        label="肉親や親戚、友人、上司などがあなたの飲酒を心配したり、飲酒量を減らすように勧めることがありましたか?",
        choices = [
            [0, "ない"],
            [2, "あるが、過去1年にはなし"],
            [4, "過去1年間にあり"]
        ],
        widget=widgets.RadioSelect
    )
    
    #EAT-26
    eat_1 = models.IntegerField(
        label="太りすぎることがこわい",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_2 = models.IntegerField(
        label="おなかがすいたときに食べないようにしている",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_3 = models.IntegerField(
        label="食物のことで頭がいっぱいである",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_4 = models.IntegerField(
        label="やめられないかもしれないと思うほど次から次へと食べ統けることがある",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_5 = models.IntegerField(
        label="食物を小さくきざんで少量ずつ口に入れる",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_6 = models.IntegerField(
        label="自分が食べる食物のカロリー量を知っている",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_7 = models.IntegerField(
        label="炭水化物が多い食物(パン、ごはん、パスタなど)は特に食べないようにしている",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_8 = models.IntegerField(
        label="他の人は、私がもっと食べるようにと望んでいるようだ",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_9 = models.IntegerField(
        label="食べた後に吐く",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_10 = models.IntegerField(
        label="食べた後でひどく悪いことをしたような気になる",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_11 = models.IntegerField(
        label="もっとやせたいという思いで頭がいっぱいである",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_12 = models.IntegerField(
        label="カロリーを使っていることを考えながら運動する",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_13 = models.IntegerField(
        label="他の人は私のことをやせすぎだと思っている",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_14 = models.IntegerField(
        label="自分の身体に脂肪がつきすぎているという考えが頭から離れない",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_15 = models.IntegerField(
        label="他の人よりも食事をするのに時間がかかる",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_16 = models.IntegerField(
        label="砂糖が入っている食物は食べないようにしている",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_17 = models.IntegerField(
        label="ダイエット食品を食べる",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_18 = models.IntegerField(
        label="私の生活は食物にふりまわされている気がする",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_19 = models.IntegerField(
        label="食物に関して自分で自分をコントロールしている",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_20 = models.IntegerField(
        label="他の人が私にもっと食べるように圧力をかけている感じがする",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_21 = models.IntegerField(
        label="食物に関して時間をかけすぎたり、考えすぎたりする",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_22 = models.IntegerField(
        label="甘い物を食べた後で、気分が落ち着かない",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_23 = models.IntegerField(
        label="ダイエットをしている",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_24 = models.IntegerField(
        label="胃が空っぽの状態が好きだ",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_25 = models.IntegerField(
        label="食べたことのないカロリーが高い食物を食べてみることは楽しみだ",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    eat_26 = models.IntegerField(
        label="食事の後で衝動的に吐きたくなる",
        choices = [
            [0, "1"],
            [0, "2"],
            [0, "3"],
            [1, "4"],
            [2, "5"],
            [3, "6"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    
    #DSM-5 level1
    dsm5_1 = models.IntegerField(
        label="物事を行うことへの関心や楽しみが、ほとんどありませんか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_2 = models.IntegerField(
        label="気持ちが沈む、憂うつまたは絶望感がありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_3 = models.IntegerField(
        label="普段よりいらいらする、不機嫌で、怒りっぽいですか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_4 = models.IntegerField(
        label="普段に比べ、睡眠時間が短くなっているものの、まだ十分元気ですか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_5 = models.IntegerField(
        label="普段に比べ、いろいろなことを始めたり、危険なことを行ったりしていますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_6 = models.IntegerField(
        label="くよくよする、不安に感じる、怯える、心配する、ピリピリしますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_7 = models.IntegerField(
        label="パニックになったり怯えている感じがありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_8 = models.IntegerField(
        label="自分を不安にさせる状況を回避しますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_9 = models.IntegerField(
        label="説明がつかない全身のさまざまな痛み(例：頭痛、腰痛、関節痛、腹痛、下肢の痛みなど)がありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_10 = models.IntegerField(
        label="自分の病状が十分、真剣に受け取られていないと感じますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_11 = models.IntegerField(
        label="自分自身を実際に傷つけたいという考えが浮かびますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_12 = models.IntegerField(
        label="誰もいないのに声が聞こえるなど、他人に聞こえないものが聞こえますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_13 = models.IntegerField(
        label="自分の考えを誰かが聞くことができるという感覚、または他人の考えを自分が聞くことができる感覚がありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_14 = models.IntegerField(
        label="睡眠全体の質を低下させる睡眠に関する問題がありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_15 = models.IntegerField(
        label="記憶(例：新しいことを覚えること)や場所探し(例：家までの順路を探す)に関する問題がありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_16 = models.IntegerField(
        label="繰り返して頭に浮かぶ不快な思考、強い衝動、またはイメージがありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_17 = models.IntegerField(
        label="ある特定の行動や精神活動を何回も何回も繰り返して行わなければならないと追い込まれる感覚がありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_18 = models.IntegerField(
        label="自分自身、自分の身体、自分の身体のまわりの環境、自分の記憶が分離または離れている感覚がありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_19 = models.IntegerField(
        label="自分自身が実際は誰であるか、人生から何を得たいかがわからないことがありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_20 = models.IntegerField(
        label="他人と親しみを感じない、もしくはその人達との関係を楽しめないことがありますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_21 = models.IntegerField(
        label="1日に種類を問わず少なくとも4杯のアルコールを摂取しますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_22 = models.IntegerField(
        label="紙巻タバコ、葉巻、パイプ、噛みタバコ、嗅ぎタバコ、電子タバコなどを喫煙しますか？",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    dsm5_23 = models.IntegerField(
        label="以下の薬を自らの判断で使用しますか？(処方箋薬の場合、医師の処方箋なく、または処方用量より多く、または長く使用)[鎮痛薬(アセトアミノフェンなど)、精神刺激薬(メチルフェニデートなど)、鎮静薬・安定薬(睡眠薬やジアゼパムなど)、大麻、クラック・コカイン、クラブ薬物(エクスタシーなど)、幻覚薬(LSDなど)、ヘロイン、有機溶剤(接着剤など)やメタンフェタミン(スピードなど)の違法薬物]",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    
    #SES
    ses_1 = models.IntegerField(
        label="私の家族は生活するのに十分なお金を持っていた",
        choices = [1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )
    ses_2 = models.IntegerField(
        label="私は比較的裕福な地域で育った",
        choices = [1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )
    ses_3 = models.IntegerField(
        label="私は学校の他の子供たちと比べて裕福であると感じていた",
        choices = [1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )
    ses_4 = models.IntegerField(
        label="私は欲しい物を買えるお金を持っている",
        choices = [1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )
    ses_5 = models.IntegerField(
        label="私はお金を支払う事に対してあまり躊躇することがない",
        choices = [1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )
    ses_6 = models.IntegerField(
        label="私は将来的にお金の心配をする必要があるとは思わない",
        choices = [1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )
    
    #othres
    age = models.IntegerField(label="1. 年齢：")
    sex = models.IntegerField(
        label="2. 性別：",
        choices = [
            [0, "男性"],
            [1, "女性"],
            [2, "答えたくない"]
        ],
        widget=widgets.RadioSelectHorizontal
        )
    education = models.IntegerField(
        label="3. 最終学歴：",
        choices = [
            [0, "中学校卒業"],
            [1, "高校卒業"],
            [2, "大学卒業"],
            [3, "大学院卒業"]
        ],
        widget=widgets.RadioSelectHorizontal
        )
    profession = models.IntegerField(
        label="4. 職業：",
        choices = [
            [0, "会社員"],
            [1, "公務員"],
            [2, "自営業"],
            [3, "会社役員"],
            [4, "自由業"],
            [5, "専業主婦(夫)"],
            [6, "学生"],
            [7, "パート・アルバイト"],
            [8, "無職"],
            [9, "その他"],
        ],
        widget=widgets.RadioSelect
    )
    height = models.IntegerField(label="5. 身長(半角、1の位まで)：")
    weight = models.IntegerField(label="6. 体重(半角、1の位まで)：")
    pmh = models.IntegerField(
        label = "7. これまで医師による精神疾患の診断を受けたことがありますか？",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    what_pmh = models.IntegerField(
        label="8. その診断名はどれですか？",
        choices = [
            [0, "統合失調症"],
            [1, "躁うつ病/うつ病"],
            [2, "不安障害（パニック障害を含む）"],
            [3, "強迫性障害"],
            [4, "発達障害(自閉スペクトラム症、ADHD、広汎性発達障害を含む)"],
            [5, "その他/分からない"]
        ],
        widget=widgets.RadioSelect,
        initial=99,
        blank=True
    )

def custom_export(players):
    yield [
        "session",
        "participant_code", "started_time",
        "age", "sex", "education", "profession", "height", "weight", "pmh", "what_pmh",
        "spq_b_1", "spq_b_2", "spq_b_3", "spq_b_4", "spq_b_5",
        "spq_b_6", "spq_b_7", "spq_b_8", "spq_b_9", "spq_b_10",
        "spq_b_11", "spq_b_12", "spq_b_13", "spq_b_14", "spq_b_15",
        "spq_b_16", "spq_b_17", "spq_b_18", "spq_b_19", "spq_b_20",
        "spq_b_21", "spq_b_22",
        "oci_1", "oci_2", "oci_3", "oci_4", "oci_5",
        "oci_6", "oci_7", "oci_8", "oci_9", "oci_10",
        "oci_11", "oci_12", "oci_13", "oci_14", "oci_15",
        "oci_16", "oci_17", "oci_18", "oci_19", "oci_20",
        "oci_21", "oci_22", "oci_23", "oci_24", "oci_25",
        "oci_26", "oci_27", "oci_28", "oci_29", "oci_30",
        "oci_31", "oci_32", "oci_33", "oci_34", "oci_35",
        "oci_36", "oci_37", "oci_38", "oci_39", "oci_40",
        "oci_41", "oci_42",
        "phq_9_1", "phq_9_2", "phq_9_3", "phq_9_4", "phq_9_5",
        "phq_9_6", "phq_9_7", "phq_9_8", "phq_9_9",
        "stai_s_1", "stai_s_2", "stai_s_3", "stai_s_4", "stai_s_5",
        "stai_s_6", "stai_s_7", "stai_s_8", "stai_s_9", "stai_s_10",
        "stai_s_11", "stai_s_12", "stai_s_13", "stai_s_14", "stai_s_15",
        "stai_s_16", "stai_s_17", "stai_s_18", "stai_s_19", "stai_s_20",
        "stai_t_1", "stai_t_2", "stai_t_3", "stai_t_4", "stai_t_5",
        "stai_t_6", "stai_t_7", "stai_t_8", "stai_t_9", "stai_t_10",
        "stai_t_11", "stai_t_12", "stai_t_13", "stai_t_14", "stai_t_15",
        "stai_t_16", "stai_t_17", "stai_t_18", "stai_t_19", "stai_t_20",
        "aq_1", "aq_2", "aq_3", "aq_4", "aq_5",
        "aq_6", "aq_7", "aq_8", "aq_9", "aq_10",
        "aq_11", "aq_12", "aq_13", "aq_14", "aq_15",
        "aq_16", "aq_17", "aq_18", "aq_19", "aq_20",
        "aq_21", "aq_22", "aq_23", "aq_24", "aq_25",
        "aq_26", "aq_27", "aq_28", "aq_29", "aq_30",
        "aq_31", "aq_32", "aq_33", "aq_34", "aq_35",
        "aq_36", "aq_37", "aq_38", "aq_39", "aq_40",
        "aq_41", "aq_42", "aq_43", "aq_44", "aq_45",
        "aq_46", "aq_47", "aq_48", "aq_49", "aq_50",
        "asrs_1", "asrs_2", "asrs_3", "asrs_4", "asrs_5",
        "asrs_6", "asrs_7", "asrs_8", "asrs_9", "asrs_10",
        "asrs_11", "asrs_12", "asrs_13", "asrs_14", "asrs_15",
        "asrs_16", "asrs_17", "asrs_18",
        "audit_1", "audit_2", "audit_3", "audit_4", "audit_5",
        "audit_6", "audit_7", "audit_8", "audit_9", "audit_10",
        "eat_1", "eat_2", "eat_3", "eat_4", "eat_5",
        "eat_6", "eat_7", "eat_8", "eat_9", "eat_10",
        "eat_11", "eat_12", "eat_13", "eat_14", "eat_15",
        "eat_16", "eat_17", "eat_18", "eat_19", "eat_20",
        "eat_21", "eat_22", "eat_23", "eat_24", "eat_25",
        "eat_26",
        "dsm5_1", "dsm5_2", "dsm5_3", "dsm5_4", "dsm5_5",
        "dsm5_6", "dsm5_7", "dsm5_8", "dsm5_9", "dsm5_10",
        "dsm5_11", "dsm5_12", "dsm5_13", "dsm5_14", "dsm5_15",
        "dsm5_16", "dsm5_17", "dsm5_18", "dsm5_19", "dsm5_20",
        "dsm5_21", "dsm5_22", "dsm5_23",
        "ses_1", "ses_2", "ses_3", "ses_4", "ses_5",
        "ses_6",
        "L_1","L_2"
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code, participant.time_started_utc,
            p.age, p.sex, p.education, p.profession, p.height, p.weight, p.pmh, p.what_pmh,
            p.spq_b_1, p.spq_b_2, p.spq_b_3, p.spq_b_4, p.spq_b_5,
            p.spq_b_6, p.spq_b_7, p.spq_b_8, p.spq_b_9, p.spq_b_10,
            p.spq_b_11, p.spq_b_12, p.spq_b_13, p.spq_b_14, p.spq_b_15,
            p.spq_b_16, p.spq_b_17, p.spq_b_18, p.spq_b_19, p.spq_b_20,
            p.spq_b_21, p.spq_b_22,
            p.oci_1, p.oci_2, p.oci_3, p.oci_4, p.oci_5,
            p.oci_6, p.oci_7, p.oci_8, p.oci_9, p.oci_10,
            p.oci_11, p.oci_12, p.oci_13, p.oci_14, p.oci_15,
            p.oci_16, p.oci_17, p.oci_18, p.oci_19, p.oci_20,
            p.oci_21, p.oci_22, p.oci_23, p.oci_24, p.oci_25,
            p.oci_26, p.oci_27, p.oci_28, p.oci_29, p.oci_30,
            p.oci_31, p.oci_32, p.oci_33, p.oci_34, p.oci_35,
            p.oci_36, p.oci_37, p.oci_38, p.oci_39, p.oci_40,
            p.oci_41, p.oci_42,
            p.phq_9_1, p.phq_9_2, p.phq_9_3, p.phq_9_4, p.phq_9_5,
            p.phq_9_6, p.phq_9_7, p.phq_9_8, p.phq_9_9,
            p.stai_s_1, p.stai_s_2, p.stai_s_3, p.stai_s_4, p.stai_s_5,
            p.stai_s_6, p.stai_s_7, p.stai_s_8, p.stai_s_9, p.stai_s_10,
            p.stai_s_11, p.stai_s_12, p.stai_s_13, p.stai_s_14, p.stai_s_15,
            p.stai_s_16, p.stai_s_17, p.stai_s_18, p.stai_s_19, p.stai_s_20,
            p.stai_t_1, p.stai_t_2, p.stai_t_3, p.stai_t_4, p.stai_t_5,
            p.stai_t_6, p.stai_t_7, p.stai_t_8, p.stai_t_9, p.stai_t_10,
            p.stai_t_11, p.stai_t_12, p.stai_t_13, p.stai_t_14, p.stai_t_15,
            p.stai_t_16, p.stai_t_17, p.stai_t_18, p.stai_t_19, p.stai_t_20,
            p.aq_1, p.aq_2, p.aq_3, p.aq_4, p.aq_5,
            p.aq_6, p.aq_7, p.aq_8, p.aq_9, p.aq_10,
            p.aq_11, p.aq_12, p.aq_13, p.aq_14, p.aq_15,
            p.aq_16, p.aq_17, p.aq_18, p.aq_19, p.aq_20,
            p.aq_21, p.aq_22, p.aq_23, p.aq_24, p.aq_25,
            p.aq_26, p.aq_27, p.aq_28, p.aq_29, p.aq_30,
            p.aq_31, p.aq_32, p.aq_33, p.aq_34, p.aq_35,
            p.aq_36, p.aq_37, p.aq_38, p.aq_39, p.aq_40,
            p.aq_41, p.aq_42, p.aq_43, p.aq_44, p.aq_45,
            p.aq_46, p.aq_47, p.aq_48, p.aq_49, p.aq_50,
            p.asrs_1, p.asrs_2, p.asrs_3, p.asrs_4, p.asrs_5,
            p.asrs_6, p.asrs_7, p.asrs_8, p.asrs_9, p.asrs_10,
            p.asrs_11, p.asrs_12, p.asrs_13, p.asrs_14, p.asrs_15,
            p.asrs_16, p.asrs_17, p.asrs_18,
            p.audit_1, p.audit_2, p.audit_3, p.audit_4, p.audit_5,
            p.audit_6, p.audit_7, p.audit_8, p.audit_9, p.audit_10,
            p.eat_1, p.eat_2, p.eat_3, p.eat_4, p.eat_5,
            p.eat_6, p.eat_7, p.eat_8, p.eat_9, p.eat_10,
            p.eat_11, p.eat_12, p.eat_13, p.eat_14, p.eat_15,
            p.eat_16, p.eat_17, p.eat_18, p.eat_19, p.eat_20,
            p.eat_21, p.eat_22, p.eat_23, p.eat_24, p.eat_25,
            p.eat_26,
            p.dsm5_1, p.dsm5_2, p.dsm5_3, p.dsm5_4, p.dsm5_5,
            p.dsm5_6, p.dsm5_7, p.dsm5_8, p.dsm5_9, p.dsm5_10,
            p.dsm5_11, p.dsm5_12, p.dsm5_13, p.dsm5_14, p.dsm5_15,
            p.dsm5_16, p.dsm5_17, p.dsm5_18, p.dsm5_19, p.dsm5_20,
            p.dsm5_21, p.dsm5_22, p.dsm5_23,
            p.ses_1, p.ses_2, p.ses_3, p.ses_4, p.ses_5,
            p.ses_6,
            p.L_1, p.L_2
            ]


# PAGES
class Introduction(Page):
    pass

class Background(Page):
    form_model = 'player'
    form_fields = [
        "age", "sex", "education", "profession", "height", "weight", "pmh", "what_pmh"
    ]

class SPQ_B(Page):
    form_model = 'player'
    form_fields = [
        "L_1", "spq_b_1", "spq_b_2", "spq_b_3", "spq_b_4", "spq_b_5",
        "spq_b_6", "spq_b_7", "spq_b_8", "spq_b_9", "spq_b_10",
        "spq_b_11", "spq_b_12", "spq_b_13", "spq_b_14", "spq_b_15",
        "spq_b_16", "spq_b_17", "spq_b_18", "spq_b_19", "spq_b_20",
        "spq_b_21", "spq_b_22"
    ]

class OCI(Page):
    form_model = 'player'
    form_fields = [
        "oci_1", "oci_2", "oci_3", "oci_4", "oci_5",
        "oci_6", "oci_7", "oci_8", "oci_9", "oci_10",
        "oci_11", "oci_12", "oci_13", "oci_14", "oci_15",
        "oci_16", "oci_17", "oci_18", "oci_19", "oci_20",
        "oci_21", "oci_22", "oci_23", "oci_24", "oci_25",
        "oci_26", "oci_27", "oci_28", "oci_29", "oci_30",
        "oci_31", "oci_32", "oci_33", "oci_34", "oci_35",
        "oci_36", "oci_37", "oci_38", "oci_39", "oci_40",
        "oci_41", "oci_42"
        ]
    
class PHQ_9(Page):
    form_model = 'player'
    form_fields = [
        "phq_9_1", "phq_9_2", "phq_9_3", "phq_9_4", "phq_9_5",
        "phq_9_6", "phq_9_7", "phq_9_8", "phq_9_9"
    ]

class STAI_S(Page):
    form_model = 'player'
    form_fields = [
        "stai_s_1", "stai_s_2", "stai_s_3", "stai_s_4", "stai_s_5",
        "stai_s_6", "stai_s_7", "stai_s_8", "stai_s_9", "stai_s_10",
        "stai_s_11", "stai_s_12", "stai_s_13", "stai_s_14", "stai_s_15",
        "stai_s_16", "stai_s_17", "stai_s_18", "stai_s_19", "stai_s_20"
        ]
    
class STAI_T(Page):
    form_model = 'player'
    form_fields = [
        "stai_t_1", "stai_t_2", "stai_t_3", "stai_t_4", "stai_t_5",
        "stai_t_6", "stai_t_7", "stai_t_8", "stai_t_9", "stai_t_10",
        "stai_t_11", "stai_t_12", "stai_t_13", "stai_t_14", "stai_t_15",
        "stai_t_16", "stai_t_17", "stai_t_18", "stai_t_19", "stai_t_20"
        ]

class AQ(Page):
    form_model = 'player'
    form_fields = [
        "aq_1", "aq_2", "aq_3", "aq_4", "aq_5",
        "aq_6", "aq_7", "aq_8", "aq_9", "aq_10",
        "aq_11", "aq_12", "aq_13", "aq_14", "aq_15",
        "aq_16", "aq_17", "aq_18", "aq_19", "aq_20",
        "aq_21", "aq_22", "aq_23", "aq_24", "aq_25",
        "aq_26", "aq_27", "aq_28", "aq_29", "aq_30",
        "aq_31", "aq_32", "aq_33", "aq_34", "aq_35",
        "aq_36", "aq_37", "aq_38", "aq_39", "aq_40",
        "aq_41", "aq_42", "aq_43", "aq_44", "aq_45",
        "aq_46", "aq_47", "aq_48", "aq_49", "aq_50"
        ]

class ASRS(Page):
    form_model = 'player'
    form_fields = [
        "asrs_1", "asrs_2", "asrs_3", "asrs_4", "asrs_5",
        "asrs_6", "asrs_7", "asrs_8", "L_2", "asrs_9", "asrs_10",
        "asrs_11", "asrs_12", "asrs_13", "asrs_14", "asrs_15",
        "asrs_16", "asrs_17", "asrs_18"
        ]

class AUDIT(Page):
    form_model = 'player'
    form_fields = [
        "audit_1", "audit_2", "audit_3", "audit_4", "audit_5",
        "audit_6", "audit_7", "audit_8", "audit_9", "audit_10"
        ]

class EAT(Page):
    form_model = 'player'
    form_fields = [
        "eat_1", "eat_2", "eat_3", "eat_4", "eat_5",
        "eat_6", "eat_7", "eat_8", "eat_9", "eat_10",
        "eat_11", "eat_12", "eat_13", "eat_14", "eat_15",
        "eat_16", "eat_17", "eat_18", "eat_19", "eat_20",
        "eat_21", "eat_22", "eat_23", "eat_24", "eat_25",
        "eat_26"
        ]

class DSM5(Page):
    form_model = 'player'
    form_fields = [
        "dsm5_1", "dsm5_2", "dsm5_3", "dsm5_4", "dsm5_5",
        "dsm5_6", "dsm5_7", "dsm5_8", "dsm5_9", "dsm5_10",
        "dsm5_11", "dsm5_12", "dsm5_13", "dsm5_14", "dsm5_15",
        "dsm5_16", "dsm5_17", "dsm5_18", "dsm5_19", "dsm5_20",
        "dsm5_21", "dsm5_22", "dsm5_23"
        ]

class SES(Page):
    form_model = 'player'
    form_fields = [
        "ses_1", "ses_2", "ses_3", "ses_4", "ses_5",
        "ses_6"
        ]

class Finish(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        key_num = random.randint(0, 3)
        player.participant.keycode = Constants.keycode_list[key_num]

class KeyCode(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {"keycode" : player.participant.keycode}


page_sequence = [
    Introduction,
    Background,
    SPQ_B,
    OCI,
    PHQ_9,
    STAI_S,
    STAI_T,
    AQ,
    ASRS,
    AUDIT,
    EAT,
    DSM5,
    SES,
    Finish,
    KeyCode
    ]
