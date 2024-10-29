import csv

def main():
    players_data = [
        "D. Henry,RB,BAL,8,9,2,,",
        "K. Williams,RB,LAR,7,8,2,0,0",
        "J. Cook,RB,BUF,7,7,,,",
        "J. Gibbs,RB,DET,7,6,,,",
        "A. Kamara,RB,NO,8,6,,,",
        "K. Walker III,RB,SEA,6,6,,,",
        "S. Barkley,RB,PHI,7,5,,,",
        "J. Mixon,RB,HOU,5,5,,,",
        "C. Brown,RB,CIN,8,4,,,",
        "Z. Charbonnet,RB,SEA,8,4,,,",
        "J. Hurts,QB,PHI,,7,7,,",
        "D. Montgomery,RB,DET,7,7,,,",
        "B. Robinson Jr.,RB,WAS,7,6,,,",
        "J. Fields,QB,PIT,6,5,,,",
        "R. Stevenson,RB,NE,7,5,,,",
        "J. Taylor,RB,IND,5,5,,,",
        "T. Bigsby,RB,JAC,8,4,,0,",
        "J. Conner,RB,ARI,8,4,,,",
        "J. Daniels,QB,WAS,8,4,,,"
    ]

    csv_filename = "players_data.csv"
    
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Assuming the header should be Player,Position,Team,Rushing Touchdowns,Receiving Touchdowns,Punt Return Touchdowns,Kickoff Return Touchdowns,Interceptions Returned for Touchdown,Fumble Recoveries Returned for Touchdown
        writer.writerow(["Player", "Position", "Team", "Rushing Touchdowns", "Receiving Touchdowns", "Punt Return Touchdowns", "Kickoff Return Touchdowns", "Interceptions Returned for Touchdown", "Fumble Recoveries Returned for Touchdown"])
        
        for player_data in players_data:
            # Replace multiple spaces with a single comma and strip any extra spaces
            clean_data = [field.strip() for field in player_data.split(',')]
            writer.writerow(clean_data)
    
    print(f"Data has been written to {csv_filename}")

if __name__ == "__main__":
    main()