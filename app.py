from fastapi import FastAPI, Request
from composio_openai import ComposioToolSet, App
import gmail_service as gmail
import calender_service as calender

toolset = ComposioToolSet()                             # picks up COMPOSIO_API_KEY automatically :contentReference[oaicite:5]{index=5}

app = FastAPI()

@app.post("/webhook")
async def gmail_webhook(request: Request):
    body = await request.json()

    # Only run on the Gmail-new-message trigger
    if body.get("type") == "gmail_new_gmail_message":
        data       = body.get("data", {})
        message_id = data.get("id")  # or data.get("messageId"), depending on your payload

        # Print just the message ID
        print(f"📧 Message ID: {message_id}")

        # Call the Gmail service to get the message content
        message = await gmail.get_mail_content(message_id)
        # Checks if any event is present in the message and returns the summary of the event with the date and time it has been scheduled on otherwise just return the keyword 'None' and nothing else

        # If the message contains an event, set it in the calendar
        set_calender_event = await calender.set_calender_event(message)

    return {"status": set_calender_event}