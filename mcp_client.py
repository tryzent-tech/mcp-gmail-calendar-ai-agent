from composio_openai import ComposioToolSet, App
import app as a

toolset = ComposioToolSet()                             # picks up COMPOSIO_API_KEY automatically :contentReference[oaicite:5]{index=5}
entity  = toolset.get_entity(id="default")              # your Composio entity

res = entity.enable_trigger(
    app="GMAIL",
    trigger_name="GMAIL_NEW_GMAIL_MESSAGE",
    config={}
)
print(res["status"])  # enabled
  # should print "enabled"