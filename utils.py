import pandas as pd
import numpy as np

def get_team_owner(team_name, teams_dict):
    """Get the owner of a specific team"""
    if team_name in teams_dict:
        return teams_dict[team_name]['owner']
    return "Unknown"

def update_payouts(df, teams, payout_structure, ff1_winner=None, ff2_winner=None, champion=None):
    """
    Update payouts based on scenario selections
    
    Parameters:
    - df: DataFrame with current owner data
    - teams: Dictionary with team information
    - payout_structure: Dictionary with payout amounts by tournament round
    - ff1_winner: Winner of first Final Four matchup
    - ff2_winner: Winner of second Final Four matchup
    - champion: Winner of championship game
    
    Returns:
    - Updated DataFrame with new payouts
    """
    # Create a copy to avoid modifying the original
    updated_df = df.copy()
    
    # Get list of all owners
    all_owners = df['Owner'].tolist()
    
    # Track additional payouts for each owner
    additional_payouts = {owner: 0 for owner in all_owners}
    
    # Process Final Four winners (Elite 8 -> Final 4)
    if ff1_winner:
        owner = get_team_owner(ff1_winner, teams)
        additional_payouts[owner] += payout_structure[4] - payout_structure[3]  # Final 4 bonus
    
    if ff2_winner:
        owner = get_team_owner(ff2_winner, teams)
        additional_payouts[owner] += payout_structure[4] - payout_structure[3]  # Final 4 bonus
    
    # Process championship game
    if champion and (ff1_winner and ff2_winner):
        # Determine runner-up
        runner_up = ff2_winner if champion == ff1_winner else ff1_winner
        
        # Champion bonus (Final 4 -> Champion)
        champion_owner = get_team_owner(champion, teams)
        additional_payouts[champion_owner] += payout_structure[6] - payout_structure[4]  # Champion bonus
        
        # Runner-up bonus (Final 4 -> Runner-up)
        runner_up_owner = get_team_owner(runner_up, teams)
        additional_payouts[runner_up_owner] += payout_structure[5] - payout_structure[4]  # Runner-up bonus
    
    # Update payouts in the DataFrame
    for idx, row in updated_df.iterrows():
        owner = row['Owner']
        if owner in additional_payouts:
            # Update payout
            updated_df.at[idx, 'Payout'] += additional_payouts[owner]
            
            # Update profit
            updated_df.at[idx, 'Profit'] = updated_df.at[idx, 'Payout'] - updated_df.at[idx, 'Spent']
            
            # Update ROI percentage
            if updated_df.at[idx, 'Spent'] > 0:
                roi = (updated_df.at[idx, 'Profit'] / updated_df.at[idx, 'Spent']) * 100
                updated_df.at[idx, '% ROI'] = f"{int(roi)}%" if roi == int(roi) else f"{roi:.0f}%"
            else:
                updated_df.at[idx, '% ROI'] = "0%"
    
    return updated_df