class Loongtu:

    def __init__(self):
        self.name = 'Prayut'
        self.lastname = 'Chanocha'
        self.nickname = 'Loong tu'

    def WhoIAm(self):
        '''
        this is a function will show the name
        '''
        print('My name is: {}'.format(self.name))
        print('My lastname is: {}'.format(self.lastname))
        print('My nickname is: {}'.format(self.nickname))

    @property
    def email(self):
        '''

        this function will show an email
        '''
        return 'email: {}.{}@gmail.com'.format(self.name.lower(),self.lastname.lower())

    def thainame(self):
        print('ประยุทธ์ จันทร์โอชา')
        return 'ประยุทธ์ จันทร์โอชา'

    def __str__(self):
        return 'This is a Loongtu class'
    

if __name__ == '__main__':

    myloong = Loongtu()

    print(myloong)
    print(myloong.name)
    print(myloong.lastname)
    print(myloong.nickname)
    myloong.WhoIAm()
    print(myloong.email)
    myloong.thainame()

    print('--------')
    mypaa = Loongtu()
    mypaa.name = 'Somsri'
    mypaa.lastname = 'Konthai'
    mypaa.nickname = 'Sri'
    mypaa.WhoIAm()
    print(mypaa.name)
    print(mypaa.lastname)
    print(mypaa.nickname)





