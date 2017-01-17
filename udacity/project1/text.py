from twilio.rest import TwilioRestClient

account_sid =  "ACd7b1fdb85819ea0509dc0a3a5e43fe93" # Your Account SID from www.twilio.com/console
auth_token  = " dbbb4c8aecc6e082bdc502dfc606cdaa"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+17153387410",    # Replace with your phone number
    from_="+16515041858") # Replace with your Twilio number

print(message.sid)
