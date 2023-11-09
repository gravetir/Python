player_1,player_2=input('Вввод: ').split()
if player_1=='камень' and  player_2== 'ножницы':
    print('игрок 1 победил')
elif player_1=='камень' and player_2 == 'бумага' :
    print('игрок 2 победил')
elif player_1=='ножницы' and player_2 == 'камень' :
    print('игрок 2 победил')
elif player_1=='ножницы' and player_2 == 'бумага' :
    print('игрок 1 победил')
elif player_1=='бумага' and player_2=='камень':
    print('игрок 1 победил')
elif player_1=='бумага' and player_2=='ножницы':
    print('игрок 2 победил')
else:
    print('ничья')
            