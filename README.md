# March Madness Calcutta Scenario Generator

An interactive Streamlit web application for visualizing and simulating different tournament outcomes and their associated payouts in a March Madness Calcutta-style league.

## Features

- **Tournament Bracket Visualization**: Traditional bracket format showing the Final Four and Championship matchups.
- **Interactive Team Selection**: Single-click interface for selecting winners in each round.
- **Real-time Payout Calculation**: Dynamically updates potential payouts based on selected scenarios.
- **Financial Projection Analysis**: Shows how each scenario affects owner profits and ROI.
- **Detailed Payout Information**: Current vs. Projected payouts with easy-to-understand summary tables.
- **Clean UI with Proper Monetary Formatting**: Dollar values formatted with appropriate styling.

## How It Works

1. The application displays the current Final Four teams and their owners.
2. Users can click on teams to select winners for each matchup.
3. The application immediately updates to show how those selections would affect payouts.
4. Changes are highlighted with appropriate color coding - green backgrounds for positive profit values and red text for negative values.
5. Users can reset selections and try different scenarios.

## Technologies Used

- **Streamlit**: Frontend framework for creating the interactive web application.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computing.

## Setup

1. Clone this repository.
2. Install the required packages: