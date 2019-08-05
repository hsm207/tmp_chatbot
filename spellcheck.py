
from typing import Any, Text, Optional, Dict

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import Message
from rasa.nlu.training_data import TrainingData


class SpellCheck(Component):
    """
    A simple spellcheck to correct common typos
    """

    name = "spellcheck"
    requires = []
    provides = ["original_text"]
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(SpellCheck, self).__init__(component_config)

        self.typos = {"teh": "the", "recomend": "recommend", "reccommend": "recommend"}

    def process(self, message: Message, **kwargs: Any) -> None:
        for spell_typo, spell_correct in self.typos.items():
            message.text = message.text.replace(spell_typo, spell_correct)

    def train(
        self, training_data: TrainingData, cfg: RasaNLUModelConfig, **kwargs: Any
    ) -> None:
        pass

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        pass
