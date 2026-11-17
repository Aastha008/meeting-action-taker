import os
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from src.models import MeetingSummary

class ActionExtractor:
    def __init__(self, llm: Optional[ChatOpenAI] = None):
        self._llm = llm
        self.parser = PydanticOutputParser(pydantic_object=MeetingSummary)

    @property
    def llm(self) -> ChatOpenAI:
        if self._llm is None:
            self._llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        return self._llm

    async def process_transcript(self, transcript: str) -> MeetingSummary:
        prompt = PromptTemplate(
            template="Extract action items and a summary from the following transcript.\n{format_instructions}\nTranscript: {transcript}",
            input_variables=["transcript"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()},
        )
        
        chain = prompt | self.llm | self.parser
        return await chain.ainvoke({"transcript": transcript})