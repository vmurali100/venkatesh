from twilio.rest import Client
account_sid = "ACa10db09f599c8d3e4751132e9c310993"
auth_token = "474113cd9c00a40ba3a755fc149d8f0e"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to='+917760355535',
    from_='+12565137801',
    body='This is our First Messsage And Updated Now '
)
