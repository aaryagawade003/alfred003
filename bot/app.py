import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.event("app_mention")
def handle_mention(event, say):
    user = event["user"]
    text = event["text"]
    channel = event["channel"]

    # ACK immediately — this is critical
    say(f"On it <@{user}>! I'll ping you when done 🤖")

    # For now just print — we'll wire SQS here later
    print(f"Job received: channel={channel}, text={text}")

if __name__ == "__main__":
    # Socket Mode — no public URL needed for local dev
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
