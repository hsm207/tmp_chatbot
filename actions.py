
import random
import sqlite3 as lite

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, Restarted

import datetime


class ActionRecommendTalk(Action):
    def name(self):
        return "action_recommend_session"

    def run(self, dispatcher, tracker, domain):
        conn = lite.connect("./ConfDB.db")
        cur = conn.cursor()

        relevant_audience = tracker.get_slot("relevant_audience")

        cur.execute(
            f"SELECT * from agenda WHERE relevant_audience like '%{relevant_audience}%'"
        )

        results = cur.fetchall()

        ind = random.randint(0, len(results))
        recommend_talk = list(results[ind])

        title, _, speaker, _, abstract, *_, length = recommend_talk

        dispatcher.utter_message(f"I would recommend you to attend {title}")

        return [
            SlotSet("speaker", speaker),
            SlotSet("abstract", abstract),
            SlotSet("length", length),
        ]


class ActionStartOver(Action):
    def name(self):
        return "action_start_over"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "I'm sorry, I don't understand what you are trying to say. Let's start over."
        )
        timestamp = datetime.datetime.now().timestamp()
        return [Restarted(timestamp=timestamp)]
