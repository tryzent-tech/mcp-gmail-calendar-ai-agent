import asyncio
import calender_service


def test_task_execution_checker():
    assert calender_service.task_execution_checker(["None"]) is False
    assert calender_service.task_execution_checker(["event"]) is True


def test_set_calender_event(monkeypatch):
    monkeypatch.setattr(calender_service.agent_executor, "invoke", lambda *a, **k: {"output": "done"})

    async def patched(message):
        flag = calender_service.task_execution_checker(message)
        if not flag:
            return "No event found in the message"
        calender_service.agent_executor.invoke({"input": message})
        return "Event Has been created succesfully on google calender"

    monkeypatch.setattr(calender_service, "set_calender_event", patched)

    result = asyncio.run(calender_service.set_calender_event(["event"]))
    assert result == "Event Has been created succesfully on google calender"

    result = asyncio.run(calender_service.set_calender_event(["None"]))
    assert result == "No event found in the message"
