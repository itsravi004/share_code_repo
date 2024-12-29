import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, BaseChatPromptTemplate, ChatMessagePromptTemplate

import os
from dotenv import load_dotenv

