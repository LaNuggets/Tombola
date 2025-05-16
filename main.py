from getData import *

file = "tombola.xlsx"

firstName, lastName, ticketNumber = chipData(file)

participants = []
for i in range(len(ticketNumber)):
    participants.append(f"{firstName[i]} {lastName[i]} - Ticket: {ticketNumber[i]}")


print(participants)
