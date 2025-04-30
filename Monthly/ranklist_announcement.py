def make_rank(contest_name,contest_id,sorted_rank_list):
    full_rank = [
        f"📢 Announcement: {contest_name} Rank List Published! 📢",
        f"We are thrilled to announce the publication of the rank list for {contest_name}, Contest ID: {contest_id}. Congratulations to all participants for their efforts and achievements. Here are the rankings of our performers:",
        f"🏆 Rank Lists 🏆",
    ]
    for rank, (name, position) in enumerate(sorted_rank_list, start=1):
        full_rank.append(f"{rank}. {name}: {position}th Position")

    count = 1
    top_rank =[
        f"We are thrilled to announce the top performers of {contest_name}:\n"
    ]
    emoji = [f"🥇",f"🥈",f"🥉"] 
    for name,rank in sorted_rank_list:
        top_rank.append(f"{count}. {emoji[count-1]} {name}")
        count+=1
        if count>3:
            break

    top_rank.append(f"Congratulations to these outstanding coders!")

    return [full_rank,top_rank]
    
    