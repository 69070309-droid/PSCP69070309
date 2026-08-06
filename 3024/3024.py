"SurprisingVote"
totalvotes = float(input())
mostVotes = float(input())
leastVotes = max(0, totalvotes - (2 * mostVotes))
if mostVotes - leastVotes > 2:
    print("Surprising")
else:
    print("Not surprising")
