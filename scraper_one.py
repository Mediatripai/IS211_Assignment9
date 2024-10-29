import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

# URL for CBS NFL Player Scoring Stats
url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/?sortcol=rutd&sortdir=descending"

def scrape_player_scoring_stats():
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data from: {url}. Status code: {response.status_code}")
        return [], [], [], []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the table containing the player statistics
    table = soup.find('table')

    # Check if the table was found
    if table is None:
        print(f"Could not find the statistics table on: {url}")
        return [], [], [], []

    # Extracting the rows of the table (excluding header)
    rows = table.find_all('tr')[1:21]  # Get top 20 players

    player_stats = []
    player_names = []
    rushing_touchdowns = []
    receiving_touchdowns = []

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 9:  # Ensure there are enough columns to avoid IndexError
            player_name = columns[0].text.strip()  # Extract player's name
            position = columns[1].text.strip()  # Extract position
            team = columns[2].text.strip()  # Extract team
            
            # Extract all relevant fields
            rtd = columns[3].text.strip()  # Rushing Touchdowns
            rtd = int(rtd) if rtd.isdigit() else 0  # Convert to int
            
            ret = columns[4].text.strip()  # Receiving Touchdowns
            ret = int(ret) if ret.isdigit() else 0  # Convert to int
            
            # Append data to lists for bar graph
            player_names.append(player_name)
            rushing_touchdowns.append(rtd)
            receiving_touchdowns.append(ret)
            
            # Format player data as a CSV string
            player_data_string = f"{player_name},{position},{team},{rtd},{ret},2,,,"
            player_stats.append(player_data_string)

            # Debugging output
            print(f"Player: {player_name}, Rushing TDs: {rtd}, Receiving TDs: {ret}")

        else:
            print("Unexpected row format.")

    return player_stats, player_names, rushing_touchdowns, receiving_touchdowns

def plot_bar_graph(player_names, rushing_touchdowns, receiving_touchdowns):
    x = range(len(player_names))

    # Create the bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(x, rushing_touchdowns, width=0.4, label='Rushing Touchdowns', color='b', align='center')
    plt.bar([p + 0.4 for p in x], receiving_touchdowns, width=0.4, label='Receiving Touchdowns', color='r', align='center')

    # Adding labels and title
    plt.xlabel('Players')
    plt.ylabel('Touchdowns')
    plt.title('Player Touchdowns Comparison')
    plt.xticks([p + 0.2 for p in x], player_names, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.grid(axis='y')

    # Show the plot
    plt.show()

def main():
    # Scrape the player statistics
    all_player_stats, player_names, rushing_touchdowns, receiving_touchdowns = scrape_player_scoring_stats()

    # Prepare to write to CSV
    csv_filename = "players_data.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write player statistics to CSV without headers
        print("Player data:")
        for player in all_player_stats:
            print(player)  # Print each player's data as a comma-separated string
            # Write to CSV as well
            csv_writer.writerow(player.split(','))  # Split by comma to write to CSV

    print(f"Data has been written to {csv_filename}")

    # Plot the bar graph
    plot_bar_graph(player_names, rushing_touchdowns, receiving_touchdowns)

if __name__ == "__main__":
    main()
