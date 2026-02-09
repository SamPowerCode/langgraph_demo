from dotenv import load_dotenv
import os


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    api_key = os.getenv("ANTHROPIC_API_KEY")
    print("Hello from langgraph-demo!")


if __name__ == "__main__":
    main()
