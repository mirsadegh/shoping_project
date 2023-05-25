import ghasedakpack


sms = ghasedakpack.Ghasedak("44de33c2f3507b45d5ea4cca47878d8899653fbae469e9f0f6f3ffc91cf5e5fd")


sms.verification({'receptor': '09036131420', 'type': '1', 'template': 'randcode', 'param1': 'test'})


