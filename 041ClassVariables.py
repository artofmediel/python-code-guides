from gametitle import GameTitle

game_1 = GameTitle("Valve","Half-Life","1998","FPS")
game_2 = GameTitle("Mojang","Minecraft","2011","Survival")

#game_1.player = 2
GameTitle.player = 2

print(game_1.player)
print(game_2.player)

print(GameTitle.player)

