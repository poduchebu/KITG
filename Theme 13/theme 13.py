def gale_shapley(men_preferences, women_preferences):
    # Инициализация: все мужчины и женщины свободны
    n = len(men_preferences)
    men = list(men_preferences.keys())
    women = list(women_preferences.keys())

    # Словарь для хранения текущих пар
    pairs = {}

    # Список свободных мужчин
    free_men = men.copy()

    # Словарь для хранения предложений, которые сделал каждый мужчина
    proposals = {man: 0 for man in men}

    while free_men:
        man = free_men.pop(0)
        # Получаем следующую женщину в списке предпочтений мужчины
        woman = men_preferences[man][proposals[man]]
        proposals[man] += 1

        if woman not in pairs:
            # Если женщина свободна, принимаем предложение
            pairs[woman] = man
        else:
            # Если женщина уже занята, сравниваем текущего партнера и нового претендента
            current_man = pairs[woman]
            if women_preferences[woman].index(man) < women_preferences[woman].index(current_man):
                # Женщина предпочитает нового мужчину
                pairs[woman] = man
                free_men.append(current_man)
            else:
                # Женщина предпочитает текущего мужчину
                free_men.append(man)

    # Возвращаем пары в формате {женщина: мужчина}
    return pairs


# Пример использования
men_preferences = {
    'm1': ['w1', 'w2', 'w3'],
    'm2': ['w2', 'w3', 'w1'],
    'm3': ['w3', 'w1', 'w2']
}

women_preferences = {
    'w1': ['m2', 'm1', 'm3'],
    'w2': ['m3', 'm2', 'm1'],
    'w3': ['m1', 'm3', 'm2']
}

stable_pairs = gale_shapley(men_preferences, women_preferences)
print("Стабильные пары:", stable_pairs)