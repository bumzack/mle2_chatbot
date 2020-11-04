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

    def setDay(self, day=None):
        self.data["day"] = day

    def setDistrict(self, district=None):
        self.data["district"] = district

    def setIntentGreeting(self):
        self.data["intent_greeting"] = True

    def setIntentGoodBye(self):
        self.data["intent_goodbye"] = True

    def setIntentThanks(self):
        self.data["intent_thanks"] = True

    def setIntentNoanswer(self):
        self.data["intent_noanswer"] = True

    def setIntentOptions(self):
        self.data["intent_options"] = True

    def setIntentUSerBored(self):
        self.data["intent_user_bored"] = True

    def setIntentPoolToday(self):
        self.data["intent_pool_today"] = True

    def setIntentPoolTomorrow(self):
        self.data["intent_pool_tomorrow"] = True

    def setIntentPoolWhere(self):
        self.data["intent_pool_where"] = True

    def setIntentUseNotHappy(self):
        self.data["intent_user_not_happy"] = True

    def setIntentUserApprove(self):
        self.data["intent_user_approve"] = True

    def print_context(self, title: str = ""):
        print("\n\n\n\n========================")
        print("BotContext:      " + title)
        print("========================")
        for key, value in self.data.items():
            print(key, ' -> ', value)
        print("========================")
