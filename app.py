from modelos.time import Time

t1= Time('OnlyFabri', 27, 50)
t2 = Time('Loucos do Ibirap', 15, 40)
t3 = Time('Vila Idosa', 12, 60)
t4 = Time('Miralua', 14, 32)
t5 = Time('Americanos de Minas', 13, 23)
t6 = Time('Clube Mangas', 8, 32)
t7 = Time('TupiGuara', 5, 18)
t8 = Time('Velho-Horizonte', 14, 25)
t9 = Time('Opers', 19, 29)
t10 = Time('Goiax', 23, 23)
t11 = Time('Siara', 23, 22)
t12 = Time('Avaraguaí', 18, 33)
t13 = Time('PntPrt', 11, 21)
t14 = Time('Crtb', 10, 19)
t15 = Time('Psnd', 13, 31)
t16 = Time('Betstrits', 14, 31)
t17 = Time('Amazns', 18, 21)
t18 = Time('Chaps', 11, 22)
t19 = Time('Bruks', 12, 15)
t20 = Time('Boftg', 19, 41)

t1.receber_avaliacao('Roberto', 10)
t1.receber_avaliacao('Roberto', 5)
t2.receber_avaliacao('Roberto', 4)
t2.receber_avaliacao('Roberto', 2)
t3.receber_avaliacao('Roberto', 3)
t3.receber_avaliacao('Roberto', 7)
t4.receber_avaliacao('Roberto', 10)
t4.receber_avaliacao('Roberto', 10)
t5.receber_avaliacao('Roberto', 9)
t5.receber_avaliacao('Roberto', 8)
t6.receber_avaliacao('Roberto', 7)
t6.receber_avaliacao('Roberto', 9)
t7.receber_avaliacao('Roberto', 6)
t7.receber_avaliacao('Roberto', 7)
t8.receber_avaliacao('Roberto', 4)
t8.receber_avaliacao('Roberto', 3)
t9.receber_avaliacao('Roberto', 2)
t9.receber_avaliacao('Roberto', 5)
t10.receber_avaliacao('Roberto', 5)
t10.receber_avaliacao('Roberto', 4)
t11.receber_avaliacao('Roberto', 2)
t12.receber_avaliacao('Roberto', 3)
t14.receber_avaliacao('Roberto', 7)
t15.receber_avaliacao('Roberto', 10)
t17.receber_avaliacao('Roberto', 9)
t18.receber_avaliacao('Roberto', 8)
t19.receber_avaliacao('Roberto', 7)
t19.receber_avaliacao('Roberto', 9)
t20.receber_avaliacao('Roberto', 6)
t20.receber_avaliacao('Roberto', 7)
t18.receber_avaliacao('Roberto', 4)
t15.receber_avaliacao('Roberto', 3)
t15.receber_avaliacao('Roberto', 2)
t13.receber_avaliacao('Roberto', 10)
t13.receber_avaliacao('Roberto', 9)
t13.receber_avaliacao('Roberto', 4)
t16.receber_avaliacao('Roberto', 4)
t13.receber_avaliacao('Roberto', 5)
t13.receber_avaliacao('Roberto', 8)




# print(dir(t1)) # verificando os métodos especiais disponíveis
# print(vars(t2)) # Verificando os atributos do método


def main():
    Time.listar_times()

if __name__ == '__main__':
    main()