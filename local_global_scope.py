# enemies = 1  # Global scope: can be accessible anywhere
#
#
# def increase_enemies():
#     enemies = 2     # Local scope: only accessible inside the function
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
#
# print(f"enemies outside function: {enemies}")


# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]  # Global scope
# this new enemy variable can be accessible anywhere infect when it is in 'if' condition

# print(new_enemy)


# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[1]  # Local scope
#         # this new enemy variable cannot be accessible anywhere as it is in 'function'
#     print(new_enemy)
#
# create_enemy()
# print(new_enemy)    # this line generate the error


# Modifying the global scope

enemies = 1  # Global scope: can be accessible anywhere


def increase_enemies():
    # For accessing the global variable we need to use global keyword
    # but using global is a bad practice as it can cause generating bugs
    # instead of using global we can use the return keyword
    # global enemies
    # enemies += 1     # Local scope: only accessible inside the function
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()

print(f"enemies outside function: {enemies}")