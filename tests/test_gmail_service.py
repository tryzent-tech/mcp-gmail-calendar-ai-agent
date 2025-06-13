import asyncio
import gmail_service


def test_get_mail_content(monkeypatch):
    monkeypatch.setattr(gmail_service.agent_executor, "invoke", lambda *a, **k: {"output": "output"})
    result = asyncio.run(gmail_service.get_mail_content("123"))
    assert result == "output"
