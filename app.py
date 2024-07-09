'''
Once we only want to test one of the specific playgrounds,
so we can run only python app.py with the different parser
to run the specific playground.
'''

import argparse
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from app.playground.classifier import build_classifier_demo


def main(*args: Any, **kwargs: Any,) -> None:
    parser = argparse.ArgumentParser(
        prog="todam-ticket-system",
        description="Run the server in different modes."
    )
    parser.add_argument(
        "--prod", action="store_true", 
        help="Run the server in production mode."
    )
    parser.add_argument(
        "--test", action="store_true", 
        help="Run the server in test mode."
    )
    parser.add_argument(
        "--dev", action="store_true", 
        help="Run the server in development mode."
    )
    parser.add_argument(
        "-p", "--port", type=int, default=8080,
        help="Specify the server port. Default is 8080."
    )
    
    args = parser.parse_args()

    project_root = Path(__file__).parent
    env_path = None

    if args.prod:
        env_path = project_root / ".env.prod"
    elif args.test:
        env_path = project_root / ".env.test"
    elif args.dev:
        env_path = project_root / ".env.dev"
    else:
        env_path = project_root / ".env"

    load_dotenv(env_path, override=True)

    demo = build_classifier_demo()
    demo.launch(
        server_port=args.port
    )

    return None

if __name__ == "__main__":
    main()
