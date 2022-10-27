class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

user_input = input()

while not user_input == "Stop":
    user_input_tokens = user_input.split(' ')
    emails.append(Email(user_input_tokens[0], user_input_tokens[1], user_input_tokens[2]))

    user_input = input()

call_parameters = input().split(", ")

for parameter in call_parameters:
    emails[int(parameter)].send()

for email in emails:
    print(email.get_info())
