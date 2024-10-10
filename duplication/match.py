# match

def judge_season(month: int) -> str:
    match month:
        case 12 | 1 | 2:
            return "冬"
        case 3 | 4 | 5:
            return "春"
            

print(judge_season(month=1))
