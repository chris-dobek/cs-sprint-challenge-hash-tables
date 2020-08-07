#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Create a dictionary
    d = dict()

    # Store the length of Tickets into a variable
    route = [None] * length

    for ticket in tickets:
        # Set the ticket source to the ticket destination in the dict
        d[ticket.source] = ticket.destination
    
    # Reset the destination in the dict to none
    destination = d['NONE']

    # Search through the tickets through it's length
    for flight in range(length):
        # Set the route flight to the destination
        route[flight] = destination
        # Set the destination to the dict
        destination = d[destination]

    return route
