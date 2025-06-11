import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

# initialise app
F1Bot = App(token=os.getenv("SLACK_BOT_TOKEN"))



@F1Bot.message("testing")
def test_message(message, say):
    say(
        blocks=[    #blocks are components of a slack message
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"success!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "test"},
                    "action_id": "button_click",
                    }
                
                }
            ],
        text="hello!"
        )

@F1Bot.action("button_click")
def button_clicked(body, ack, say):
    ack()
    say("button clicked!")

@F1Bot.event("message")
def handle_message_events(body, logger):
    logger.info(body)


# start
if __name__ == "__main__":
    SocketModeHandler(F1Bot, os.getenv("SLACK_APP_TOKEN")).start()

