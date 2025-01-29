import pandas as pd
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_ID"] = "QandA ChatBot with OpenAI"

class QueryEngine:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_query(self, question: str) -> pd.DataFrame:
        """
        Uses OpenAI to generate a query based on the user's question
        and execute it on the DataFrame.
        """
        try:
            # Convert DataFrame to string
            data_preview = self.dataframe.head(5).to_csv(index=False)

            # Generate query prompt
            prompt = f"""
            You are a data analysis assistant specializing in Python Pandas. Analyze the following data and generate a pandas query:
            
            Data Preview:
            {data_preview}
            
            Question:
            {question}
            
            Provide only the code for a pandas query, no explanation. 
            The query should reference the DataFrame as 'self.dataframe'.
            """

            # Create completion using new API syntax
            response = self.client.chat.completions.create(
                model="gpt-4",  # or your preferred model
                messages=[
                    {"role": "system", "content": "You are a data analysis assistant that generates Pandas queries."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=500
            )

            # Extract generated query
            query = response.choices[0].message.content.strip()

            # Add safety check for the query
            if not query.startswith("self.dataframe"):
                query = f"self.dataframe{query}" if query.startswith(".") else f"self.dataframe.{query}"

            # Evaluate the query
            result = eval(query)
            return result

        except Exception as e:
            raise ValueError(f"Error generating query: {e}")

# Usage Example
if __name__ == "__main__":
    df = pd.read_csv("CSV_TNPD_1.csv")
    engine = QueryEngine(df)
    try:
        output = engine.generate_query("What are the top 5 rows?")
        print(output)
    except Exception as e:
        print(f"Error: {e}")