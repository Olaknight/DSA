def min_coins(cents):
    coins = dict()
    coins[25] = cents//25
    coins[10] = cents//10
    coins[1] = cents