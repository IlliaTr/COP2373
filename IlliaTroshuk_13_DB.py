import sqlite3
import matplotlib.pyplot as plt

# Database name with initials
db_name = 'population_IT.db'

# Cities in Florida
cities = ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee', 'St. Petersburg', 'Fort Lauderdale', 'Hialeah', 'Sarasota', 'Gainesville']

# Initial population data for 2023
initial_population = [4559200, 320740, 403360, 985840, 202220, 263550, 183120, 221300, 57600, 145810]

# Connect to SQLite database
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Create the population table
c.execute('''
    CREATE TABLE IF NOT EXISTS population (
        city TEXT,
        year INTEGER,
        population INTEGER
    )
''')

# Insert initial data into the population table
for city, population in zip(cities, initial_population):
    c.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, 2023, population))

conn.commit()

# Function to simulate population growth
def simulate_population_growth(years=20, growth_rate=0.02):
    for city in cities:
        for year in range(2024, 2024 + years):
            # Get the last year's population
            c.execute('SELECT population FROM population WHERE city = ? AND year = ?', (city, year - 1))
            last_population = c.fetchone()[0]
            # Calculate the new population
            new_population = int(last_population * (1 + growth_rate))
            # Insert the new data into the table
            c.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, year, new_population))

    conn.commit()

# Function to plot population growth for a city
def plot_population_growth():
    print("Cities:", ", ".join(cities))
    city = input("Choose a city to visualize population growth: ")

    c.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (city,))
    data = c.fetchall()

    if data:
        years, populations = zip(*data)
        plt.plot(years, populations, marker='o')
        plt.title(f'Population Growth of {city}')
        plt.xlabel('Year')
        plt.ylabel('Population (thousands)')
        plt.grid(True)
        plt.show()
    else:
        print("No data available for the selected city.")

# Simulate population growth
simulate_population_growth()

# Plot the population growth for a user-selected city
plot_population_growth()

# Close the database connection
conn.close()
