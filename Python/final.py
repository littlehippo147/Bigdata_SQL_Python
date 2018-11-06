# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:22:35 2018

@author: user
"""

from myMod import *
while ( True ) :
        
    print(' ** 간단 계산기 ** ')
    print(' 종료 하려면 : 0 ')
    print(' **************** ')
    number1 = int(input(' 첫번째 수 : '))
    
    if ( number1 == 0 ):
        print(' Good - Bye! ')
        break
    oper = str(input(' +, -, *, / : '))
    number2 = int(input(' 두번째 수 : '))
    
    if ( oper == '+' ):
        res = plus( number1, number2 )
    elif ( oper == '-' ):
        res = minus( number1, number2 )
    elif ( oper == '*' ):
        res = multi( number1, number2 )
    elif ( oper == '/' ):
        res = divi( number1, number2 )
    else:
        print('{} 연산자 없음'.format(oper))
        
    print(' 결과 : {} {} {} = {}'.format(number1, oper, number2, res))
