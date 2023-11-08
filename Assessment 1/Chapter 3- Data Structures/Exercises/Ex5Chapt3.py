#make a list of people to invite
invited = ["Bins", "Dobi", "Danish"]
#define a function to send the invitations
def send_invitations(name):
    return f"Dear {name}, You are invited to dinner at my place. Please join me tonight."

#print the name of the guest who cant go
guest_cant_go = "Dobi"
print(f"{guest_cant_go} cant make it to the dinner.")
#replace the guest who cant go with a new person
new_invited = "Gerard"
invited.remove(guest_cant_go)
invited.append(new_invited)
#print a second set of invitation messages
for person in invited:
    invitation = send_invitations(person)
    print(invitation)