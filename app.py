import streamlit as st
import pandas as pd
import numpy as np
from utils import update_payouts, get_team_owner

# Set page configuration
st.set_page_config(
    page_title="March Madness Calcutta Scenario Generator",
    page_icon="🏀",
    layout="wide"
)

# Custom CSS to ensure text is black in dataframes
st.markdown("""
<style>
    .stDataFrame {
        color: black !important;
    }
    .dataframe {
        color: black !important;
    }
    div[data-testid="stDataFrame"] div[data-testid="stTable"] {
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.title("March Madness Calcutta Scenario Generator")
st.markdown("""
This app calculates potential payouts for the March Madness Calcutta league based on Final Four and Championship outcomes.
Select winners for each matchup to see how payouts, profits, and ROI would change.
""")

# Initialize state if not already set
if 'final_four_1_winner' not in st.session_state:
    st.session_state.final_four_1_winner = None
if 'final_four_2_winner' not in st.session_state:
    st.session_state.final_four_2_winner = None
if 'champion' not in st.session_state:
    st.session_state.champion = None

# Initial data - current state
initial_owners_data = {
    'Owner': ['Lance', 'Brandon', 'Trevor', 'Percy', 'Sean', 'Elia', 'Trent', 'Lenny', 'Spotts', 'Jon', 'Ron'],
    'Spent': [14575.00, 7000.00, 11700.00, 18775.00, 650.00, 22072.00, 675.00, 1275.00, 600.00, 5075.00, 3750.00],
    'Payout': [14644.99, 6891.76, 9045.44, 13137.42, 1722.94, 22613.59, 1076.84, 1076.84, 0.00, 2153.68, 0.00],
    'Profit': [69.99, -108.24, -2654.57, -5637.58, 1072.94, 541.59, 401.84, -198.16, -600.00, -2921.33, -3750.00],
    'Total Teams': [10, 1, 8, 7, 1, 14, 1, 2, 1, 7, 12],
    'Wins': [12, 4, 6, 11, 2, 21, 1, 1, 0, 2, 0],
    'Teams Eliminated': [9, 0, 7, 6, 1, 14, 1, 2, 1, 7, 12],
    'Teams Remaining': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    '% ROI': ['0%', '-2%', '-23%', '-30%', '165%', '2%', '60%', '-16%', '-100%', '-58%', '-100%']
}

owners_df = pd.DataFrame(initial_owners_data)

# Payout structure
payout_structure = {
    0: 0.00,             # No wins
    1: 1076.84,          # Round of 32
    2: 1722.94,          # Sweet 16
    3: 3445.88,          # Elite 8
    4: 6891.76,          # Final 4
    5: 10337.64,         # Runner-Up
    6: 17229.40          # Champion
}

# Team information - with owners
teams = {
    'Auburn': {'owner': 'Brandon', 'seed': 1, 'region': 'South', 'reach': 'Final 4'},
    'Florida': {'owner': 'Trevor', 'seed': 1, 'region': 'West', 'reach': 'Final 4'},
    'Duke': {'owner': 'Percy', 'seed': 1, 'region': 'East', 'reach': 'Final 4'},
    'Houston': {'owner': 'Lance', 'seed': 1, 'region': 'Midwest', 'reach': 'Final 4'}
}

# Define the matchups
matchup_1 = ['Auburn', 'Florida']
matchup_2 = ['Duke', 'Houston']

# Tournament bracket visualization
st.header("Tournament Bracket")

# Create a traditional bracket layout with 3 columns
left_bracket, center_bracket, right_bracket = st.columns([2, 1.5, 2])

# Left bracket (South/West - Final Four Matchup 1)
with left_bracket:
    st.subheader("Final Four - Left Bracket")
    
    # Team 1 (Top)
    team1_selected = st.button(
        f"{matchup_1[0]} (South #1)\nOwner: {get_team_owner(matchup_1[0], teams)}",
        key="team1_button",
        use_container_width=True,
        type="primary" if st.session_state.final_four_1_winner == matchup_1[0] else "secondary"
    )
    
    # Vertical space between teams
    st.write("")
    st.write("")
    
    # Team 2 (Bottom)
    team2_selected = st.button(
        f"{matchup_1[1]} (West #1)\nOwner: {get_team_owner(matchup_1[1], teams)}",
        key="team2_button",
        use_container_width=True,
        type="primary" if st.session_state.final_four_1_winner == matchup_1[1] else "secondary"
    )
    
    # Handle selection
    if team1_selected:
        st.session_state.final_four_1_winner = matchup_1[0]
        # Reset champion if needed
        if st.session_state.champion in matchup_1 and st.session_state.champion != matchup_1[0]:
            st.session_state.champion = None
        # Force rerun to update UI immediately
        st.rerun()
            
    if team2_selected:
        st.session_state.final_four_1_winner = matchup_1[1]
        # Reset champion if needed
        if st.session_state.champion in matchup_1 and st.session_state.champion != matchup_1[1]:
            st.session_state.champion = None
        # Force rerun to update UI immediately
        st.rerun()

# Right bracket (East/Midwest - Final Four Matchup 2)
with right_bracket:
    st.subheader("Final Four - Right Bracket")
    
    # Team 3 (Top)
    team3_selected = st.button(
        f"{matchup_2[0]} (East #1)\nOwner: {get_team_owner(matchup_2[0], teams)}",
        key="team3_button",
        use_container_width=True,
        type="primary" if st.session_state.final_four_2_winner == matchup_2[0] else "secondary"
    )
    
    # Vertical space between teams
    st.write("")
    st.write("")
    
    # Team 4 (Bottom)
    team4_selected = st.button(
        f"{matchup_2[1]} (Midwest #1)\nOwner: {get_team_owner(matchup_2[1], teams)}",
        key="team4_button",
        use_container_width=True,
        type="primary" if st.session_state.final_four_2_winner == matchup_2[1] else "secondary"
    )
    
    # Handle selection
    if team3_selected:
        st.session_state.final_four_2_winner = matchup_2[0]
        # Reset champion if needed
        if st.session_state.champion in matchup_2 and st.session_state.champion != matchup_2[0]:
            st.session_state.champion = None
        # Force rerun to update UI immediately
        st.rerun()
            
    if team4_selected:
        st.session_state.final_four_2_winner = matchup_2[1]
        # Reset champion if needed
        if st.session_state.champion in matchup_2 and st.session_state.champion != matchup_2[1]:
            st.session_state.champion = None
        # Force rerun to update UI immediately
        st.rerun()

# Center bracket (Championship)
with center_bracket:
    st.subheader("Championship")
    
    # Add some space to align with teams
    st.write("")
    st.write("")
    
    # Championship container
    championship_container = st.container()
    
    with championship_container:
        # Only enable championship selection if both Final Four winners are selected
        if st.session_state.final_four_1_winner and st.session_state.final_four_2_winner:
            # Display the Final Four Winner from Left Bracket
            champ1_selected = st.button(
                f"{st.session_state.final_four_1_winner}\nOwner: {get_team_owner(st.session_state.final_four_1_winner, teams)}",
                key="champ1_button",
                use_container_width=True,
                type="primary" if st.session_state.champion == st.session_state.final_four_1_winner else "secondary"
            )
            
            # Space between championship teams
            st.write("")
            st.write("")
            
            # Display the Final Four Winner from Right Bracket
            champ2_selected = st.button(
                f"{st.session_state.final_four_2_winner}\nOwner: {get_team_owner(st.session_state.final_four_2_winner, teams)}",
                key="champ2_button",
                use_container_width=True,
                type="primary" if st.session_state.champion == st.session_state.final_four_2_winner else "secondary"
            )
            
            # Handle champion selection
            if champ1_selected:
                st.session_state.champion = st.session_state.final_four_1_winner
                # Force rerun to update UI immediately
                st.rerun()
                
            if champ2_selected:
                st.session_state.champion = st.session_state.final_four_2_winner
                # Force rerun to update UI immediately
                st.rerun()
                
            # Display champion (if selected)
            if st.session_state.champion:
                st.write("")
                st.write("")
                st.success(f"Champion: {st.session_state.champion}")
        else:
            st.info("Select winners from both brackets")
            
# Display the Champion Trophy container at the center bottom
if st.session_state.champion:
    st.subheader("🏆 Tournament Champion 🏆")
    champion_col = st.columns(3)[1]  # Center column
    with champion_col:
        st.success(f"{st.session_state.champion} (Owner: {get_team_owner(st.session_state.champion, teams)})")
        st.write(f"Payout Increase: ${payout_structure[6] - payout_structure[4]:,.2f}")

# Reset button
if st.button("Reset Selections", use_container_width=True):
    st.session_state.final_four_1_winner = None
    st.session_state.final_four_2_winner = None
    st.session_state.champion = None
    st.rerun()

# Display scenario information
st.header("Scenario Summary")
summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:
    if st.session_state.final_four_1_winner:
        st.success(f"Final Four Winner 1: {st.session_state.final_four_1_winner}")
    else:
        st.warning("Final Four Winner 1: Not Selected")

with summary_col2:
    if st.session_state.final_four_2_winner:
        st.success(f"Final Four Winner 2: {st.session_state.final_four_2_winner}")
    else:
        st.warning("Final Four Winner 2: Not Selected")

with summary_col3:
    if st.session_state.champion:
        st.success(f"Champion: {st.session_state.champion}")
    else:
        st.warning("Champion: Not Selected")

# Calculate and display updated payouts
st.header("Payout Scenarios")

# Calculate updated payouts based on selections
updated_df = update_payouts(
    owners_df.copy(), 
    teams,
    payout_structure,
    st.session_state.final_four_1_winner,
    st.session_state.final_four_2_winner,
    st.session_state.champion
)

# Format monetary values and apply styling
def style_monetary_values(df):
    """Apply background color for positive values and text color for negative values"""
    # Create a copy of the dataframe to avoid modifying the original
    df_copy = df.copy()
    
    # Apply formatting first
    df_styled = df_copy.style.format({
        'Spent': '${:,.2f}', 
        'Payout': '${:,.2f}', 
        'Profit': '${:,.2f}'
    })
    
    # Only apply background color to Profit column
    if 'Profit' in df_copy.columns:
        # Green background for positive values in Profit column only
        df_styled = df_styled.apply(lambda x: ['background-color: #b7e1cd' if v > 0 else '' for v in x], subset=['Profit'])
        # Red text for negative values in Profit column only
        df_styled = df_styled.apply(lambda x: ['color: #ff0000' if v < 0 else '' for v in x], subset=['Profit'])
    
    return df_styled

# Display current payouts with formatting
st.subheader("Current Payouts")
st.dataframe(style_monetary_values(owners_df), use_container_width=True)

# Only show updated payouts if any selections are made
if st.session_state.final_four_1_winner or st.session_state.final_four_2_winner or st.session_state.champion:
    st.subheader("Projected Payouts")
    
    # Format the dataframe to highlight changes
    def highlight_changes(row, col_name):
        if col_name in ['Payout', 'Profit', '% ROI']:
            current_val = owners_df.loc[row.name, col_name]
            new_val = row[col_name]
            
            if col_name == '% ROI':
                # Handle string percentage values
                try:
                    current_num = float(current_val.strip('%'))
                    new_num = float(new_val.strip('%'))
                    return 'background-color: green' if new_num > current_num else 'background-color: red' if new_num < current_num else ''
                except:
                    return ''
            else:
                # Handle numeric values
                return 'background-color: green' if new_val > current_val else 'background-color: red' if new_val < current_val else ''
        return ''
    
    # Apply simple styling for projected payouts
    styled_df = updated_df.style.format({
        'Spent': '${:,.2f}', 
        'Payout': '${:,.2f}', 
        'Profit': '${:,.2f}'
    })
    
    # Only apply colors to the Profit column
    if 'Profit' in updated_df.columns:
        # Apply background color only to Profit column (using subset to target specific column)
        styled_df = styled_df.apply(
            lambda x: ['background-color: #b7e1cd' if v > 0 else '' for v in x], 
            subset=['Profit']
        )
        # Apply red text only to negative values in Profit column
        styled_df = styled_df.apply(
            lambda x: ['color: #ff0000' if v < 0 else '' for v in x], 
            subset=['Profit']
        )
    
    st.dataframe(styled_df, use_container_width=True)
    
    # Show changes summary
    st.subheader("Changes Summary")
    changes_df = pd.DataFrame({
        'Owner': updated_df['Owner'],
        'Current Payout': owners_df['Payout'],
        'Projected Payout': updated_df['Payout'],
        'Difference': updated_df['Payout'] - owners_df['Payout'],
        'Current Profit': owners_df['Profit'],
        'Projected Profit': updated_df['Profit'],
        'Profit Change': updated_df['Profit'] - owners_df['Profit']
    })
    
    # Only show rows with changes
    changes_df = changes_df[changes_df['Difference'] != 0]
    
    if not changes_df.empty:
        # Apply formatting to the changes summary table
        styled_changes_df = changes_df.style.format({
            'Current Payout': '${:,.2f}',
            'Projected Payout': '${:,.2f}',
            'Difference': '${:,.2f}',
            'Current Profit': '${:,.2f}',
            'Projected Profit': '${:,.2f}',
            'Profit Change': '${:,.2f}'
        })
        
        # Only apply styling to profit-related columns
        profit_cols = ['Current Profit', 'Projected Profit', 'Profit Change']
        for col in profit_cols:
            # Green background for positive values in profit columns only
            styled_changes_df = styled_changes_df.apply(
                lambda x: ['background-color: #b7e1cd' if v > 0 else '' for v in x], 
                subset=[col]
            )
            # Red text for negative values in profit columns only
            styled_changes_df = styled_changes_df.apply(
                lambda x: ['color: #ff0000' if v < 0 else '' for v in x], 
                subset=[col]
            )
        
        st.dataframe(styled_changes_df, use_container_width=True)
    else:
        st.info("No changes in payouts with the current selections.")
else:
    st.info("Select winners to see projected payouts.")

# Display payout structure for reference
with st.expander("Payout Structure Reference"):
    payout_df = pd.DataFrame({
        'Wins': list(payout_structure.keys()),
        'Getting To': ['', 'Round of 32', 'Sweet 16', 'Elite 8', 'Final 4', 'Runner-Up', 'Champion'],
        'Percentage': ['0%', '1.25%', '2.00%', '4.00%', '8.00%', '12.00%', '20.00%'],
        'Payout': list(payout_structure.values())
    })
    
    # Format the payout structure table
    styled_payout_df = payout_df.style.format({
        'Payout': '${:,.2f}'
    })
    
    # Style positive payout values with safer approach
    styled_payout_df = styled_payout_df.apply(
        lambda x: ['background-color: #b7e1cd' if v > 0 else '' for v in x], 
        subset=['Payout']
    )
    
    st.dataframe(styled_payout_df, use_container_width=True)