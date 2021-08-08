from os import environ

SESSION_CONFIGS = [
    dict(
        name='categorization',
        display_name="categorization",
        app_sequence=['categorization'],
        num_demo_participants=2,
    ),
    dict(
        name='naminggame_one_feature',
        display_name="Naming-game One feature",
        app_sequence=['categorization', 'create_symbol'],
        num_demo_participants=2,
    ),
    # dict(
    #     name='public_goods',
    #     app_sequence=['public_goods'],
    #     num_demo_participants=3,
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    "img2category",
    "img2name",
    "stimuli_id_list",
    "stimuli_img_order",
    "imgPathSeries",
    ]
SESSION_FIELDS = ["test_id_list"]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3953047406988'

ROOMS = [
    dict(
        name='naming_game_revise',
        display_name='Naming-Game Revise1'
    ),
]