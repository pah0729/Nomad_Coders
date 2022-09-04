days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri"]
days_of_week.append("Sat") # 추가
days_of_week.remove("Fri") # 삭제
print(days_of_week[3]) # index 활용

days = ("Mon", "Tue", "Wed")
print(days.index("Mon"))
print(days.count("Tue"))

player = {
    'name': 'Lucy',
    'age': 12,
    'alive': True,
    'fav_food': ["🍕", "🍔"]
}
player['fav_food'].append("🍜")
print(player.get('fav_food'))