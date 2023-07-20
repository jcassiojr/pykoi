"""This module provides a wrapper for the OpenAI model."""
import openai
from plotano.llm.abs_llm import AbsLlm


class OpenAIModel(AbsLlm):
    """
    A class that wraps the OpenAI model for use in the LLMChain.

    Attributes:
        _engine (str): The engine to use for the OpenAI model.
        _max_tokens (int): The maximum number of tokens to generate.
        _temperature (float): The temperature to use for the OpenAI model.

    Methods:
        __init__(self, api_key: str, engine: str, max_tokens: int, temperature: float): Initializes the OpenAI model.
        predict(self, message: str): Predicts the next word based on the given message.
    """

    def __init__(self,
                 api_key: str,
                 engine: str = "davinci",
                 max_tokens: int = 100,
                 temperature: float = 0.5):
        """
        Initializes the OpenAI model with the given parameters.

        Args:
            api_key (str): The API key for the OpenAI model.
            engine (str, optional): The engine to use for the OpenAI model. Defaults to "davinci".
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 100.
            temperature (float, optional): The temperature to use for the OpenAI model. Defaults to 0.5.
        """
        openai.api_key = api_key
        self._engine = engine
        self._max_tokens = max_tokens
        self._temperature = temperature
        super().__init__()

    def predict(self,
                message: str):
        """
        Predicts the next word based on the given message.

        Args:
            message (str): The message to base the prediction on.

        Returns:
            str: The predicted next word.
        """
        prompt = f"Question: {message}\nAnswer:"
        response = openai.Completion.create(
            engine=self._engine,
            prompt=prompt,
            max_tokens=self._max_tokens,
            n=1,
            stop=None,
            temperature=self._temperature,
        )
        return response.choices[0].text.split("\n")[0]