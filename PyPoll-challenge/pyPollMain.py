#print ("pyPoll")

#These are my column headers
'''
Voter ID	
County	
Candidate

worksheet name: election_data

'''
# Dependencies
import csv


# Files to use and create
fileToLoad = "/Users/eli/Desktop/Assignments/Week-4_Python1/python-challenge/PyPoll-challenge/raw-data/election_data.csv"
fileToOutput = "/Users/eli/Desktop/Assignments/Week-4_Python1/python-challenge/PyPoll-challenge/output/electionAnalysis_1.txt"

# Total vote counter
totalVotes = 0

#Candidate options and vote counters
candidateOptions = []
candidateVotes = {} #cand name and votes

# Winning candidates and winning count tracker
winningCandidate = ""
winningCount = 0

# Read in the csv and convert it into a list of dictionaries
with open(fileToLoad) as election_data:
    reader = csv.DictReader(election_data)

    # For each row...
    for row in reader:

        # Add to the total vote count
        totalVotes = totalVotes + 1

        #Extract the candidate name from each row
        candidateName = row["Candidate"]

        # If the candidate does not mathc any existing candidate...
        if candidateName not in candidateOptions:


            # Add it to the list of candidates in the running
            candidateOptions.append(candidateName)

            # And begin tracking that candidates voter count
            candidateVotes[candidateName] = 0

        # Then add a vote to the candidates count
        candidateVotes[candidateName] = candidateVotes[candidateName] + 1

#Print the resutls and export the data to our text file
with open(fileToOutput, "w") as txt_file:

    # print the final vote count
    electionResults = (
        f"\n\nElection Results:\n"
        f"----------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"----------------------\n"
    ) 

    print(electionResults)

    # Save the final vote count to the text file
    txt_file.write(electionResults)

    # Determine the winner by looping through the counts
    for candidate in candidateVotes:

        # Retrieve the vote count and percentage
        votes = candidateVotes.get(candidate)
        votePercentage = float(votes) / float(totalVotes) * 100

        # Determine winning vote coutnt and candidate
        if (votes > winningCount):
            winningCount = votes
            winningCandidate = candidate

        # Print each candidates voter count and percentage
        voterOutput = f"{candidate}: {votePercentage:.3f}% ({votes})\n"
        print(voterOutput)

        # Save each candidates voter count and percentage to text file
        txt_file.write(voterOutput)

    # Print the winning candidate
    winningCandidateSummary = (
        f"----------------------\n"
        f"Winner: {winningCandidate}\n"
        f"----------------------\n"
    )

    print(winningCandidateSummary)

    # Save the winning candidates name to the text file
    txt_file.write(winningCandidateSummary)

















