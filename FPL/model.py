# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the data
players_df = pd.read_csv('players_data.csv', encoding='windows-1252')

# Explore the data (you can add more exploration if needed)
print(players_df.head())
print(players_df.info())

# Choose your features and target
# For example, you might want to predict 'total_points' based on 'minutes' and 'goals_scored'
# You'll probably want to experiment with different features to get the best results
features = ['minutes', 'goals_scored']
target = 'total_points'

X = players_df[features]
y = players_df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
