import pandas as pd

def main():
    games_ls = []

    with open('day2_input.txt') as file:
        for line in file:
            ID, sets = line.split(sep = ":")
            ID = int(ID.split(sep = " ")[1])
            games = [set.strip() for set in sets.replace(';', ',').split(',')]
            games_ls.append(max_count(ID, games))

    all_games = pd.DataFrame(games_ls, columns = ['ID', 'red', 'green', 'blue'])
    df_filtered = all_games.query('red <= 12 & green <= 13 & blue <= 14')
    print('First part: ', sum(df_filtered['ID'].tolist()))

    all_games['power'] = all_games['red'] * all_games['green'] * all_games['blue']
    print('Second part: ', sum(all_games['power']))

def max_count(ID, all_sets):
    red = 0
    green = 0
    blue = 0
    results = [color.split(sep = " ") for color in all_sets]

    for color in results:
        count = int(color[0])
        if color[1] == "red":
            if count >= red:
                red = count
        elif color[1] == "green":
            if count >= green:
                green = count
        else:
            if count >= blue:
                blue = count
    return([ID, red, green, blue])

main()