import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.error import BoltError
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")
def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"Missing required environment variable: {name}", file=sys.stderr)
        print(f"Add it to {ROOT_DIR / '.env'}", file=sys.stderr)
        sys.exit(1)
    return value

try:
    app = App(token=require_env("SLACK_BOT_TOKEN"))
except BoltError as exc:
    print(f"Slack authentication failed: {exc}", file=sys.stderr)
    print(
        "Your SLACK_BOT_TOKEN is invalid or the app was uninstalled. "
        "Reinstall the app at https://api.slack.com/apps and update .env.",
        file=sys.stderr,
    )
    sys.exit(1)
@app.event("app_mention")
def handle_mention(event, say):
if __name__ == "__main__":
    handler = SocketModeHandler(app, require_env("SLACK_APP_TOKEN"))
    handler.start()
