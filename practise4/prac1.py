
from import_this import RACE_DATA
if __name__=="__main__":
    
    winner_racer:str=''
    if RACE_DATA[1]["FinishedPlace"]==1:
        winner_racer=("Выиграл-Vova!!! Поздравляем!!")
        print(winner_racer)
    elif RACE_DATA[2]["FinishedPlace"]==1:
        winner_racer=("Выиграл-Vova!!! Поздравляем!!")
        print(winner_racer)
    elif RACE_DATA[3]["FinishedPlace"]==1:
        winner_racer=("Выиграл-Gennady!!! Поздравляем!!")
        print(winner_racer)
    elif RACE_DATA[4]["FinishedPlace"]==1:
        winner_racer=("Выиграл-Grisha!!! Поздравляем!!")
        print(winner_racer)
    elif RACE_DATA[5]["FinishedPlace"]==1:
        winner_racer=("Выиграл-Grisha!!! Поздравляем!!")
        print(winner_racer)
    print("_"*len(winner_racer))
    
    print("\n Первые три места: \n")
    for place_racer in range(1,4):
        racer_option=f"\t Гонщик на {'первом' if place_racer==1 else'втором' if place_racer==2 else'третьем'} месте:"
        for i in RACE_DATA.values():
            if i.get("FinishedPlace",0)==place_racer:
                racer_option +=f"\n\t\tИмя:{i.get('RacerName')}\n"
                racer_option +=f"\t\tКоманда:{i.get('RacerTeam')}\n"
                racer_option +=f"\t\tВремя:{i.get('FinishedTimeSeconds')}'S'\n"
        print(racer_option)
 