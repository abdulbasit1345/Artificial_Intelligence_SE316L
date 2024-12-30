dinner_invites = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

print(f"Unfortunately, {dinner_invites[1]} can't make it to dinner.")

dinner_invites[1] = "Nikola Tesla"

print("\nUpdated Invitations:")
for person in dinner_invites:
    print(f"Dear {person}, I would be honored to have you join me for dinner.")
