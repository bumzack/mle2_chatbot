class BotContext:
    def __init__(self):
        self.data = {
            "intent_greeting": None,
            "intent_goodbye": None,
            "intent_thanks": None,
            "intent_noanswer": None,
            "intent_options": None,
            "intent_user_bored": None,
            "intent_pool_today": None,
            "intent_pool_tomorrow": None,
            "intent_pool_where": None,
            "intent_user_not_happy": None,
            "intent_user_approve": None,
            "day": None,
            "district": None
        }
