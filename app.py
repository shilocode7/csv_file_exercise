import pandas as pd
import csv

df = pd.read_csv('data.csv')
# print(df.info())
# מה מחיר היהלום הגבוהה ביותר?
maxp = df.max()["price"]
print("the maximup price of the dimond is: ", maxp)
#מה המחיר הממוצע של יהלום?
# Open the CSV file and read the contents into a list
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    prices = [float(row['price']) for row in reader]
    cuts = [row['cut'] for row in reader]

# Calculate the average price
average_price = sum(prices) / len(prices)
print("the avarge prces is: ", average_price)
# כמה יהלומים מסוג Ideal קיימים?
ideal_count = df[df['cut'] == 'Ideal'].shape[0]
print(
    f"The number of occurrences of 'Ideal' in the 'cut' column is {ideal_count}")
#כמה צבעים שונים יש ליהלומים? מהם?
color_counts = df['color'].value_counts().to_dict()
print(color_counts)
# מה החציון קאראט של יהלומים מסוג Premium?
# filter the diamonds that have "Premium" in the cut column
premium_diamonds = df[df['cut'] == 'Premium']
# get the median carat of premium diamonds
median_carat = premium_diamonds['carat'].median()
print(f"The median carat of premium diamonds is {median_carat}")
# צרו ממוצע carat לכל סוג cut
# פרימיום
premium_diamonds = df[df['cut'] == 'Premium']
premium_avg = premium_diamonds['carat'].mean()
# אידאלי
Ideal_diamonds = df[df['cut'] == 'Ideal']
Ideal_avg = Ideal_diamonds['carat'].mean()
# טוב מאוד
Very_Good_diamonds = df[df['cut'] == 'Very Good']
Very_Good_avg = Very_Good_diamonds['carat'].mean()
#טוב
Good_diamonds = df[df['cut'] == 'Good']
Good_avg = Good_diamonds['carat'].mean()

print("the avarge cart of each type: premium: ", premium_avg, "Ideal: ", Ideal_avg,
      "Very Good: ",Very_Good_avg, "Good: ",Good_avg )
#צרו ממוצע מחיר לכל סוג צבע.
#group the diamonds by color and calculate the average price for each group
average_price_by_color = df.groupby('color')['price'].mean()
print(average_price_by_color)
