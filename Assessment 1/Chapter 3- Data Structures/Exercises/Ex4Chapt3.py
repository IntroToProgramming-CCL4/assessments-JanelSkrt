#make a list of people to invite
invited = ["Bins", "Dobi", "Danish"]
#define a function to send the invitations
def send_invitations(name):
    return f"Dear {name}, You are invited to dinner at my place. Please join me tonight."
#loop through the list and print
for person in invited:
    invitation = send_invitations(person)
    print(invitation)