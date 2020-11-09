class BotContext:
    def __init__(self):
        self.data = {
            "intent_greeting": False,
            "intent_goodbye": False,
            "intent_thanks": False,
            "intent_noanswer": False,
            "intent_options": False,
            "intent_user_bored": False,
            "intent_pool_today": False,
            "intent_pool_tomorrow": False,
            "intent_pool_where": False,
            "intent_user_not_happy": False,
            "intent_user_approve": False,
            "day": "",
            "district": "",
            "shown_pools": False
        }

    def setDay(self, day=None):
        self.data["day"] = day

    def setDistrict(self, district=None):
        self.data["district"] = district

    def setShownPools(self, val: bool = False):
        self.data["shown_pools"] = val

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

    def getDay(self) -> str:
        return self.data["day"]

    def getDistrict(self) -> str:
        return self.data["district"]

    def hasDay(self) -> bool:
        return self.data["day"] != ""

    def hasDistrict(self) -> bool:
        return self.data["district"] != ""

    def getIntentGreeting(self) -> bool:
        return self.data["intent_greeting"]

    def getIntentGoodBye(self) -> bool:
        return self.data["intent_goodbye"]

    def getIntentThanks(self) -> bool:
        return self.data["intent_thanks"]

    def getIntentNoanswer(self) -> bool:
        return self.data["intent_noanswer"]

    def getIntentOptions(self) -> bool:
        return self.data["intent_options"]

    def getIntentUSerBored(self) -> bool:
        return self.data["intent_user_bored"]

    def getIntentPoolToday(self) -> bool:
        return self.data["intent_pool_today"]

    def getIntentPoolTomorrow(self) -> bool:
        return self.data["intent_pool_tomorrow"]

    def getIntentPoolWhere(self) -> bool:
        return self.data["intent_pool_where"]

    def getIntentUseNotHappy(self) -> bool:
        return self.data["intent_user_not_happy"]

    def getIntentUserApprove(self) -> bool:
        return self.data["intent_user_approve"]

    def getShownPools(self) -> bool:
        return self.data["shown_pools"]
