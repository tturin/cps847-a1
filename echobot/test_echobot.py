import echobot

def test_parse_bot_commands():
	assert echobot.parse_bot_commands([]) == (None, None)